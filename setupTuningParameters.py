print 'Load variables from file: setupTuningParameters_VARS.py'
execfile('setupTuningParameters_VARS.py')
connect( userConfigFile=userConfigFilePath, userKeyFile=userKeyFilePath, url=adminUrl )
edit()
startEdit()

domainName = cmo.getName()
print 'Setup Domain Level configuration : ' + domainName
cd( '/JTA/' + domainName )
set( 'TimeoutSeconds', int(jtaTimeoutSeconds) )
cd( '/WebAppContainer/' + domainName )
set( 'JSPCompilerBackwardsCompatible', bool(JSPCompilerBackwardsCompatible) )
set( 'ShowArchivedRealPathEnabled',    bool(showArchivedRealPathEnabled)    ) 
print ' DONE'

print 'Setup Managed Server Level configuration'
cd( '/' )
for server in cmo.getServers():
  if ( server.getName() != 'AdminServer' ):
    print 'Managed Server :' + server.getName()
    cd( '/Servers/' + server.getName() )
    set( 'StuckThreadMaxTime', int(stuckThreadMaxTime) )
    cd( '/Servers/' + server.getName() + '/Log/' + server.getName() )
    set( 'LoggerSeverity',  minimumSeverityToLog )
    set( 'LogFileSeverity', logFileSeverityLevel )
    set( 'StdoutSeverity',  standardOutSeverityLevel )
    set( 'DomainLogBroadcastSeverity', domainLogBroadcasterSeverityLevel )
    cd( '/Servers/' + server.getName() + '/WebServer/' + server.getName() + '/WebServerLog/' + server.getName() )
    set( 'LoggingEnabled', bool(httpAccessLogFileEnabled) )
    if ( bool(obdxSpecific) ): 
      print 'Setup OBDX Specific configuration'
      cd( '/Servers/' + server.getName() + '/Log/' + server.getName() )
      set( 'NumberOfFilesLimited', bool( limitNumberOfRetainedFiles ) )
      set( 'FileCount', int(filesToRetain) )
      cd( '/Servers/' + server.getName() + '/WebServer/' + server.getName() + '/WebServerLog/' + server.getName() )
      set( 'ELFFields', extendedLoggingFormatFields )
      cd( '/Servers/' + server.getName() + '/ServerStart/' + server.getName() )
      javaArguments = get('Arguments')
      if ( javaArguments.find(optimizeSecureRandomNumberGeneration) < 0 ):
        set( 'Arguments', javaArguments + ' ' + optimizeSecureRandomNumberGeneration )
    print ' DONE'

print 'Setup DataSource Level configuration'
cd( '/' )
for datasource in cmo.getJDBCSystemResources():
  dsName = datasource.getName()
  print dsName
  cd( '/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDataSourceParams/' + dsName )
  set( 'StreamChunkSize', int(dsStreamChunkSize) )
  cd( '/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCConnectionPoolParams/' + dsName )
  set( 'InitialCapacity', int(dsInitCapacity) )
  set( 'MaxCapacity',     int(dsMaxCapacity)  )
  set( 'MinCapacity',     int(dsMinCapacity)  )
  set( 'TestTableName',       dsTestQuery     )
  if ( dsInitSQL > 0 ):
      set( 'InitSql', 'SQL begin pr_datasource(\''+ dsName +'\'); end;' )
  set( 'TestFrequencySeconds',             int(dsTestFrequencySeconds)      ) 
  set( 'InactiveConnectionTimeoutSeconds', int(dsInactiveConnectionTimeout) ) 
  set( 'ShrinkFrequencySeconds',           int(dsShrinkFrequencySeconds)    ) 
  set( 'TestConnectionsOnReserve',        bool(dsTestConnectionsOnReserve)  ) 
  set( 'ConnectionReserveTimeoutSeconds',  int(dsConnectionReserveTimeout)  )
  set( 'StatementCacheType', dsStatementCacheType ) 
  set( 'StatementCacheSize', int(dsStatementCacheSize) )
  print ' DONE'

cd( '/' )
if ( bool(obdxSpecific) ): 
  ldapProvider = (cmo.getSecurityConfiguration().getDefaultRealm().getAuthenticationProviders())[0]
  cd( '/SecurityConfiguration/' + domainName + '/Realms/myrealm/AuthenticationProviders/' + ldapProvider.getName() )
  print 'Setup Security Realm Level configuration for OBDX on ADAuthenticator ' + ldapProvider.getName()
  set( 'ConnectionPoolSize',   int( ldapProviderConnectionPoolSize ) )
  set( 'ConnectTimeout',       int( ldapProviderConnectTimeout ) ) 
  set( 'ConnectionRetryLimit', int( ldapProviderConnectionRetryLimit ) ) 
  print ' DONE'

print 'Finished'
save()
activate()
disconnect()
exit()
