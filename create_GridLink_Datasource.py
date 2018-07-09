#####################################################################################################################
print 'Load variables from file: create_GridLink_Datasource_VARS.py'
execfile('create_GridLink_Datasource_VARS.py')

connect( userConfigFile='/weblogic/bin/WLSTSecureConfigFile', userKeyFile='/weblogic/bin/WLSTSecureKeyFile', url='t3s://...:7001' )

edit()
startEdit()
#####################################################################################################################
for i in range(0, len(dsName)):
  print '========================================='
  print '=   Creating GridLink DataSource  ....  ='
  print '========================================='
  print 'DataSource Name    : ',dsName[i]
  print 'dsJNDIName         : ',dsJNDIName[i]
  print 'dsTargetCluster    : ',dsTargetCluster
  print 'dsUsername         : ',dsUsername
  print 'dsPassword         : ',dsPassword
  print 'dsInitCapacity     : ',dsInitCapacity
  print 'dsMaxCapacity      : ',dsMaxCapacity
  print 'dsTestQuery        : ',dsTestQuery
  print 'dsTestFrequencySeconds      : ',dsTestFrequencySeconds
  print 'dsInactiveConnectionTimeout : ',dsInactiveConnectionTimeout
  print 'dsShrinkFrequencySeconds    : ',dsShrinkFrequencySeconds
  print 'dsTestConnectionsOnReserve  : ',dsTestConnectionsOnReserve
  print 'dsConnectionReserveTimeout  : ',dsConnectionReserveTimeout
  print 'dsStatementCacheType        : ',dsStatementCacheType
  print 'dsStatementCacheSize        : ',dsStatementCacheSize
  print 'dsDriver           : ',dsDriver[i]
  print 'dsFanEnabled       : ',dsFanEnabled
  print 'dsNodeList         : ',dsNodeList
  print 'dsGlobalTransProt  : ',dsGlobalTransProt[i]
  print 'dsURL              : ',dsURL
###  print 'dsKeepXaConnTillTxComplete : ',dsKeepXaConnTillTxComplete

  cd( '/' )
  jdbcSystemResource = create( dsName[i], 'JDBCSystemResource' )
  jdbcResource       = jdbcSystemResource.getJDBCResource()
  jdbcResource.setName( dsName[i] )

  dataSourceParams = jdbcResource.getJDBCDataSourceParams()
  dataSourceParams.setJNDINames( [dsJNDIName[i]] )
  dataSourceParams.setGlobalTransactionsProtocol( dsGlobalTransProt[i] )
  dataSourceParams.setStreamChunkSize( int(dsStreamChunkSize) )

  driverParams     = jdbcResource.getJDBCDriverParams()
  driverParams.setPassword( dsPassword )
  driverParams.setUrl( dsURL )
  driverParams.setDriverName( dsDriver[i] )
  driverProperties = driverParams.getProperties()
  userBean         = driverProperties.createProperty( 'user' )
  userBean.setValue( dsUsername )

  oracleParams     = jdbcResource.getJDBCOracleParams()
  oracleParams.setFanEnabled(  bool(dsFanEnabled) )
  oracleParams.setOnsNodeList( dsNodeList )
 
  connPoolParams   = jdbcResource.getJDBCConnectionPoolParams()
  connPoolParams.setInitialCapacity( int(dsInitCapacity) )
  connPoolParams.setMaxCapacity( int(dsMaxCapacity) )
  connPoolParams.setTestTableName( dsTestQuery )
  connPoolParams.setTestFrequencySeconds( int(dsTestFrequencySeconds) ) 
  connPoolParams.setInactiveConnectionTimeoutSeconds( int(dsInactiveConnectionTimeout) ) 
  connPoolParams.setShrinkFrequencySeconds( int(dsShrinkFrequencySeconds) ) 
  connPoolParams.setTestConnectionsOnReserve( bool(dsTestConnectionsOnReserve) ) 
  connPoolParams.setConnectionReserveTimeoutSeconds( int(dsConnectionReserveTimeout) )
  connPoolParams.setStatementCacheType( dsStatementCacheType ) 
  connPoolParams.setStatementCacheSize( int(dsStatementCacheSize) ) 

  ###xaParams = jdbcResource.getJDBCXAParams()
  ###xaParams.setKeepXaConnTillTxComplete( int(dsKeepXaConnTillTxComplete) )

  jdbcSystemResource.addTarget( getMBean( 'Clusters/'+dsTargetCluster ) )

  print 'DataSource: ',dsName[i],', has been created Successfully !!!'
  print '========================================='
#####################################################################################################################
save()
activate()
disconnect()
#####################################################################################################################
