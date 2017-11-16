# Set all variables from values in properties file.
adminUsername   = 'weblogic'
adminPassword   = '...'
adminURL        = 't3://...:7001'
domainHomeDir   = '/weblogic/config/a_domain'

jmsTargetServer = 'manage_server1'
jmsServerName   = 'JMSServer-0'
jmsFileStore    = 'FileStore-0'
jmsFileStoreDir = '/weblogic/app/FileStore'

# FCUBS GateWay LOCAL JMS Resources
jmsModule              = 'L_Module'
jmsSubdeployment       = 'JMS_SUB'
jmsConnectionFactories =['L_QCF']
jmsQueues              =['L_QUEUE']

# FCUBS GateWay FOREIGN JMS Resources
jmsForeignModule       = 'A_MODULE'
jmsForeignSubdeployment= 'A_SUB'
jmsForeignServer       = 'A_Server'
jmsForeignServerUser   = 'mquser'
jmsForeignServerPass   = 'mqpass'
jmsForeignConnFactories=['A_QCF']
jmsForeignDestinations =['A_DEST_QUEUE']