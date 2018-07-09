# WLST Connection Details
adminUsername, adminPassword, adminURL = 'weblogic', 'weblogicPass', 't3://...:9001/'

# Admin Server's Configuration
baseAdminPort   =   9001
plainAdminPort  =  19001
SSLAdminPort    =  29001

# Managed Server's Configuration
managedName     = ['managed1','managed2']
baseMServerPort = [  9002,  9002 ]
plainMServerPort= [ 19002, 19002 ]
adminMServerPort= [  9012,  9012 ]

# Common Keystore Configuration
keyAlias        = ['host1', 'host2']
keystorePass    = 'myPass'
privatekeyPass  = 'myPass'
keystorePath    = '/my/path/to/keystore/location/'
keystoreFile    = ['host1_keystore.jks', 'host2_keystore.jks']
