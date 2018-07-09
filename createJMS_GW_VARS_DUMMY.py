# Set all variables from values in properties file.
userConfigFilePath='/weblogic/bin/WLSTSecureConfigFile'
userKeyFilePath='/weblogic/bin/WLSTSecureKeyFile'
adminURL='t3s://...:7001'

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
