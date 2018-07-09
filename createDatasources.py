#####################################################################################################################
print "Load variables from file: createDatasources_VARS.py"
execfile('create_datasources_VARS.py')
#####################################################################################################################
# Connect to the AdminServer.
connect(adminUsername, adminPassword, adminURL)
edit()
startEdit()
#####################################################################################################################
print "Common Variables for all DataSources :"
print "   dsTargetName="+dsTargetName
print "   dsTargetType="+dsTargetType
print "   dsURL="+dsURL
print "   dsUsername="+dsUsername
print "   dsPassword="+dsPassword
#####################################################################################################################
for i in range(0, len(dsName)):
  print "Creating Data Source :"
  print "   name="+dsName[i]
  print "   jndi="+dsJNDIName[i]
  print "   dsDriver="+dsDriver[i]
  print "   XA="+dsGlobalTransProt[i]
  cd('/')
  cmo.createJDBCSystemResource(dsName[i])
  cd('/JDBCSystemResources/' + dsName[i] + '/JDBCResource/' + dsName[i])
  cmo.setName(dsName[i])
  cd('/JDBCSystemResources/' + dsName[i] + '/JDBCResource/' + dsName[i] + '/JDBCDataSourceParams/' + dsName[i])
  set('JNDINames',jarray.array([String(dsJNDIName[i])], String))
  cd('/JDBCSystemResources/ASYNC/JDBCResource/ASYNC')
  cmo.setDatasourceType('GENERIC')
  cd('/JDBCSystemResources/' + dsName[i] + '/JDBCResource/' + dsName[i] + '/JDBCDriverParams/' + dsName[i])
  cmo.setUrl(dsURL)
  cmo.setDriverName(dsDriver[i])
  set('Password', dsPassword)
  cd('/JDBCSystemResources/' + dsName[i] + '/JDBCResource/' + dsName[i] + '/JDBCConnectionPoolParams/' + dsName[i])
  cmo.setTestTableName('SQL SELECT 1 FROM DUAL\r\n\r\n')
  cd('/JDBCSystemResources/' + dsName[i] + '/JDBCResource/' + dsName[i] + '/JDBCDriverParams/' + dsName[i] + '/Properties/' + dsName[i])
  cmo.createProperty('user')
  cd('/JDBCSystemResources/' + dsName[i] + '/JDBCResource/' + dsName[i] + '/JDBCDriverParams/' + dsName[i] + '/Properties/' + dsName[i] + '/Properties/user')
  cmo.setValue(dsUsername)
  cd('/JDBCSystemResources/' + dsName[i] + '/JDBCResource/' + dsName[i] + '/JDBCDataSourceParams/' + dsName[i] + '')
  cmo.setGlobalTransactionsProtocol(dsGlobalTransProt[i])
  cd('/SystemResources/' + dsName[i])
  set('Targets',jarray.array([ObjectName('com.bea:Name=' + dsTargetName + ',Type=' + dsTargetType)], ObjectName))
#####################################################################################################################
save()
activate()
disconnect()
exit()
#####################################################################################################################
