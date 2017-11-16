#!/bin/sh

cd $DOMAIN_HOME/bin
./NodeManagerStart.sh

printf "Starting nodemanager "
while [ `grep 'socket listener started on port' nodemanager.log | wc -l` -lt 1 ]
do
  printf "."
  sleep 1
done
printf "\n"

cd $DOMAIN_HOME/bin
. ./setDomainEnv.sh
cd $DOMAIN_HOME/bin
./StartAdminServer.sh

printf "Starting Admin Server "
while [ `grep RUNNING admin.log | wc -l` -lt 1 ]
do
  printf "."
  sleep 1
done
printf "\n"