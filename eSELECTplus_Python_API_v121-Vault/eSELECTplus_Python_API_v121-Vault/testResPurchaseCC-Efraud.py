import time
import mpgClasses

host = "esqa.moneris.com"
store_id = "store5"
api_token = "yesguy"

data_key = "I697jeffVXSW2xJp8ixCrIG84"
order_id = "test_python-" + str(time.time())
amount = "10.31"
crypt = "7"

p = mpgClasses.ResPurchaseCC (data_key, order_id, amount, crypt)
p.setCustId ("cust 1")

cvd_indicator = "1"
cvd_value = "123"
cvd = mpgClasses.CvdInfo(cvd_indicator, cvd_value)

avs_street_number = "123"
avs_street_name = "Eglinton Ave E BNS Transit 91538"
avs_zipcode = "a1a2b2"

avs = mpgClasses.AvsInfo(avs_street_number, avs_street_name, avs_zipcode)

p.setCvdInfo(cvd)
p.setAvsInfo(avs)

req = mpgClasses.mpgHttpsPost(host, store_id, api_token, p)
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
print ("AvsResultCode: " + resp.getAvsResultCode())
print ("CvdResultCode: " + resp.getCvdResultCode())
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

