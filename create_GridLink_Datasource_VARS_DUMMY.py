userConfigFilePath='/weblogic/bin/WLSTSecureConfigFile'
userKeyFilePath='/weblogic/bin/WLSTSecureKeyFile'
adminURL='t3s://...:7001'

dsTargetCluster='my_cluster'

dsURL='jdbc:oracle:thin:@...'
dsUsername='...'
dsPassword='...'
dsFanEnabled=1
dsNodeList='DB1:6200,DB2:6200'
###dsKeepXaConnTillTxComplete=1
dsTestQuery='SQL SELECT 1 FROM DUAL'
dsInitCapacity=30
dsMaxCapacity=130
dsTestFrequencySeconds=60
dsInactiveConnectionTimeout=30
dsShrinkFrequencySeconds=0
dsTestConnectionsOnReserve=1
dsConnectionReserveTimeout=30
dsStatementCacheType='LRU'
dsStatementCacheSize=200
dsStreamChunkSize=4096

dsName=['testDS']
dsJNDIName=['jdbc/testDS']
dsDriver=['oracle.jdbc.OracleDriver']
dsGlobalTransProt=['None']
