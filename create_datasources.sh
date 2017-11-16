#!/bin/sh

cd $DOMAIN_HOME/bin
. ./setDomainEnv.sh
cd /weblogic/bin

java -classpath ${FMWCONFIG_CLASSPATH} ${MEM_ARGS} ${JVM_D64} ${JAVA_OPTIONS} weblogic.WLST ./create_datasources.py 2>&1