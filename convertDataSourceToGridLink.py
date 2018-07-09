def edit_startEdit_print( msg ):
  edit()
  startEdit()
  print msg

def save_activate_print( msg ):
  save()
  activate()
  print msg

def untargetDS( jdbcSystemRsrc ):
  edit_startEdit_print( 'UN-Target DataSource : ' + jdbcSystemRsrc.getName() )
  cd('/JDBCSystemResources/' +  jdbcSystemRsrc.getName() )
  trgts=get('Targets')
  set('Targets', jarray.array([], ObjectName))
  return trgts

def enableActiveGridLink( jdbcSystemRsrc, jdbsUrl, jdbcRcuUrl, onsNodeList ):
  edit_startEdit_print( 'Set RAC url for DataSource ' + jdbcSystemRsrc.getName() + ':\n' + url )
  dsName = jdbcSystemRsrc.getName()
  cd( '/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCDriverParams/' + dsName )
  oldUrl = get( 'Url' )
  # If the url does not connect to the RCU 
  if ( oldUrl.find('rcu') < 0 and oldUrl.find('RCU') < 0 ):
    set( 'Url', jdbsUrl)
  else:
    set( 'Url', jdbcRcuUrl)
  cd( '/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName + '/JDBCOracleParams/' + dsName )
  set( 'FanEnabled',  true)
  set( 'OnsNodeList', onsNodeList)
  cd( '/JDBCSystemResources/' + dsName + '/JDBCResource/' + dsName )
  set( 'DatasourceType', 'AGL')
  save_activate_print( 'DONE' )

def retargetDS( jdbcSystemRsrc, trgts ):
  edit_startEdit_print( 'RE-Target DataSource : ' + jdbcSystemRsrc.getName() )
  cd("/JDBCSystemResources/" + jdbcSystemRsrc.getName() )
  set("Targets", trgts)
  save_activate_print( 'DONE' )
#=======================================================================================
print 'Load variables from file: convertDataSourceToGridLink_VARS.py'
execfile('convertDataSourceToGridLink_VARS.py')
connect(userConfigFile='/weblogic/bin/WLSTSecureConfigFile',userKeyFile='/weblogic/bin/WLSTSecureKeyFile',url=adminUrl)
for jdbcSystemResource in cmo.getJDBCSystemResources():
  targets = untargetDS( jdbcSystemResource )
  enableActiveGridLink( jdbcSystemResource, url, rcuUrl, ons_node_list )
  retargetDS( jdbcSystemResource, targets )
print 'Finished'
disconnect()
exit()
