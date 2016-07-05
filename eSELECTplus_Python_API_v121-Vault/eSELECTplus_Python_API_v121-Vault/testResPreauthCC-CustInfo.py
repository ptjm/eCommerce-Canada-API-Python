import time
import mpgClasses

p = mpgClasses.ResPreauthCC ("pqL7LvBDxWzotwRYirH1lAd64", "test_python-" + str(time.time()), "1.00", "7")
p.setCustId ("cust 1")

cust = mpgClasses.CustInfo()
billing = mpgClasses.BillingInfo("first_name", "last_name", "company_name", "address", "city", "province", "postal_code", "country", "phone_number", "fax", "tax1", "tax2", "tax3", "shipping_cost")
shipping = mpgClasses.ShippingInfo("first_name", "last_name", "company_name", "address", "city", "province", "postal_code", "country", "phone_number", "fax", "tax1", "tax2", "tax3", "shipping_cost")
email = "email@abc.com"
instruction = "take it slow"
cust.setBilling(billing)
cust.setShipping(shipping)
cust.setEmail(email)
cust.setInstruction(instruction)
cust.addItem(mpgClasses.Item("item 123", "1", "4527182-90123", "5.00"))
cust.addItem(mpgClasses.Item("item 234", "2", "4527182-90234", "4.00"))
cust.addItem(mpgClasses.Item("item 345", "3", "4527182-90345", "3.00"))
p.setCustInfo (cust)

req = mpgClasses.mpgHttpsPost("esqa.moneris.com", "store3", "yesguy", p)
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

