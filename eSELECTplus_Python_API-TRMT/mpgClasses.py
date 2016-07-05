import urllib2
import xml.sax
import socket

class mpgHttpsPost:
        __url = {'protocol' : 'https', 'port' : '443', 'file' : 'gateway2/servlet/MpgRequest' }
        __agent = "PYTHON - 1.0.0 - RISK"
        __timeout = 40
        __requestData = ""
        __Response = None       
        
        def __init__ (self, host, store_id, api_token, trxn):
                self.__trxn = trxn
                self.__storeId = store_id
                self.__apiToken = api_token
                self.__url["host"] = host
                self.__data = self.__toXml()
        
        
        def postRequest (self):         
                requestUrl = self.__url["protocol"] + "://" + self.__url["host"] + ":" + self.__url["port"] + "/" + self.__url["file"]
                try:
                        #print ("Request URL is: [" + requestUrl + "]") 
                        #print ("Data to send : " + self.__data)
                        requestObj = urllib2.Request(requestUrl, self.__data)
                        socket.setdefaulttimeout(self.__timeout)
                        requestObj.add_header("USER-AGENT", self.__agent)
                        requestObj.add_header("CONTENT-TYPE:", "text/xml")
                        
                        #Print string being sent
                        #print(self.__data)
                        
                        responsePacket = urllib2.urlopen(requestObj)
                        response = responsePacket.read()

                        #print ("******\n Got response of: " + response + "\n******")

                except urllib2.URLError, e:                     
                        response = self.__GlobalError(e)
   
                self.__Response = mpgResponse(response)


        def getResponse(self):
                return self.__Response

        def __toXml(self):
                request = "<request>" + "<store_id>" + self.__storeId + "</store_id>" + "<api_token>" + self.__apiToken + "</api_token>" + self.__trxn.toXml() + "</request>"
                return request

        def __GlobalError(self, error):
                errorNumber, errorMessage = error.reason
                errorResponse = '<?xml version="1.0" standalone="yes"?><response><receipt><ReceiptId>null</ReceiptId><ReferenceNum>null</ReferenceNum><ResponseCode>null</ResponseCode><ISO>null</ISO><AuthCode>null</AuthCode><TransTime>null</TransTime><TransDate>null</TransDate><TransType>null</TransType><Complete>false</Complete><Message>' + '[' + str(errorNumber) + '] ' + errorMessage + '</Message><TransAmount>null</TransAmount><CardType>null</CardType><TransID>null</TransID><TimedOut>null</TimedOut><BankTotals>null</BankTotals><Ticket>null</Ticket></receipt></response>'
                return errorResponse

class mpgResponse (xml.sax.handler.ContentHandler):
        
        def __init__(self, xmlResponse):
        
                handler = self.__xmlResponseHandler()
                xml.sax.parseString(xmlResponse, handler)
                self.__map = handler.getMap()
                self.__results = handler.getResults()
                self.__RuleNames = handler.getRuleNames()
                
        class __xmlResponseHandler (xml.sax.handler.ContentHandler):
                __currTag = ""
                __map = None
                __buffer = ""
                __results = None

                def __init__ (self):
                        self.__currTag = ""
                        self.__buffer = ""
                        self.__map = {}
                        self.__results = {}
                        self.__RuleNames = {}
                        self.__inResult = False
                        self.__inRule = False
                
                def startElement(self, name, attributes):                       
                        self.__currTag = name   
                        
                        if name == "Result":
                                self.__inResult = True
                        elif name == "Rule":
                                self.__inRule = True
                                self.__currRuleName = {}
                
                def characters (self,ch):
                        self.__buffer = self.__buffer + ch
                        
                def endElement(self, name):                     
                        if name == self.__currTag:
                                if self.__inResult :
                                        self.__results[name] = self.__buffer
                                
                                elif self.__inRule :
                                        self.__currRuleName[name] = self.__buffer
                                        if name == "RuleName":
                                                    self.__map["RuleName"] = self.__buffer

                                else:
                                        self.__map[name] = self.__buffer
                                        
                        if name == "Result":
                                self.__inResult = False
                        
                        elif name == "Rule":
                                self.__inRule = False
                                self.__RuleNames[self.__map["RuleName"]] = self.__currRuleName

                        else:
                                if name == "Card" :                                                                                                                     
                                        self.__currECR["Cards"][self.__currECRCardType] = self.__currECRCard
                                        self.__inECRCard = False
                                        
                        self.__buffer = ""
                        
                def getMap(self):
                        return self.__map
                
                def getResults(self):
                        return self.__results
                    
                def getRuleNames(self):
                        return self.__RuleNames
                
        def __getMapValue(self, dict, key):
                if key in dict:
                        return dict[key]    
                else:
                        return "null"
        def getResponseCode (self):
                return self.__map["ResponseCode"]

        def getMessage (self):
                return self.__map["Message"]

        def getResults(self):
            return self.__results
                    
        def getRuleNames(self):
            return self.__RuleNames
        
        def getRuleCode(self, ruleName):
                return self.__getMapValue(self.__RuleNames[ruleName], "RuleCode")
            
        def getRuleMessageEn(self, ruleName):
                return self.__getMapValue(self.__RuleNames[ruleName], "RuleMessageEn")
        
        def getRuleMessageFr(self, ruleName):
                return self.__getMapValue(self.__RuleNames[ruleName], "RuleMessageFr")
    
        
class mpgTransaction:
        def __init__(self):
                self._Request = ""
                self._tags = {}
                self._order
        
        def toXml(self):
                requestXml = "<" + self._Request + ">"
                for index, tag in enumerate(self._order):
                        value = self._tags[tag]                 
                        if isinstance(value, basestring):
                                requestXml = requestXml + "<" + tag + ">" + value + "</" + tag + ">"
                        elif isinstance(value, mpgTransaction):
                                requestXml = requestXml + value.toXml()
                        elif isinstance(value, list):
                                for item in value:                              
                                        requestXml = requestXml + item.toXml()
                        
                requestXml = requestXml + "</" + self._Request + ">"
                return requestXml

class RiskCheck(mpgTransaction):
        def __init__(self):
                self._Request = "risk"
                self._tags = {}
                self._order = []            

        def setSessionQuery (self, session_query):
                self._tags["session_query"] = session_query
                self._order.append("session_query")

        def setAttributeQuery (self, attribute_query):
                self._tags["attribute_query"] = attribute_query
                self._order.append("attribute_query")

        def setAssert (self, assertion):
                self._tags["assert"] = assertion
                self._order.append("assert")
                
class SessionQuery(mpgTransaction):
        def __init__(self, order_id, session_id, service_type):
                self._Request = "session_query"
                self._tags = {"order_id" : order_id, "session_id" : session_id, "service_type" : service_type, "event_type" : None, "session_account_info": None}
                self._order = ["order_id", "session_id", "service_type"]            

        def setSessionAccountInfo (self, session_account_info):
                self._tags["session_account_info"] = session_account_info
                self._order.append("session_account_info")

        def setEventType (self, event_type):
                self._tags["event_type"] = event_type
                self._order.append("event_type")        

class AttributeQuery(mpgTransaction):
        def __init__(self, order_id, service_type):
                self._Request = "attribute_query"
                self._tags = {"order_id" : order_id, "service_type" : service_type, "policy_id" : None, "attribute_account_info": None}
                self._order = ["order_id", "service_type"]            

        def setAttributeAccountInfo (self, attribute_account_info):
                self._tags["attribute_account_info"] = attribute_account_info
                self._order.append("attribute_account_info")

        def setPolicyId (self, policy_id):
                self._tags["policy_id"] = policy_id
                self._order.append("policy_id")

class SessionAccountInfo(mpgTransaction):
        def __init__(self) :
                self._Request = "session_account_info"
                self._tags = {}
                self._order = []
        
        def setPolicy (self, policy):
                self._tags["policy"] = policy
                self._order.append("policy")
            
        def setDeviceId (self, device_id):
                self._tags["device_id"] = device_id
                self._order.append("device_id")            
            
        def setAccountLogin (self, account_login):
                self._tags["account_login"] = account_login
                self._order.append("account_login")
            
        def setPasswordHash (self, password_hash):
                self._tags["password_hash"] = password_hash
                self._order.append("password_hash")
                
        def setAccountNumber (self, account_number):
                self._tags["account_number"] = account_number
                self._order.append("account_number")
            
        def setAccountName (self, account_name):
                self._tags["account_name"] = account_name
                self._order.append("account_name")
            
        def setAccountEmail (self, account_email):
                self._tags["account_email"] = account_email
                self._order.append("account_email")

        def setAccountTelephone (self, account_telephone):
                self._tags["account_telephone"] = account_telephone
                self._order.append("account_telephone")            

        def setPan (self, pan):
                self._tags["pan"] = pan
                self._order.append("pan")    
                        
        def setAccountAddressStreet1 (self, account_address_street1):
                self._tags["account_address_street1"] = account_address_street1
                self._order.append("account_address_street1")
            
        def setAccountAddressStreet2 (self, account_address_street2):
                self._tags["account_address_street2"] = account_address_street2
                self._order.append("account_address_street2")
            
        def setAccountAddressCity (self, account_address_city):
                self._tags["account_address_city"] = account_address_city
                self._order.append("account_address_city")
            
        def setAccountAddressState (self, account_address_state):
                self._tags["account_address_state"] = account_address_state
                self._order.append("account_address_state")
            
        def setAccountAddressCountry (self, account_address_country):
                self._tags["account_address_country"] = account_address_country
                self._order.append("account_address_country")
            
        def setAccountAddressZip (self, account_address_zip):
                self._tags["account_address_zip"] = account_address_zip
                self._order.append("account_address_zip")

        def setShippingAddressStreet1 (self, shipping_address_street1):
                self._tags["shipping_address_street1"] = shipping_address_street1
                self._order.append("shipping_address_street1")
            
        def setShippingAddressStreet2 (self, shipping_address_street2):
                self._tags["shipping_address_street2"] = shipping_address_street2
                self._order.append("shipping_address_street2")
            
        def setShippingAddressCity (self, shipping_address_city):
                self._tags["shipping_address_city"] = shipping_address_city
                self._order.append("shipping_address_city")
            
        def setShippingAddressState (self, shipping_address_state):
                self._tags["shipping_address_state"] = shipping_address_state
                self._order.append("shipping_address_state")
            
        def setShippingAddressCountry (self, shipping_address_country):
                self._tags["shipping_address_country"] = shipping_address_country
                self._order.append("shipping_address_country")
            
        def setShippingAddressZip (self, shipping_address_zip):
                self._tags["shipping_address_zip"] = shipping_address_zip
                self._order.append("shipping_address_zip")
            
        def setLocalAttrib1 (self, local_attrib_1):
                self._tags["local_attrib_1"] = local_attrib_1
                self._order.append("local_attrib_1")
            
        def setLocalAttrib2 (self, local_attrib_2):
                self._tags["local_attrib_2"] = local_attrib_2
                self._order.append("local_attrib_2")    

        def setLocalAttrib3 (self, local_attrib_3):
                self._tags["local_attrib_3"] = local_attrib_3
                self._order.append("local_attrib_3")    

        def setLocalAttrib4 (self, local_attrib_4):
                self._tags["local_attrib_4"] = local_attrib_4
                self._order.append("local_attrib_4")    

        def setLocalAttrib5 (self, local_attrib_5):
                self._tags["local_attrib_5"] = local_attrib_5
                self._order.append("local_attrib_5")
            
        def setTransactionAmount (self, transaction_amount):
                self._tags["transaction_amount"] = transaction_amount
                self._order.append("transaction_amount")    

        def setTransactionCurrency (self, transaction_currency):
                self._tags["transaction_currency"] = transaction_currency
                self._order.append("transaction_currency")    
                
class AttributeAccountInfo(mpgTransaction):
        def __init__(self) :
                self._Request = "attribute_account_info"
                self._tags = {}
                self._order = []
        
        def setDeviceId (self, device_id):
                self._tags["device_id"] = device_id
                self._order.append("device_id")            
            
        def setAccountLogin (self, account_login):
                self._tags["account_login"] = account_login
                self._order.append("account_login")
            
        def setPasswordHash (self, password_hash):
                self._tags["password_hash"] = password_hash
                self._order.append("password_hash")
            
        def setAccountNumber (self, account_number):
                self._tags["account_number"] = account_number
                self._order.append("account_number")
            
        def setAccountName (self, account_name):
                self._tags["account_name"] = account_name
                self._order.append("account_name")
            
        def setAccountEmail (self, account_email):
                self._tags["account_email"] = account_email
                self._order.append("account_email")

        def setAccountTelephone (self, account_telephone):
                self._tags["account_telephone"] = account_telephone
                self._order.append("account_telephone")            

        def setCCNumberHash (self, cc_number_hash):
                self._tags["cc_number_hash"] = cc_number_hash
                self._order.append("cc_number_hash")    

        def setIPAddress (self, ip_address):
                self._tags["ip_address"] = ip_address
                self._order.append("ip_address")
            
        def setIPForwarded (self, ip_forwarded):
                self._tags["ip_forwarded"] = ip_forwarded
                self._order.append("ip_forwarded")    
                
        def setAccountAddressStreet1 (self, account_address_street1):
                self._tags["account_address_street1"] = account_address_street1
                self._order.append("account_address_street1")
            
        def setAccountAddressStreet2 (self, account_address_street2):
                self._tags["account_address_street2"] = account_address_street2
                self._order.append("account_address_street2")
            
        def setAccountAddressCity (self, account_address_city):
                self._tags["account_address_city"] = account_address_city
                self._order.append("account_address_city")
            
        def setAccountAddressState (self, account_address_state):
                self._tags["account_address_state"] = account_address_state
                self._order.append("account_address_state")
            
        def setAccountAddressCountry (self, account_address_country):
                self._tags["account_address_country"] = account_address_country
                self._order.append("account_address_country")
            
        def setAccountAddressZip (self, account_address_zip):
                self._tags["account_address_zip"] = account_address_zip
                self._order.append("account_address_zip")

        def setShippingAddressStreet1 (self, shipping_address_street1):
                self._tags["shipping_address_street1"] = shipping_address_street1
                self._order.append("shipping_address_street1")
            
        def setShippingAddressStreet2 (self, shipping_address_street2):
                self._tags["shipping_address_street2"] = shipping_address_street2
                self._order.append("shipping_address_street2")
            
        def setShippingAddressCity (self, shipping_address_city):
                self._tags["shipping_address_city"] = shipping_address_city
                self._order.append("shipping_address_city")
            
        def setShippingAddressState (self, shipping_address_state):
                self._tags["shipping_address_state"] = shipping_address_state
                self._order.append("shipping_address_state")
            
        def setShippingAddressCountry (self, shipping_address_country):
                self._tags["shipping_address_country"] = shipping_address_country
                self._order.append("shipping_address_country")
            
        def setShippingAddressZip (self, shipping_address_zip):
                self._tags["shipping_address_zip"] = shipping_address_zip
                self._order.append("shipping_address_zip")

class Assert(mpgTransaction):
        def __init__(self, orig_order_id, activities_description, impact_description, confidence_description):
                self._Request = "assert"
                self._tags = {"orig_order_id" : orig_order_id, "activities_description" : activities_description, "impact_description" : impact_description, "confidence_description": confidence_description}
                self._order = ["orig_order_id", "activities_description", "impact_description", "confidence_description"]            
            