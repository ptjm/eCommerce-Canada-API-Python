import time
import mpgClasses

p = mpgClasses.CardVerification ("test_python-" + str(time.time()), "4242424242424242", "0909", "7")
p.setCustId ("cust 1")
cvd = mpgClasses.CvdInfo("1", "123")
avs = mpgClasses.AvsInfo("123", "Main St", "a1a2b2")

p.setCvdInfo(cvd)
p.setAvsInfo(avs)

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
print ("AvsResultCode: " + resp.getAvsResultCode())
print ("CvdResultCode: " + resp.getCvdResultCode())

