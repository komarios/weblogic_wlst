#!/bin/sh

echo "Killing nodemanager"
nm_pid=`ps -efx | grep java | grep wlogic | grep -v wlogic2 | grep -i NodeManager | awk '{print $2}'`
kill -9 ${nm_pid}

cd $DOMAIN_HOME/bin
. ./setDomainEnv.sh
cd $DOMAIN_HOME/bin

echo  "Stopping Admin Server "
./stopWebLogic.sh