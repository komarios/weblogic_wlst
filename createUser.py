
execfile('createUser_VARS.py')

connect( userConfigFile=userConfigFilePath, userKeyFile=userKeyFilePath, url=adminUrl )

securityConfig= cmo.getSecurityConfiguration().getDefaultRealm().lookupAuthenticationProvider( authProvider )
for i in range(0, len(newUserNames)):
  print "Create User "
  print "   Name: "+ newUserNames[i]
  print "   Pass: "+ newUserNames[i] + userPassSuffix
  print "   Desc: "+ newUserNames[i]
  securityConfig.createUser( newUserNames[i], newUserNames[i] + userPassSuffix, newUserNames[i] ) 
  print " Done"
  print "Add User "+ newUserNames[i] +" to group "+ userGroup
  securityConfig.addMemberToGroup( userGroup, newUserNames[i] ) 
  print " Done"
  if securityConfig.isMember( userGroup, newUserNames[i], true ) == 0:
    print newUserNames[i] +" is NOT a member of "+ userGroup
  else:
    print newUserNames[i] +" IS a member of "+ userGroup
exit()
