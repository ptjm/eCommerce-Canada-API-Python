import time
import mpgClasses

host = "esqa.moneris.com"
store_id = "moneris"
api_token = "hurgle"

temp_data_key = "ot-322w9TtUAeGWLYjqup8PlAa3G"
expdate = "1711"
crypt = "7"

resAddToken = mpgClasses.ResAddToken (temp_data_key, expdate, crypt)
resAddToken.setCustId ("cust 1")
avs = mpgClasses.AvsInfo("123", "Main St", "a1a2b2")

email = "email@abc.com"
phone = "8889998765"
note = "Charge them weekly"

resAddToken.setPhone(phone)
resAddToken.setEmail(email)
resAddToken.setNote(note)
resAddToken.setAvsInfo(avs)

req = mpgClasses.mpgHttpsPost(host, store_id, api_token, resAddToken)
req.postRequest()
resp = req.getResponse()
print ("ReceiptId: " + resp.getReceiptId()) 
print ("ReferenceNum: " + resp.getReferenceNum()) 
print ("ResponseCode: " + resp.getResponseCode()) 
print ("ISO: " + resp.getISO()) 
print ("AuthCode: " + resp.getAuthCode()) 
print ("TransTime: " + resp.getTransTime()) 
print ("TransDate: " + resp.getTransDate()) 
print ("TransType: " + resp.getTransType()) 
print ("Complete: " + resp.getComplete()) 
print ("Message: " + resp.getMessage()) 
print ("TransAmount: " + resp.getTransAmount()) 
print ("CardType: " + resp.getCardType()) 
print ("TransID: " + resp.getTransID()) 
print ("TimedOut: " + resp.getTimedOut()) 

#Resolver Data
print ("DataKey: " + resp.getDataKey()) 
print ("PaymentType: " + resp.getPaymentType())
print ("ResSuccess: " + resp.getResSuccess()) 
print ("ResDataMaskedPan: " + resp.getResDataMaskedPan()) 
print ("ResDataCustId " + resp.getResDataCustId())
print ("ResDataPhone " + resp.getResDataPhone())
print ("ResDataEmail " + resp.getResDataEmail())
print ("ResDataNote " + resp.getResDataNote())
print ("ResDataCryptType " + resp.getResDataCryptType())
print ("ResDataExpDate " + resp.getResDataExpDate())
print ("ResDataAvsStreetName " + resp.getResDataAvsStreetName())
print ("ResDataAvsStreetNumber " + resp.getResDataAvsStreetNumber())
print ("ResDataAvsZipcode " + resp.getResDataAvsZipcode())
