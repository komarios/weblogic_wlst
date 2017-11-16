#!/bin/sh

./startupNMandAdminServer.sh

./statusWebLogicInfra.sh

./startupAllManagedServers.sh

./statusWebLogicInfra.sh