import jarray

def setupCustomKeystore( p_path, p_keystoreFile, p_keystorePass ):
    cd (p_path)
    set ('KeyStores', 'CustomIdentityAndJavaStandardTrust')
    set ('CustomIdentityKeyStoreFileName', p_keystoreFile)
    set ('CustomIdentityKeyStorePassPhrase', p_keystorePass)
    set ('CustomIdentityKeyStoreType', 'JKS')

def setupSSL( p_path, p_port, p_serversHostname, p_privatekeyPass ):
    cd (p_path)
    set ('ListenPort', p_port)
    set ('Enabled', true)
    set ('ServerPrivateKeyAlias', p_serversHostname)
    set ('ServerPrivateKeyPassPhrase', p_privatekeyPass)
    ciphers = jarray.array( ['TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA', 'TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256', 'TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA', 'TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384', 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384', 'TLS_DHE_RSA_WITH_AES_128_CBC_SHA', 'TLS_DHE_RSA_WITH_AES_128_CBC_SHA256', 'TLS_DHE_RSA_WITH_AES_128_GCM_SHA256', 'TLS_DHE_RSA_WITH_AES_256_CBC_SHA', 'TLS_DHE_RSA_WITH_AES_256_CBC_SHA256', 'TLS_DHE_RSA_WITH_AES_256_GCM_SHA384', 'TLS_RSA_WITH_AES_128_CBC_SHA', 'TLS_RSA_WITH_AES_128_CBC_SHA256', 'TLS_RSA_WITH_AES_128_GCM_SHA256', 'TLS_RSA_WITH_AES_256_CBC_SHA', 'TLS_RSA_WITH_AES_256_CBC_SHA256', 'TLS_RSA_WITH_AES_256_GCM_SHA384'] , java.lang.String)
    set ('Ciphersuites', ciphers )

def setupClusterReplication( p_path ):
    cd (p_path)
    cluster=cmo.getCluster()
    clusterName=cluster.getName()
    cd('/Clusters/'+clusterName)
    set('SecureReplicationEnabled', true)

execfile( 'enableSSL_VARS.py')
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

print('   Setup SSL for Node Manager')
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
setupCustomKeystore('/Servers/AdminServer', keystoreFile, keystorePass)
setupSSL('/Servers/AdminServer/SSL/AdminServer', SSLAdminPort, serversHostname, privatekeyPass)
#####################################################################################################################
print('   Setup SSL for Managed Server')
cd ('/Servers/'+ managedName)
set ('ListenPort',         plainMServerPort)
set ('ListenPortEnabled',  false)
set ('AdministrationPort', adminMServerPort)
setupCustomKeystore('/Servers/'+ managedName, keystoreFile, keystorePass)
setupSSL('/Servers/'+ managedName +'/SSL/'+ managedName, baseMServerPort, serversHostname, privatekeyPass)
setupClusterReplication ('/Servers/'+ managedName)
#####################################################################################################################
print('   DONE')
save()
activate()
disconnect()
exit()
