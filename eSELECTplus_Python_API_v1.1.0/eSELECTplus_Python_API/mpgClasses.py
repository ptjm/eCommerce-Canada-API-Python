import urllib2
import xml.sax
import socket

class mpgHttpsPost:
        __url = {'protocol' : 'https', 'port' : '443', 'file' : 'gateway2/servlet/MpgRequest' }
        __agent = "Python API 1.1.0"
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
                        requestObj.add_header("USER-AGENT", self.__agent)
                        requestObj.add_header("CONTENT-TYPE", "text/xml")
                        responsePacket = urllib2.urlopen(requestObj, timeout=self.__timeout)
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
                self.__ECRs = handler.getECRs()
                
                
        class __xmlResponseHandler (xml.sax.handler.ContentHandler):
                __currTag = ""
                __map = None
                __buffer = ""
                __ECRs = None

                def __init__ (self):
                        self.__currTag = ""
                        self.__buffer = ""
                        self.__map = {}
                        self.__ECRs = {}
                        self.__isBankTotal = False
                        self.__inECR = False

                
                def startElement(self, name, attributes):                       
                        self.__currTag = name   
                        
                        if self.__inECR :
                                if name == "Card":                              
                                        self.__inECRCard = True
                                        self.__currECRCard = {}
                                elif name != "Amount" and name != "Count" :
                                        self.__currTransType = name
                                        
                        if name == "BankTotals":
                                self.__isBankTotal = True
                        elif name == "ECR":
                                self.__inECR = True
                                self.__inECRCard = False
                                self.__currECR = {}
                                self.__currECR["CardTypes"] = []
                                self.__currECR["Cards"] = {}
                                
                        
                                        
                
                def characters (self,ch):
                        self.__buffer = self.__buffer + ch
                        
                
                def endElement(self, name):                     
                        if name == self.__currTag:
                                if self.__inECR :
                                        if self.__inECRCard :                                                                           
                                                if name == "CardType" : 
                                                        self.__currECR["CardTypes"].append(self.__buffer)
                                                        self.__currECRCard[name] = self.__buffer
                                                        self.__currECRCardType = self.__buffer
                                                else : 
                                                        self.__currECRCard[self.__currTransType + name] = self.__buffer

                                        else:           
                                                self.__currECR[name] = self.__buffer
                                else:
                                        self.__map[name] = self.__buffer
                                        
                        if name == "BankTotals":                        
                                self.__isBankTotal = False
                                
                        elif name == "ECR":
                                self.__inECR = False
                                self.__ECRs[self.__currECR["term_id"]] = self.__currECR
                        else:
                                if name == "Card" :                                                                                                                     
                                        self.__currECR["Cards"][self.__currECRCardType] = self.__currECRCard
                                        self.__inECRCard = False
                                        
                        self.__buffer = ""
                        
                def getMap(self):
                        return self.__map
                
                def getECRs(self):
                        return self.__ECRs
        
        def getReceiptId (self):
                return self.__map["ReceiptId"]

        def getReferenceNum (self):
                return self.__map["ReferenceNum"]

        def getResponseCode (self):
                return self.__map["ResponseCode"]

        def getISO (self):
                return self.__map["ISO"]

        def getAuthCode (self):
                return self.__map["AuthCode"]

        def getTransTime (self):
                return self.__map["TransTime"]

        def getTransDate (self):
                return self.__map["TransDate"]

        def getTransType (self):
                return self.__map["TransType"]

        def getComplete (self):
                return self.__map["Complete"]

        def getMessage (self):
                return self.__map["Message"]

        def getTransAmount (self):
                return self.__map["TransAmount"]

        def getCardType (self):
                return self.__map["CardType"]

        def getTransID (self):
                return self.__map["TransID"]

        def getTimedOut (self):
                return self.__map["TimedOut"]

        def getBankTotals (self):
                return self.__map["BankTotals"]

        def getTicket (self):
                return self.__map["Ticket"]
                
        def getAvsResultCode (self):
                return self.__map["AvsResultCode"]
                
        def getCvdResultCode (self):
                return self.__map["CvdResultCode"]

        def getRecurSuccess (self):
                return self.__map["RecurSuccess"]

        def getRecurUpdateSuccess (self):
                return self.__map["RecurUpdateSuccess"]

        def getNextRecurDate (self):
                return self.__map["NextRecurDate"]

        def getRecurEndDate (self):
                return self.__map["RecurEndDate"]
                
        def getECRs (self):
                return self.__ECRs
        
        def getCardTypes (self, ecr):
                return self.__ECRs[ecr]["CardTypes"]
                
        def getPurchaseCount (self, ecr, cardType):
                return self.__ECRs[ecr]["Cards"][cardType]["PurchaseCount"]
                
        def getPurchaseAmount (self, ecr, cardType):
                return self.__ECRs[ecr]["Cards"][cardType]["PurchaseAmount"]

        def getRefundCount (self, ecr, cardType):
                return self.__ECRs[ecr]["Cards"][cardType]["RefundCount"]
                
        def getRefundAmount (self, ecr, cardType):
                return self.__ECRs[ecr]["Cards"][cardType]["RefundAmount"]

        def getCorrectionCount (self, ecr, cardType):
                return self.__ECRs[ecr]["Cards"][cardType]["CorrectionCount"]
                
        def getCorrectionAmount (self, ecr, cardType):
                return self.__ECRs[ecr]["Cards"][cardType]["CorrectionAmount"]

        def getPurchaseCount (self, ecr, cardType):
                return self.__ECRs[ecr]["Cards"][cardType]["PurchaseCount"]
                
        def getPurchaseAmount (self, ecr, cardType):
                return self.__ECRs[ecr]["Cards"][cardType]["PurchaseAmount"]


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

class Purchase(mpgTransaction):
        def __init__(self, order_id, amount, pan, expdate, crypt_type):
                self._Request = "purchase"
                self._tags = {"order_id" : order_id, "amount" : amount, "pan" : pan, "expdate" : expdate, "crypt_type" : crypt_type, "cvd": None, "avs": None}
                self._order = ["order_id", "amount", "pan", "expdate", "crypt_type"]            

        def setCustId (self, cust_id):
                self._tags["cust_id"] = cust_id
                self._order.append("cust_id")
        
        def setCvdInfo (self, cvdInfo):
                self._tags["cvd"] = cvdInfo
                self._order.append("cvd")

        def setAvsInfo (self, avsInfo):
                self._tags["avs"] = avsInfo
                self._order.append("avs")

        def setCustInfo (self, custInfo):
                self._tags["CustInfo"] = custInfo
                self._order.append("CustInfo")

        def setRecur (self, recur):
                self._tags["recur"] = recur
                self._order.append("recur")

class Preauth(mpgTransaction):
        def __init__(self, order_id, amount, pan, expdate, crypt_type):
                self._Request = "preauth"
                self._tags = {"order_id" : order_id, "amount" : amount, "pan" : pan, "expdate" : expdate, "crypt_type" : crypt_type, "cvd": None, "avs": None}
                self._order = ["order_id", "amount", "pan", "expdate", "crypt_type"]

        def setCustId (self, cust_id):
                self._tags["cust_id"] = cust_id
                self._order.append("cust_id")
        
        def setCvdInfo (self, cvdInfo):
                self._tags["cvd"] = cvdInfo
                self._order.append("cvd")

        def setAvsInfo (self, avsInfo):
                self._tags["avs"] = avsInfo
                self._order.append("avs")

        def setCustInfo (self, custInfo):
                self._tags["CustInfo"] = custInfo
                self._order.append("CustInfo")


class Correction(mpgTransaction):
        def __init__(self, order_id, txn_number, crypt_type):
                self._Request = "purchasecorrection"
                self._tags = {"order_id" : order_id, "txn_number" : txn_number, "crypt_type" : crypt_type}
                self._order = ["order_id", "txn_number", "crypt_type"]

        def setShipIndicator(self, ship_indicator):
                self._tags["ship_indicator"] = ship_indicator
                self._order.append("ship_indicator")

        def toXml(self):
                return mpgTransaction.toXml(self)


class Completion(mpgTransaction):
        def __init__(self, order_id, comp_amount, txn_number, crypt_type):
                self._Request = "completion"
                self._tags = {"order_id" : order_id, "comp_amount" : comp_amount, "txn_number" : txn_number, "crypt_type" : crypt_type}
                self._order = ["order_id", "comp_amount", "txn_number", "crypt_type"]
                
        def setShipIndicator(self, ship_indicator):
                self._tags["ship_indicator"] = ship_indicator
                self._order.append("ship_indicator")
        

class Refund(mpgTransaction):
        def __init__(self, order_id, amount, crypt_type, txn_number):
                self._Request = "refund"
                self._tags = {"order_id" : order_id, "amount" : amount, "txn_number" : txn_number, "crypt_type" : crypt_type}
                self._order = ["order_id", "amount", "txn_number", "crypt_type"]

class IndRefund(mpgTransaction):
        def __init__(self, order_id, amount, pan, expdate, crypt_type):
                self._Request = "ind_refund"
                self._tags = {"order_id" : order_id, "amount" : amount, "pan" : pan, "expdate" : expdate, "crypt_type" : crypt_type}
                self._order = ["order_id", "amount", "pan", "expdate", "crypt_type"]
                
        def setCustId (self, cust_id):
                self._tags["cust_id"] = cust_id
                self._order.append("cust_id")

class iDebitPurchase(mpgTransaction):
        def __init__(self, order_id, amount, idebit_track2):
                self._Request = "idebit_purchase"
                self._tags = {"order_id" : order_id, "amount" : amount, "idebit_track2" : idebit_track2 } 
                self._order = ["order_id","amount","idebit_track2"]

class iDebitRefund(mpgTransaction):
        def __init__(self, order_id, amount, txn_number):
                self._Request = "idebit_refund"
                self._tags = {"order_id" : order_id, "amount" : amount, "txn_number" : txn_number } 
                self._order = ["order_id","amount","txn_number"]

class OpenTotals(mpgTransaction):
        def __init__(self, ecr_number):
                self._Request = "opentotals"
                self._tags = {"ecr_number" : ecr_number } 
                self._order = ["ecr_number"]

class BatchClose(mpgTransaction):
        def __init__(self, ecr_number):
                self._Request = "batchclose"
                self._tags = {"ecr_number" : ecr_number } 
                self._order = ["ecr_number"]

class CavvPurchase(mpgTransaction):
        def __init__(self, order_id, amount, pan, expdate, cavv):
                self._Request = "cavv_purchase"
                self._tags = {"order_id" : order_id, "amount" : amount, "pan" : pan, "expdate" : expdate, "cavv" : cavv, "cvd": None, "avs": None}
                self._order = ["order_id", "amount", "pan", "expdate", "cavv"]            

        def setCustId (self, cust_id):
                self._tags["cust_id"] = cust_id
                self._order.append("cust_id")
        
        def setCvdInfo (self, cvdInfo):
                self._tags["cvd"] = cvdInfo
                self._order.append("cvd")

        def setAvsInfo (self, avsInfo):
                self._tags["avs"] = avsInfo
                self._order.append("avs")

        def setCustInfo (self, custInfo):
                self._tags["CustInfo"] = custInfo
                self._order.append("CustInfo")

class CavvPreauth(mpgTransaction):
        def __init__(self, order_id, amount, pan, expdate, cavv):
                self._Request = "cavv_preauth"
                self._tags = {"order_id" : order_id, "amount" : amount, "pan" : pan, "expdate" : expdate, "cavv" : cavv, "cvd": None, "avs": None}
                self._order = ["order_id", "amount", "pan", "expdate", "cavv"]            

        def setCustId (self, cust_id):
                self._tags["cust_id"] = cust_id
                self._order.append("cust_id")
        
        def setCvdInfo (self, cvdInfo):
                self._tags["cvd"] = cvdInfo
                self._order.append("cvd")

        def setAvsInfo (self, avsInfo):
                self._tags["avs"] = avsInfo
                self._order.append("avs")

        def setCustInfo (self, custInfo):
                self._tags["CustInfo"] = custInfo
                self._order.append("CustInfo")

class RecurUpdate(mpgTransaction):
        def __init__(self, order_id):
                self._Request = "recur_update"
                self._tags = {"order_id" : order_id } 
                self._order = ["order_id"]

        def setCustId (self, cust_id):
                self._tags["cust_id"] = cust_id
                self._order.append("cust_id")

        def setRecurAmount (self, recur_amount):
                self._tags["recur_amount"] = recur_amount
                self._order.append("recur_amount")

        def setPan (self, pan):
                self._tags["pan"] = pan
                self._order.append("pan")

        def setExpDate (self, expdate):
                self._tags["expdate"] = expdate
                self._order.append("expdate")

        def setAddNumRecurs (self, add_num_recurs):
                self._tags["add_num_recurs"] = add_num_recurs
                self._order.append("add_num_recurs")

        def setTotalNumRecurs (self, total_num_recurs):
                self._tags["total_num_recurs"] = total_num_recurs
                self._order.append("total_num_recurs")

        def setHold (self, hold):
                self._tags["hold"] = hold
                self._order.append("hold")
                
        def setTerminate (self, terminate):
                self._tags["terminate"] = terminate
                self._order.append("terminate")

class CvdInfo(mpgTransaction):
        def __init__(self, cvd_indicator, cvd_value):
                self._Request = "cvd_info"
                self._tags = {"cvd_indicator" : cvd_indicator, "cvd_value" : cvd_value}
                self._order = ["cvd_indicator", "cvd_value"]

class AvsInfo(mpgTransaction):
        def __init__(self, avs_street_number, avs_street_name, avs_zipcode) :
                self._Request = "avs_info"
                self._tags = {"avs_street_number" : avs_street_number, "avs_street_name" : avs_street_name, "avs_zipcode" : avs_zipcode}
                self._order = ["avs_street_number", "avs_street_name", "avs_zipcode"]

class Recur(mpgTransaction):
        def __init__(self, recur_unit, start_now, start_date, num_recurs, period, recur_amount):
                self._Request = "recur"
                self._tags = {"recur_unit" : recur_unit, "start_now" : start_now, "start_date" : start_date, "num_recurs" : num_recurs, "period" : period, "recur_amount" : recur_amount}
                self._order = ["recur_unit", "start_now", "start_date", "num_recurs", "period", "recur_amount"]
                
                
class CustInfo(mpgTransaction):
        def __init__(self) :
                self._Request = "cust_info"
                self._tags = {"billing" : None, "shipping" : None, "email" : "", "instructions": "", "item" : []}
                self._order = []

        def setBilling(self, billingInfo):
                self._tags["billing"] = billingInfo
                self._order.append("billing")

        def setShipping(self, shippingInfo):
                self._tags["shipping"] = shippingInfo           
                self._order.append("shipping")
                
        def setEmail(self, email):
                self._tags["email"] = email
                self._order.append("email")
                
        def setInstruction(self, instructions):
                self._tags["instructions"] = instructions
                self._order.append("instructions")
        
        def addItem(self, item):
                itm = self._tags["item"]
                itm.append(item)
                self._tags["item"] = itm
                if "item" not in self._order:
                        self._order.append("item")
                
class BillingInfo(mpgTransaction):
        def __init__(self, first_name, last_name, company_name, address, city, province, postal_code, country, phone_number, fax, tax1, tax2, tax3, shipping_cost):
                self._Request = "billing"
                self._tags = {}
                self._tags["first_name"] = first_name
                self._tags["last_name"] = last_name
                self._tags["company_name"] = company_name
                self._tags["address"] = address
                self._tags["city"] = city
                self._tags["province"] = province
                self._tags["postal_code"] = postal_code
                self._tags["country"] = country
                self._tags["phone_number"] = phone_number
                self._tags["fax"] = fax
                self._tags["tax1"] = tax1
                self._tags["tax2"] = tax2
                self._tags["tax3"] = tax3
                self._tags["shipping_cost"] = shipping_cost
                self._order = ["first_name", "last_name", "company_name", "address", "city", "province", "postal_code", "country", "phone_number", "fax", "tax1", "tax2", "tax3", "shipping_cost"]

        def setFirstName (self, first_name):
                self._tags["first_name"] = first_name

        def setLastName (self, last_name):
                self._tags["last_name"] = last_name

        def setCompanyName (self, company_name):
                self._tags["company_name"] = company_name

        def setAddress (self, address):
                self._tags["address"] = address

        def setCity (self, city):
                self._tags["city"] = city

        def setProvince (self, province):
                self._tags["province"] = province

        def setPostalCode (self, postal_code):
                self._tags["postal_code"] = postal_code

        def setCountry (self, country):
                self._tags["country"] = country

        def setPhoneNumber (self, phone_number):
                self._tags["phone_number"] = phone_number

        def setFax (self, fax):
                self._tags["fax"] = fax

        def setTax1 (self, tax1):
                self._tags["tax1"] = tax1

        def setTax2 (self, tax2):
                self._tags["tax2"] = tax2

        def setTax3 (self, tax3):
                self._tags["tax3"] = tax3

        def setShippingCost (self, shipping_cost):
                self._tags["shipping_cost"] = shipping_cost

class ShippingInfo(mpgTransaction):
        def __init__(self, first_name, last_name, company_name, address, city, province, postal_code, country, phone_number, fax, tax1, tax2, tax3, shipping_cost):
                self._Request = "shipping"
                self._tags = {}         
                self._tags["first_name"] = first_name
                self._tags["last_name"] = last_name
                self._tags["company_name"] = company_name
                self._tags["address"] = address
                self._tags["city"] = city
                self._tags["province"] = province
                self._tags["postal_code"] = postal_code
                self._tags["country"] = country
                self._tags["phone_number"] = phone_number
                self._tags["fax"] = fax
                self._tags["tax1"] = tax1
                self._tags["tax2"] = tax2
                self._tags["tax3"] = tax3
                self._tags["shipping_cost"] = shipping_cost
                self._order = ["first_name", "last_name", "company_name", "address", "city", "province", "postal_code", "country", "phone_number", "fax", "tax1", "tax2", "tax3", "shipping_cost"]

        def setFirstName (self, first_name):
                self._tags["first_name"] = first_name

        def setLastName (self, last_name):
                self._tags["last_name"] = last_name

        def setCompanyName (self, company_name):
                self._tags["company_name"] = company_name

        def setAddress (self, address):
                self._tags["address"] = address

        def setCity (self, city):
                self._tags["city"] = city

        def setProvince (self, province):
                self._tags["province"] = province

        def setPostalCode (self, postal_code):
                self._tags["postal_code"] = postal_code

        def setCountry (self, country):
                self._tags["country"] = country

        def setPhoneNumber (self, phone_number):
                self._tags["phone_number"] = phone_number

        def setFax (self, fax):
                self._tags["fax"] = fax

        def setTax1 (self, tax1):
                self._tags["tax1"] = tax1

        def setTax2 (self, tax2):
                self._tags["tax2"] = tax2

        def setTax3 (self, tax3):
                self._tags["tax3"] = tax3

        def setShippingCost (self, shipping_cost):
                self._tags["shipping_cost"] = shipping_cost

                
class Item(mpgTransaction):
        def __init__(self, itemName, quantity, product_code, extended_amount) :
                self._Request = "item"
                self._tags = {"name" : itemName, "quantity" : quantity, "product_code" : product_code, "extended_amount" : extended_amount}
                self._order = ["name", "quantity", "product_code", "extended_amount"]

        def setitemName (self, itemName):
                self._tags["itemName"] = itemName

        def setquantity (self, quantity):
                self._tags["quantity"] = quantity

        def setproduct_code (self, product_code):
                self._tags["product_code"] = product_code

        def setextended_amount (self, extended_amount):
                self._tags["extended_amount"] = extended_amount
