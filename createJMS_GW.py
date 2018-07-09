import sys
#from java.lang import System
#=======================================================================================
# Function Definitions
#=======================================================================================
def printScriptVariables( p_variablesFile ):
  print "Loaded variables from : "+ p_variablesFile
  print "   adminUsername  : "+ adminUsername
  print "   adminPassword  : "+ adminPassword
  print "   adminURL       : "+ adminURL
  print "   jmsTargetServer: "+ jmsTargetServer
  print "   jmsServerName  : "+ jmsServerName
  print "   jmsFileStore   : "+ jmsFileStore
  print "   jmsFileStoreDir: "+ jmsFileStoreDir

def connectToAdminServer( p_adminUsername, p_adminPassword, p_adminURL ):
  print "Connect to Admin server"
  connect( p_adminUsername, p_adminPassword, p_adminURL )
  print "Start new edit session"
  edit()
  startEdit()

def createNewJMSModule( p_jmsModule, p_jmsTargetServer, p_jmsTargetServerMBean ):
  print "Create "+ p_jmsModule +" and target it to "+ p_jmsTargetServer
  cd('/')
  v_jmsModuleObj= cmo.createJMSSystemResource( p_jmsModule )
  v_jmsModuleObj.addTarget( p_jmsTargetServerMBean )
  #v_theJMSResource= v_jmsModuleObj.getJMSResource()
  print " Done"
  return v_jmsModuleObj
  
def createNewLocalConnectionFactories( p_jmsConnectionFactories, p_jmsModuleObj, p_jmsSubdeployment ):
  print "Create LOCAL connection factories"
  for i in range(0, len(p_jmsConnectionFactories)):
    print "   Connection Factory: "+ p_jmsConnectionFactories[i]
    v_connectionFactoryObj= p_jmsModuleObj.createConnectionFactory( p_jmsConnectionFactories[i] )
    v_connectionFactoryObj.setJNDIName( p_jmsConnectionFactories[i] )
    v_connectionFactoryObj.setSubDeploymentName( p_jmsSubdeployment )
    v_jmsConnFactoryPath= getPath( v_connectionFactoryObj )
    cd( '/'+ v_jmsConnFactoryPath +'/TransactionParams/'+ p_jmsConnectionFactories[i] )
    cmo.setXAConnectionFactoryEnabled( true )
  print " Done"

def createNewLocalQueues( p_jmsQueues, p_jmsSubdeployment, p_jmsModuleObj ):
  print "Create LOCAL queues"
  for i in range(0, len(p_jmsQueues)):
    print "   Queue: "+ p_jmsQueues[i]
    curJMSQueue= p_jmsModuleObj.createQueue( p_jmsQueues[i] )
    curJMSQueue.setJNDIName( p_jmsQueues[i] )
    curJMSQueue.setSubDeploymentName( p_jmsSubdeployment )
  print " Done"

def createNewJMSFilestore( p_jmsFileStore, p_jmsFileStoreDir, p_jmsTargetServer, p_jmsTargetServerMBean ):
  print "Create JMS File Store "+ p_jmsFileStore +" with target "+ p_jmsTargetServer
  cd('/')
  v_filestoreObj=cmo.createFileStore( p_jmsFileStore )
  v_filestoreObj.setDirectory( p_jmsFileStoreDir )
  v_filestoreObj.addTarget( p_jmsTargetServerMBean )
  print " Done"
  return v_filestoreObj

def createNewJMSServerWithFilestore( p_jmsServerName, p_jmsTargetServer, p_jmsFileStore, p_filestoreObj, p_jmsTargetServerMBean ):
  print "Create JMS Server "+ p_jmsServerName +" with target "+ p_jmsTargetServer +" and file store "+ p_jmsFileStore
  cd('/')
  v_jmsServerObj= cmo.createJMSServer( p_jmsServerName )
  v_jmsServerObj.setPersistentStore( p_filestoreObj )
  v_jmsServerObj.addTarget( p_jmsTargetServerMBean )
  print " Done"
  return v_jmsServerObj

def createNewSubdeployment( p_jmsSubdeployment, p_jmsServerName, p_jmsServerObj, p_jmsModuleObj ):
  print "Create subdeployment "+ p_jmsSubdeployment +" with target "+ p_jmsServerName
  v_subdeployment= p_jmsModuleObj.createSubDeployment( p_jmsSubdeployment )
  #localSubdeployment= localJmsModule.createSubDeployment( jmsSubdeployment )
  v_subdeployment.addTarget( p_jmsServerObj )
  print " Done"

def createNewJMSForeignServer( p_jmsForeignServer, p_jmsForeignSubdeployment, p_jmsModuleObj ):
  print "Create FOREIGN JMS Server "+ p_jmsForeignServer
  v_foreignServerObj= p_jmsModuleObj.createForeignServer( p_jmsForeignServer )
  v_foreignServerObj.setInitialContextFactory( 'com.sun.jndi.fscontext.RefFSContextFactory' )
  v_foreignServerObj.setConnectionURL( 'file:///var/mqm/JNDI' )
  v_foreignServerObj.setDefaultTargetingEnabled( false )
  v_foreignServerObj.setSubDeploymentName( p_jmsForeignSubdeployment )
  # cmo.unSet('JNDIPropertiesCredentialEncrypted') ???
  # JNDI Properties Credential: ???
  # Confirm JNDI Properties Credential: ???
  print " Done"
  return v_foreignServerObj

def createNewForeignDestinations( p_foreignServerObj, p_jmsForeignDestinations ):
  print "Create FOREIGN Destinations"
  for i in range(0, len(p_jmsForeignDestinations)):
    print "  FOREIGN Destination: "+ p_jmsForeignDestinations[i]
    v_foreignDestination= p_foreignServerObj.createForeignDestination( p_jmsForeignDestinations[i] )
    v_foreignDestination.setLocalJNDIName(  p_jmsForeignDestinations[i] )
    v_foreignDestination.setRemoteJNDIName( p_jmsForeignDestinations[i] )
  print " Done"

def createNewForeignConnectionFactories( p_foreignServerObj, p_jmsForeignConnFactories, p_jmsForeignServerUser, p_jmsForeignServerPass, p_domainHomeDir ):
  print "Create FOREIGN connection factories"
  for i in range(0, len(p_jmsForeignConnFactories)):
    print "   FOREIGN Connection Factory: "+ p_jmsForeignConnFactories[i]
    v_foreignConnectionFactory= p_foreignServerObj.createForeignConnectionFactory( p_jmsForeignConnFactories[i] )
    v_foreignConnectionFactory.setLocalJNDIName(  p_jmsForeignConnFactories[i] )
    v_foreignConnectionFactory.setRemoteJNDIName( p_jmsForeignConnFactories[i] )
    v_foreignConnectionFactory.setUsername( p_jmsForeignServerUser )
    v_encPass= encrypt( p_jmsForeignServerPass, p_domainHomeDir )
    v_foreignConnectionFactory.setPasswordEncrypted( v_encPass )
  print " Done"

def disconnectFromAdminServer():
  print "Saving and activating changes"
  save()
  activate()
  print " Done"
  exit()
#=======================================================================================
# Main
#=======================================================================================
execfile( 'createJMS_GW_VARS.py' )
printScriptVariables( 'createJMS_GW_VARS.py' )
connectToAdminServer( adminUsername, adminPassword, adminURL )
jmsTargetServerMBean= getMBean( "/Servers/"+ jmsTargetServer )
if jmsTargetServerMBean is None:
  sys.exit("Target Server ["+ jmsTargetServer +"] MBean is None") 

localJMSModuleObj= createNewJMSModule( jmsModule, jmsTargetServer, jmsTargetServerMBean )
localJMSModuleResource= localJMSModuleObj.getJMSResource()
createNewLocalConnectionFactories( jmsConnectionFactories, localJMSModuleResource, jmsSubdeployment )
createNewLocalQueues( jmsQueues, jmsSubdeployment, localJMSModuleResource )
filestoreObj= createNewJMSFilestore( jmsFileStore, jmsFileStoreDir, jmsTargetServer, jmsTargetServerMBean )
jmsServerObj= createNewJMSServerWithFilestore( jmsServerName, jmsTargetServer, jmsFileStore, filestoreObj, jmsTargetServerMBean )
createNewSubdeployment( jmsSubdeployment, jmsServerName, jmsServerObj, localJMSModuleObj )

foreignJMSModuleObj= createNewJMSModule( jmsForeignModule, jmsTargetServer, jmsTargetServerMBean )
foreignJMSModuleResource= foreignJMSModuleObj.getJMSResource()
foreignServerObj= createNewJMSForeignServer( jmsForeignServer, jmsForeignSubdeployment, foreignJMSModuleResource )
createNewForeignDestinations( foreignServerObj, jmsForeignDestinations )
createNewForeignConnectionFactories( foreignServerObj, jmsForeignConnFactories, jmsForeignServerUser, jmsForeignServerPass, domainHomeDir )
createNewSubdeployment( jmsForeignSubdeployment, jmsServerName, jmsServerObj, foreignJMSModuleObj )

disconnectFromAdminServer()
