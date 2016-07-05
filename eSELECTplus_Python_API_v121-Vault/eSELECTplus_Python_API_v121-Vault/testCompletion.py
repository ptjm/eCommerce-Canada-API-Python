import mpgClasses

host = "esqa.moneris.com"
store_id = "store5"
api_token = "yesguy"

order_id = "test_python-1411094669.6"
comp_amount = "0.10"
txn_number = "409525-0_9"
crypt = "7"


p = mpgClasses.Completion(order_id, comp_amount, txn_number, crypt)

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


