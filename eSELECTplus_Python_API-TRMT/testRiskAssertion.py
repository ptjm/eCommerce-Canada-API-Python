import mpgClasses
#orig_order_id, activities_description, impact_description, confidence_description
a = mpgClasses.Assert("order24", "charge_back", "medium", "suspicious")

rc = mpgClasses.RiskCheck()
rc.setAssert(a)

req = mpgClasses.mpgHttpsPost("esqa.moneris.com", "moneris", "hurgle", rc)

req.postRequest()
resp = req.getResponse()

print ("ResponseCode: " + resp.getResponseCode())
print ("Message: " + resp.getMessage())

results = resp.getResults()
ruleNames = resp.getRuleNames()
#Print results 
for value in results:
	print (value + " = " + results[value])
