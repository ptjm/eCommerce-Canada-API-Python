import mpgClasses
ot = mpgClasses.OpenTotals("66005372")
req = mpgClasses.mpgHttpsPost("esqa.moneris.com", "store5", "yesguy", ot)
req.postRequest()
resp = req.getResponse()
ecrs = resp.getECRs()
for termid in ecrs.keys():
	print ("ecr is: "+ termid )
	cardTypes = resp.getCardTypes(termid)
	for card in cardTypes:
		print ("Card Type is : " + card)
		print ("\tPurchase Count: " + resp.getPurchaseCount(termid, card))
		print ("\tPurchase Amount: " + resp.getPurchaseAmount(termid, card))
		print ("\tRefund Count: " + resp.getRefundCount(termid, card))
		print ("\tRefund Amount: " + resp.getRefundAmount(termid, card))
		print ("\tCorrection Count: " + resp.getCorrectionCount(termid, card))
		print ("\tCorrection Amount: " + resp.getCorrectionAmount(termid, card))	
		print ("\n\n")
	print ("------------------------------\n\n")
