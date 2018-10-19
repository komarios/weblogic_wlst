# Set admin url pointing to AdminServer
userConfigFilePath='/weblogic/bin/WLSTSecureConfigFile'
userKeyFilePath='/weblogic/bin/WLSTSecureKeyFile'
adminURL='t3s://...:7001'

# ACTIVE DIRECTORY PARAMETERS
providerName='AD01'
providerHost='AD01'
principalUser='ADuser'
principalPass='ADpass'

userBaseDN='ou=Users,dc=DomainController.eu'
groupBaseDN='ou=Groups,dc=DomainController,dc=eu'

connPoolSize=1000
connTimeout=60
cacheSize=32000
cacheTTL=6000
