# Set admin url pointing to AdminServer
userConfigFilePath='/weblogic/bin/WLSTSecureConfigFile'
userKeyFilePath='/weblogic/bin/WLSTSecureKeyFile'
adminURL='t3s://...:7001'

# Domain Level
jtaTimeoutSeconds=300
JSPCompilerBackwardsCompatible=1
showArchivedRealPathEnabled=1

# Managed Server Level
stuckThreadMaxTime=900
minimumSeverityToLog='Warning'
logFileSeverityLevel='Warning'
standardOutSeverityLevel='Critical'
domainLogBroadcasterSeverityLevel='Critical'
httpAccessLogFileEnabled=1
# OBDX Specific
obdxSpecific=1
extendedLoggingFormatFields='date time cs-method cs-uri sc-status'
limitNumberOfRetainedFiles=1
filesToRetain=100
optimizeSecureRandomNumberGeneration='-Djava.security.egd=file:/dev/./urandom'
# -Xms8G -Xmx8G (Or 16G if available)

# Data Source Level
dsConnectionReserveTimeout=10
dsTestFrequencySeconds=360
dsInactiveConnectionTimeout=0
dsInitCapacity=100
dsMaxCapacity=750
dsMinCapacity=100
dsShrinkFrequencySeconds=900
dsTestQuery='SQL ISVALID'
dsInitSQL=0
dsTestConnectionsOnReserve=1
dsStatementCacheType='LRU'
dsStatementCacheSize=1000
dsStreamChunkSize=4096

# OBDX Specific : 
# ACTIVE DIRECTORY PARAMETERS
# myrealm > Providers > ADAuthenticator
ldapProviderConnectionPoolSize=1000
ldapProviderConnectTimeout=60
ldapProviderConnectionRetryLimit=1
