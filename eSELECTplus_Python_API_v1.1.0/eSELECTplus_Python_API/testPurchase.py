import time
import time
import mpgClasses

p = mpgClasses.Purchase ("test_python-" + str(time.time()), "1.00", "4242424242424242", "0909", "7")
p.setCustId ("cust 1")
cvd = mpgClasses.CvdInfo("1", "123")
avs = mpgClasses.AvsInfo("123", "Main St", "a1a2b2")

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

p.setCvdInfo(cvd)
p.setAvsInfo(avs)

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
print ("BankTotals: " + resp.getBankTotals()) 
print ("Ticket: " + resp.getTicket()) 
#print ("AvsResultCode: " + resp.getAvsResultCode())
#print ("CvdResultCode: " + resp.getCvdResultCode())

