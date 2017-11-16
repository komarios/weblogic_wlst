import sys

def startAllManagedServers():
 for server in cmo.getServerLifeCycleRuntimes():
#  if ( (server.getName() == 'myserver1' or server.getName() == 'myserver2' ):
  if (server.getName() != 'AdminServer' and server.getState() != 'RUNNING' ):
   tasks.append(server.start())

def waitTillCompleted ():
 sys.stdout.write('Waiting for managed servers to start')
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
startAllManagedServers()
waitTillCompleted()
disconnect()