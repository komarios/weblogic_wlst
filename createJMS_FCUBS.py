import sys
from java.lang import System
#####################################################################################################################
print "Load variables from file: create_datasources_VARS.py"
execfile('create_datasources_VARS.py')
#####################################################################################################################
print "Script Parameters :"
print "   adminUsername    = "+adminUsername
print "   adminPassword    = "+adminPassword
print "   adminURL         = "+adminURL
print "   jmsTargetServer  = "+jmsTargetServer
print "   jmsModule        = "+jmsModule
print "   jmsSubdeployment = "+jmsSubdeployment
#####################################################################################################################
print "Connect to Admin server ..."
connect(adminUsername, adminPassword, adminURL)
#####################################################################################################################
print "Start new edit session ..."
edit()
startEdit()
#####################################################################################################################
print "Get target server MBean : "+jmsTargetServer
servermb=getMBean("Servers/"+jmsTargetServer)
if servermb is None:
        print "FAILURE: NO server MBean with name "+jmsTargetServer+" found in domain:"+adminURL
else:
        print "SUCCESS: Server MBean with name "+jmsTargetServer+" found in domain:"+adminURL
#=======================================================================================
# Create a JMS System resource.
#=======================================================================================
print "Creating "+ jmsModule +" and target it to "+jmsTargetServer
GWSystemResourceObj=create( jmsModule, 'JMSSystemResource')
GWSystemResourceObj.addTarget(servermb)
theJMSResource=GWSystemResourceObj.getJMSResource()
print "Done"
#=======================================================================================
# Create connection factories.
#=======================================================================================
print "Creating connection factories..."
for i in range(0, len(jmsConnectionFactories)):
  print "Creating Connection Factory :"
  print "   jmsConnectionFactory="+jmsConnectionFactories[i]
  cd('/JMSSystemResources/'+ jmsModule +'/JMSResource/'+ jmsModule)
  curConnFact=cmo.createConnectionFactory( jmsConnectionFactories[i] )
  cd('/JMSSystemResources/'+ jmsModule +'/JMSResource/'+ jmsModule +'/ConnectionFactories/'+ jmsConnectionFactories[i] )
  curConnFact.setJNDIName( jmsConnectionFactories[i] )
  curConnFact.setSubDeploymentName( jmsSubdeployment )
  cd('/JMSSystemResources/'+ jmsModule +'/JMSResource/'+ jmsModule +'/ConnectionFactories/'+ jmsConnectionFactories[i] +'/TransactionParams/'+ jmsConnectionFactories[i] )
  cmo.setXAConnectionFactoryEnabled(true)
print "Done"
#=======================================================================================
# Create queues.
#=======================================================================================
print "Creating queues..."
for i in range(0, len(jmsQueues)):
  print "Creating Queue :"
  print "   jmsQueue="+jmsQueues[i]
  curJMSQueue=theJMSResource.createQueue( jmsQueues[i] )
  curJMSQueue.setJNDIName( jmsQueues[i] )
  curJMSQueue.setSubDeploymentName( jmsSubdeployment )
print "Done"
#=======================================================================================
# Create a JMS server with a file store
#=======================================================================================
print "Creating JMS File Store and target it to "+jmsTargetServer
filestoremb=create('FileStore-0','FileStore')
filestoremb.addTarget( servermb )
jmsserver1mb=create('JMSServer-0','JMSServer')
jmsserver1mb.setPersistentStore( filestoremb )
jmsserver1mb.addTarget( servermb )
print "Done"
#=======================================================================================
# Create the subdeployment.
#=======================================================================================
print "Creating subdeployment and target it to the JMS server..."
subDeplmb=GWSystemResourceObj.createSubDeployment( jmsSubdeployment )
subDeplmb.addTarget( jmsserver1mb )
print "Done"
#===================================================================
# Save and Activate changes
#===================================================================
print "Saving and activating changes..."
save()
activate()
exit()
print "Done"
#===================================================================