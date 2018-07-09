import sys

#=======================================================================================
# Define Helper Functions
#=======================================================================================
def stopAllManagedServers():
 for server in cmo.getServerLifeCycleRuntimes():
  if (server.getName() != 'AdminServer' and server.getState() != 'SHUTDOWN' ):
   tasks.append(server.forceShutdown())

def waitManagedServersToStop():
 sys.stdout.write('Waiting for managed servers to shutdown')
 while len(tasks) > 0:
  for task in tasks:
   if task.getStatus()  != 'TASK IN PROGRESS' :
    tasks.remove(task)
  java.lang.Thread.sleep(1000)
  sys.stdout.write('.')
 print('.')

def startAllManagedServers():
 for server in cmo.getServerLifeCycleRuntimes():
  if (server.getName() != 'AdminServer' and server.getState() != 'RUNNING' ):
   tasks.append(server.start())

def waitManagedServersToStart():
 sys.stdout.write('Waiting for managed servers to start')
 while len(tasks) > 0:
  for task in tasks:
   if task.getStatus()  != 'TASK IN PROGRESS' :
    tasks.remove(task)
  java.lang.Thread.sleep(1000)
  sys.stdout.write('.')
 print('.')

def myPrintln( my_msg ):
  sys.stdout.write( '### '+my_msg+'\n')

#=======================================================================================
# Load Variables from redeploy_app_VARS.py
#=======================================================================================
execfile( 'redeployApp_VARS.py' )

#=======================================================================================
# Connect
#=======================================================================================
myPrintln( 'Connecting...' )
connect( userConfigFile=userConfigFilePath, userKeyFile=userKeyFilePath, url=adminUrl )

#=======================================================================================
# Shutdown managed server
#=======================================================================================
domainRuntime()
tasks = []
myPrintln( 'Shutting DOWN managed server...' )
stopAllManagedServers()
waitManagedServersToStop()

#=======================================================================================
# Undeploy previous version of application
#=======================================================================================
domainConfig()
myPrintln( 'Undeploy...' )
edit()
startEdit()

for cur_app in app_list:
  myPrintln( 'Undeploying PREVIOUS version of :'+cur_app )
  undeploy( cur_app )

save()
activate()

#=======================================================================================
# Deploy new version of FCUBS application
#=======================================================================================
myPrintln( 'Deployment...' )
edit()
startEdit()

for cur_app in app_list:
  myPrintln( 'Deploying NEW version of :'+cur_app )
  deploy( cur_app, deploy_dir+cur_app+'.ear', targets=deploy_target, stageMode='STAGE' )

save()
activate()

#=======================================================================================
# Startup managed server
#=======================================================================================
domainRuntime()
tasks = []
myPrintln( 'Starting UP managed server...')
startAllManagedServers()
waitManagedServersToStart()

#=======================================================================================
# Start servicing all requests
#=======================================================================================
myPrintln( 'Start servicing all requests...' )

for cur_app in app_list:
  myPrintln( 'Starting APP :'+cur_app )
  startApplication( cur_app )

#=======================================================================================
# Disconnect
#=======================================================================================
myPrintln( 'Disconnect...' )
disconnect()

#=======================================================================================
# END
#=======================================================================================
