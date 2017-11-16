import sys

def stopAllManagedServers():
 for server in cmo.getServerLifeCycleRuntimes():
#  if ( (server.getName() == 'myserver1' or server.getName() == 'myserver2' ):
  if (server.getName() != 'AdminServer' and server.getState() != 'SHUTDOWN' ):
   tasks.append(server.forceShutdown())

def waitTillCompleted ():
 sys.stdout.write('Waiting for managed servers to shutdown')
 while len(tasks) > 0:
  for task in tasks:
   if task.getStatus()  != 'TASK IN PROGRESS' :
    tasks.remove(task)
  java.lang.Thread.sleep(1000)
  sys.stdout.write('.')
 print('.')

connect('weblogic','welcome1','t3://localhost:7001');
domainRuntime()
tasks = []
stopAllManagedServers()
waitTillCompleted()
disconnect()