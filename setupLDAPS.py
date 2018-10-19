def edit_startEdit_print( msg ):
  edit()
  startEdit()
  print msg

def save_activate_print( msg ):
  save()
  activate()
  print msg

def deleteTrustServiceIdentityAsserter( domainNM ):
  edit_startEdit_print( 'Delete Trust Service Identity Asserter' )
  cd('/SecurityConfiguration/'+ domainNM +'/Realms/myrealm')
  trustServiceIdentityAsserter = cmo.lookupAuthenticationProvider('Trust Service Identity Asserter')
  cmo.destroyAuthenticationProvider( trustServiceIdentityAsserter )
  save_activate_print( '  DONE' )

def createADAuthProvider( domainNM, ldapName ):
  edit_startEdit_print( 'Create Active Directory Authentication Provider : ' + ldapName )
  cd('/SecurityConfiguration/'+ domainNM +'/DefaultRealm/myrealm')
  cmo.createAuthenticationProvider( ldapName, 'weblogic.security.providers.authentication.ActiveDirectoryAuthenticator')
  cd('/SecurityConfiguration/'+ domainNM +'/DefaultRealm/myrealm/AuthenticationProviders/'+ ldapName)
  set('ControlFlag','SUFFICIENT')
  cd('/SecurityConfiguration/'+ domainNM +'/DefaultRealm/myrealm/AuthenticationProviders/DefaultAuthenticator/')
  set('ControlFlag','SUFFICIENT')
  save_activate_print( '  DONE' )

def configureConnectionADAuthProvider( domainNM, ldapName, host, principal, credential ):
  edit_startEdit_print( 'Configure Connection for Active Directory Authentication Provider : ' + ldapName )
  cd('/SecurityConfiguration/'+ domainNM +'/DefaultRealm/myrealm/AuthenticationProviders/'+ ldapName)
  set('Host', host)
  set('Port', int(636))
  set('SSLEnabled', true)
  set('Principal',  principal)
  set('Credential', credential)  
  save_activate_print( '  DONE' )

def configureAttributesADAuthProvider( domainNM, ldapName, userDN, groupDN, poolSize, timeout, cacheSize, cacheTTL ):
  edit_startEdit_print( 'Configure Attributes for Active Directory Authentication Provider : ' + ldapName )
  cd('/SecurityConfiguration/'+ domainNM +'/DefaultRealm/myrealm/AuthenticationProviders/'+ ldapName)
  set('UserBaseDN',  userDN )
  set('GroupBaseDN', groupDN)
  set('UseRetrievedUserNameAsPrincipal', true)
  set('ConnectionPoolSize', poolSize)
  set('ConnectTimeout',     timeout )
  set('FollowReferrals',    false   )
  set('CacheSize', cacheSize)
  set('CacheTTL',  cacheTTL )
  save_activate_print( '  DONE' )

def reorderAuthProviders( domainNM, ldapName ):
  edit_startEdit_print( 'RE-Order Authentication Providers' )
  my1stProvider = ldapName
  my2ndProvider = 'DefaultAuthenticator'
  my3rdProvider = 'DefaultIdentityAsserter'
  prvd1 = getMBean('/SecurityConfiguration/' + domainNM + '/Realms/myrealm/AuthenticationProviders/' + my1stProvider)
  prvd2 = getMBean('/SecurityConfiguration/' + domainNM + '/Realms/myrealm/AuthenticationProviders/' + my2ndProvider)
  prvd3 = getMBean('/SecurityConfiguration/' + domainNM + '/Realms/myrealm/AuthenticationProviders/' + my3rdProvider)
  realm = getMBean('/SecurityConfiguration/' + domainNM + '/Realms/myrealm/')
  realm.setAuthenticationProviders(jarray.array([prvd1, prvd2, prvd3], weblogic.management.security.authentication.AuthenticationProviderMBean))
  save_activate_print( '  DONE' )

print 'Load variables from file: setupLDAPS_VARS.py'
execfile('setupLDAPS_VARS.py')
connect( userConfigFile=userConfigFilePath, userKeyFile=userKeyFilePath, url=adminUrl )
domainName = cmo.getName()
deleteTrustServiceIdentityAsserter( domainName )
createADAuthProvider( domainName, providerName )
configureConnectionADAuthProvider( domainName, providerName, providerHost, principalUser, principalPass )
configureAttributesADAuthProvider( domainName, providerName, userBaseDN, groupBaseDN, connPoolSize, connTimeout, cacheSize, cacheTTL )
reorderAuthProviders( domainName, providerName )
print 'Finished'

