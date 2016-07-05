import time
import mpgClasses

host = "esqa.moneris.com"
store_id = "store5"
api_token = "yesguy"

resLookupFull = mpgClasses.ResGetExpiring()

req = mpgClasses.mpgHttpsPost(host, store_id , api_token, resLookupFull)
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
print ("DataKey: " + resp.getDataKey()) 
print ("PaymentType: " + resp.getPaymentType())
print ("ResSuccess: " + resp.getResSuccess()) 
print ("ResDataPan: " + resp.getResDataPan()) 

#Resolver Data
for key in resp.getDataKeys():
	print ("DataKey:"+key)
	print ("\tResDataMaskedPan: " + resp.getResDataMaskedPan(key)) 
	print ("\tResDataCustId " + resp.getResDataCustId(key))
	print ("\tResDataPhone " + resp.getResDataPhone(key))
	print ("\tResDataEmail " + resp.getResDataEmail(key))
	print ("\tResDataNote " + resp.getResDataNote(key))
	print ("\tResDataCryptType " + resp.getResDataCryptType(key))
	print ("\tResDataExpDate " + resp.getResDataExpDate(key))
	print ("\tResDataAvsStreetName " + resp.getResDataAvsStreetName(key))
	print ("\tResDataAvsStreetNumber " + resp.getResDataAvsStreetNumber(key))
	print ("\tResDataAvsZipcode " + resp.getResDataAvsZipcode(key))
	print ("\n")
