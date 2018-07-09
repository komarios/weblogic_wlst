# Set all variables from values in properties file.
userConfigFilePath='/weblogic/bin/WLSTSecureConfigFile'
userKeyFilePath='/weblogic/bin/WLSTSecureKeyFile'
adminURL='t3s://...:7001'

dsTargetName ='managed_server1'
dsTargetType ='Cluster'

dsName           = ['myDS', 'myDS_XA']
dsJNDIName       = ['jdbc/myDS', 'jdbc/myDS_XA']
dsURL            =  'jdbc:oracle:thin:@//myoracledb:1521/mysid'
dsUsername       =  'muuser'
dsPassword       =  'mypass'
dsDriver         = ['oracle.jdbc.OracleDriver', 'oracle.jdbc.xa.client.OracleXADataSource']
dsGlobalTransProt= ['None', 'TwoPhaseCommit']
