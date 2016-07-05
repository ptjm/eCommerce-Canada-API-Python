import time
import mpgClasses

host = "esqa.moneris.com"
store_id = "store5"
api_token = "yesguy"

data_key = "I697jeffVXSW2xJp8ixCrIG84"
order_id = "test_python-" + str(time.time())
amount = "1.00"
crypt = "7"

p = mpgClasses.ResPurchaseCC (data_key, order_id, amount, crypt)
p.setCustId ("cust 1")

recur_unit = "month" #valid values are (day,week,month,eom)
start_now = "true"
start_date = "2015/12/01"
num_recurs = "12"
period = "1"
recur_amount = "30.00"

recur = mpgClasses.Recur(recur_unit, start_now, start_date, num_recurs, period, recur_amount)
p.setRecur(recur)

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
print ("RecurSuccess: " + resp.getRecurSuccess())
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

