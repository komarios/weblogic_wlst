#!/bin/sh

. $DOMAIN_HOME/bin/setDomainEnv.sh
cd $INFRA_HOME

java -classpath ${FMWCONFIG_CLASSPATH} ${MEM_ARGS} ${JVM_D64} ${JAVA_OPTIONS} weblogic.WLST ./convertDataSourceToGridLink.py 2>&1
