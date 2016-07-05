import time
import mpgClasses

host = "esqa.moneris.com"
store_id = "store5"
api_token = "yesguy"

data_key = "I697jeffVXSW2xJp8ixCrIG84"
amount = "1.00"
xid = "pythonxid-"+`int(time.time())`
MD = "session=abc"
merchantUrl = "www.test.com"
accept = "text/html"
userAgent = "Browser"

txn = mpgClasses.ResMpiTxn (data_key, amount, xid,MD,merchantUrl,accept,userAgent)

req = mpgClasses.mpgHttpsPost("esqa.moneris.com", "store5", "yesguy", txn)
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
print ("MpiType: "+resp.getMpiType())
print ("MpiSuccess: "+resp.getMpiSuccess())
print ("MpiMessage: "+resp.getMpiMessage())
print ("MpiPaReq: "+resp.getMpiPaReq())
print ("MpiTermUrl: "+resp.getMpiTermUrl())
print ("MpiMD: "+resp.getMpiMD())
print ("MpiACSUrl: "+resp.getMpiACSUrl())
print ("MpiCavv: "+resp.getMpiCavv())
print ("MpiPAResVerified: "+resp.getMpiPAResVerified())
