#!/bin/sh
#------------------------------------------------------------------------------
# @(#) Subject : Get a managed server's state through nodemanager 
# @(#) Author: KOGIAS M. - ALPHA BANK SA
#------------------------------------------------------------------------------
# @(#) Usage: getManagedServerState.sh
#
#  Launch example : ./getManagedServerState.sh manage_server_name
# History:
# -------
#
# Revision              Who             When            Object
# --------
#  1.0                  MKO           25/04/2016        Creation
#------------------------------------------------------------------------------
server_name=$1

cd $DOMAIN_HOME/bin
. ./setDomainEnv.sh
cd /weblogic/bin

java -classpath ${FMWCONFIG_CLASSPATH} ${MEM_ARGS} ${JVM_D64} ${JAVA_OPTIONS} weblogic.WLST ./getManagedServerState.py $server_name 2>&1