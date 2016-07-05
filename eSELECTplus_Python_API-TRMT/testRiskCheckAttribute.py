import mpgClasses
aq = mpgClasses.AttributeQuery("order24", "session")
aai = mpgClasses.AttributeAccountInfo()

aai.setDeviceId("");
aai.setAccountLogin("13195417-8CA0-46cd-960D-14C158E4DBB2");
aai.setPasswordHash("489c830f10f7c601d30599a0deaf66e64d2aa50a");
aai.setAccountNumber("3E17A905-AC8A-4c8d-A417-3DADA2A55220");
aai.setAccountName("4590FCC0-DF4A-44d9-A57B-AF9DE98B84DD");
aai.setAccountEmail("3CAE72EF-6B69-4a25-93FE-2674735E78E8@test.threatmetrix.com");
#aai.setCCNumberHash("4242424242424242");
#aai.setIPAddress("192.168.0.1");
#aai.setIPForwarded("192.168.1.0");
aai.setAccountAddressStreet1("3300 Bloor St W");
aai.setAccountAddressStreet2("4th Flr West Tower");
aai.setAccountAddressCity("Toronto");
aai.setAccountAddressState("Ontario");
aai.setAccountAddressCountry("Canada");
aai.setAccountAddressZip("M8X2X2");
aai.setShippingAddressStreet1("3300 Bloor St W");
aai.setShippingAddressStreet2("4th Flr West Tower");
aai.setShippingAddressCity("Toronto");
aai.setShippingAddressState("Ontario");
aai.setShippingAddressCountry("Canada");
aai.setShippingAddressZip("M8X2X2");

aq.setAttributeAccountInfo(aai)
#aq.setPolicyId("")

rc = mpgClasses.RiskCheck()
rc.setAttributeQuery(aq)

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
	
#Print rules thrown
for ruleName in ruleNames:
	print ("\nRuleName = " + ruleName)
	print ("RuleCode = " + resp.getRuleCode(ruleName))
	print ("RuleMessageEn = " + resp.getRuleMessageEn(ruleName))
	print ("RuleMessageFr = " + resp.getRuleMessageFr(ruleName))