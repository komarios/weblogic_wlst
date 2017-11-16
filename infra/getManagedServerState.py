import sys

connect('weblogic','welcome1','t3://localhost:7001');
domainRuntime()
state(sys.argv[1],'Server')
disconnect()