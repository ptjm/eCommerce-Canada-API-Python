import time
import mpgClasses

p = mpgClasses.Purchase ("test_python-" + str(time.time()), "10.10", "4242424242424242", "0909", "7")
p.setCustId ("cust 1")
cvd = mpgClasses.CvdInfo("1", "123")
avs = mpgClasses.AvsInfo("1234", "Eglinton Ave E BNS Transit 91538", "a1a2b2")

p.setCvdInfo(cvd)
p.setAvsInfo(avs)

req = mpgClasses.mpgHttpsPost("esqa.moneris.com", "store5", "yesguy", p)
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

