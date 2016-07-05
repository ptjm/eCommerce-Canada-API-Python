import time
import mpgClasses

host = "esqa.moneris.com"
store_id = "store5"
api_token = "yesguy"

resDelete = mpgClasses.ResDelete ("jDVd8Y2cjrrNP2K99yVQUTXn2")

req = mpgClasses.mpgHttpsPost(host, store_id, api_token, resDelete)
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
print ("ResDataPan: " + resp.getResDataPan()) 
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
