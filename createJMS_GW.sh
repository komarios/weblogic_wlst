#!/bin/sh

cd $DOMAIN_HOME/bin
. ./setDomainEnv.sh
cd $INFRA_HOME

echo "Create filestore path : /weblogic/app/GW_JMS"
mkdir -p $INFRA_HOME/../app/GW_JMS

java -classpath ${FMWCONFIG_CLASSPATH} ${MEM_ARGS} ${JVM_D64} ${JAVA_OPTIONS} weblogic.WLST ./createJMS_GW.py 2>&1
