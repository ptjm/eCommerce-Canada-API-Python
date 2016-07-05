import time
import mpgClasses

p = mpgClasses.Purchase ("test_python-" + str(time.time()), "1.00", "4242424242424242", "0909", "7")
p.setCustId ("cust 1")

recur = mpgClasses.Recur("month", "true", "2010/10/10", "12", "1", "30.00")
p.setRecur(recur)

req = mpgClasses.mpgHttpsPost("esqa.moneris.com", "moneris", "hurgle", p)
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
print ("RecurSuccess: " + resp.getRecurSuccess())

