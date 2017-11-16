#!/bin/sh

 echo "=================================================================================="
 echo "#  COMPONENT        #  EXPECTED STATUS  #  STATUS                 #  PID         #"
 echo "=================================================================================="
if [ `ps -efx | grep AdminServer | grep java | grep -v grep | grep -v wlogic2 | wc -l` -lt 1 ] 
then
 echo "#  Admin Server     #  RUNNING          #  DOWN                   #              #"
else
 my_pid=`ps -efx | grep AdminServer | grep java | grep -v grep | grep -v wlogic2 | awk '{print $2}'`
 echo "#  Admin Server     #  RUNNING          #  RUNNING                #  `printf %-12s ${my_pid}`#"
fi
if [ `ps -efx | grep NodeManager | grep java | grep -v grep | grep -v wlogic2 | wc -l` -lt 1 ]
then
 echo "#  Node  Manager    #  RUNNING          #  DOWN                   #              #"
else
 my_pid=`ps -efx | grep NodeManager | grep java | grep -v grep | grep -v wlogic2 | awk '{print $2}'`
 echo "#  Node  Manager    #  RUNNING          #  RUNNING                #  `printf %-12s ${my_pid}`#"
fi
if [ `ps -efx | grep Server1 | grep java | grep -v grep | wc -l` -lt 1 ]
then
 echo "#  Server1          #  RUNNING          #  DOWN                   #              #"
else
 state=`cat $DOMAIN_HOME/servers/Server1/data/nodemanager/Server1.state | awk -F":" '{print $1}'`
 my_pid=`ps -efx | grep Server1 | grep java | grep -v grep | awk '{print $2}'`
 echo "#  Server1          #  RUNNING          #  `printf %-23s ${state}`#  `printf %-12s ${my_pid}`#"
fi
 echo "=================================================================================="
 echo "#  Managed by WebLogic                                                           #"
 echo "----------------------------------------------------------------------------------"
if [ `ps -efx | grep NetworkServerControl | grep derby | grep -v grep | grep -v wlogic2 | wc -l` -lt 1 ]
then
 echo "#  Derby DB Server  #  RUNNING          #  DOWN                   #              #"
else
 my_pid=`ps -efx | grep NetworkServerControl | grep derby | grep -v grep | grep -v wlogic2 | awk '{print $2}'`
 echo "#  Derby DB Server  #  RUNNING          #  RUNNING                #  `printf %-12s ${my_pid}`#"
fi
 echo "=================================================================================="