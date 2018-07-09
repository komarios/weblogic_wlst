import jarray

def setupCustomKeystore( p_path, p_keystoreFile, p_keystorePass ):
    cd (p_path)
    set ('KeyStores', 'CustomIdentityAndJavaStandardTrust')
    set ('CustomIdentityKeyStoreFileName', p_keystoreFile)
    set ('CustomIdentityKeyStorePassPhrase', p_keystorePass)
    set ('CustomIdentityKeyStoreType', 'JKS')

def setupSSL( p_path, p_port, p_keyAlias, p_privatekeyPass ):
    cd (p_path)
    set ('ListenPort', p_port)
    set ('Enabled', true)
    set ('ServerPrivateKeyAlias', p_keyAlias)
    set ('ServerPrivateKeyPassPhrase', p_privatekeyPass)
    ciphers = jarray.array( ['TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA', 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256', 'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA', 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384', 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384', 'TLS_DHE_RSA_WITH_AES_128_CBC_SHA', 'TLS_DHE_RSA_WITH_AES_128_CBC_SHA256', 'TLS_DHE_RSA_WITH_AES_128_GCM_SHA256', 'TLS_DHE_RSA_WITH_AES_256_CBC_SHA', 'TLS_DHE_RSA_WITH_AES_256_CBC_SHA256', 'TLS_DHE_RSA_WITH_AES_256_GCM_SHA384', 'TLS_RSA_WITH_AES_128_CBC_SHA', 'TLS_RSA_WITH_AES_128_CBC_SHA256', 'TLS_RSA_WITH_AES_128_GCM_SHA256', 'TLS_RSA_WITH_AES_256_CBC_SHA', 'TLS_RSA_WITH_AES_256_CBC_SHA256', 'TLS_RSA_WITH_AES_256_GCM_SHA384'] , java.lang.String)
    set ('Ciphersuites', ciphers )

def setupClusterReplication( p_path ):
    cd (p_path)
    cluster=cmo.getCluster()
    clusterName=cluster.getName()
    cd('/Clusters/'+clusterName)
    set('SecureReplicationEnabled', true)

print( '   LOAD Variables from file: enableSSL_CLUSTER_VARS.py' )
execfile( 'enableSSLOnCluster_VARS.py')
print( '   Connect to Admin Server' )
connect(  adminUsername, adminPassword, adminURL)
edit()
startEdit()
#####################################################################################################################
print('   Harden Domain')
cd('/')
set('AdministrationPortEnabled', true)
set('AdministrationPort', baseAdminPort)

domainName=cmo.getName()
cd ('/SecurityConfiguration/'+ domainName)
set('UseKSSForDemo', false)

print('   Setup SSL for Node Managers')
cd('/')
for m in cmo.getMachines():
    cd ('/Machines/'+ m.getName() +'/NodeManager/'+ m.getName() )
    set ('NMType', 'SSL')
#####################################################################################################################
print('   Setup SSL for Admin Server')
cd ('/Servers/AdminServer')
set ('ListenPort',         plainAdminPort)
set ('ListenPortEnabled',  false)
set ('AdministrationPort', baseAdminPort)
setupCustomKeystore('/Servers/AdminServer', keystorePath + keystoreFile[0], keystorePass)
setupSSL('/Servers/AdminServer/SSL/AdminServer', SSLAdminPort, keyAlias[0], privatekeyPass)
#####################################################################################################################
print('   Setup SSL for Managed Servers')
for i in range(0, len(managedName)):
    cd ('/Servers/'+ managedName[i])
    set ('ListenPort',         plainMServerPort[i])
    set ('ListenPortEnabled',  false)
    set ('AdministrationPort', adminMServerPort[i])
    setupCustomKeystore('/Servers/'+ managedName[i], keystorePath + keystoreFile[i], keystorePass)
    setupSSL('/Servers/'+ managedName[i] +'/SSL/'+ managedName[i], baseMServerPort[i], keyAlias[i], privatekeyPass)
    setupClusterReplication ('/Servers/'+ managedName[i])
#####################################################################################################################
print('   DONE')
save()
activate()
disconnect()
exit()
