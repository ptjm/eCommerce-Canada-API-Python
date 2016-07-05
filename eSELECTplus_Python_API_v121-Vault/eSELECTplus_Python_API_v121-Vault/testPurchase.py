import time
import mpgClasses

host = "esqa.moneris.com"
store_id = "store5"
api_token = "yesguy"

order_id = "test_python-" + str(time.time())
amount = "1.00"
pan = "4242424242424242"
expiry_date = "1611"
crypt = "7"

p = mpgClasses.Purchase (order_id, amount, pan, expiry_date, crypt)
p.setCustId ("cust 1")
p.setDynamicDescriptor("INVOICE 001")

req = mpgClasses.mpgHttpsPost(host, store_id , api_token, p)
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

