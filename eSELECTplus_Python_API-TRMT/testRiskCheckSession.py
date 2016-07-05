import mpgClasses
sq = mpgClasses.SessionQuery("order23", "abc123", "session")
sai = mpgClasses.SessionAccountInfo()

#sai.setPolicy("");
#sai.setDeviceId("4EC40DE5-0770-4fa0-BE53-981C067C598D");
sai.setAccountLogin("13195417-8CA0-46cd-960D-14C158E4DBB2");
sai.setPasswordHash("489c830f10f7c601d30599a0deaf66e64d2aa50a");
sai.setAccountNumber("3E17A905-AC8A-4c8d-A417-3DADA2A55220");
sai.setAccountName("4590FCC0-DF4A-44d9-A57B-AF9DE98B84DD");
sai.setAccountEmail("3CAE72EF-6B69-4a25-93FE-2674735E78E8@test.threatmetrix.com");
#sai.setAccountTelephone("5556667777");
sai.setPan("4242424242424242");
#sai.setAccountAddressStreet1("3300 Bloor St W");
#sai.setAccountAddressStreet2("4th Flr West Tower");
#sai.setAccountAddressCity("Toronto");
#sai.setAccountAddressState("Ontario");
#sai.setAccountAddressCountry("Canada");
#sai.setAccountAddressZip("M8X2X2");
#sai.setShippingAddressStreet1("3300 Bloor St W");
#sai.setShippingAddressStreet2("4th Flr West Tower");
#sai.setShippingAddressCity("Toronto");
#sai.setShippingAddressState("Ontario");
#sai.setShippingAddressCountry("Canada");
#sai.setShippingAddressZip("M8X2X2");
#sai.setLocalAttrib1("a");
#sai.setLocalAttrib2("b");
#sai.setLocalAttrib3("c");
#sai.setLocalAttrib4("d");
#sai.setLocalAttrib5("e");
#sai.setTransactionAmount("1.00");
#sai.setTransactionCurrency("840");

sq.setSessionAccountInfo(sai)
#sq.setEventType("")

rc = mpgClasses.RiskCheck()
rc.setSessionQuery(sq)

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