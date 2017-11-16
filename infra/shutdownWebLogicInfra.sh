#!/bin/sh

./shutdownAllManagedServers.sh

./statusWebLogicInfra.sh

./shutdownNMandAdminServer.sh

./statusWebLogicInfra.sh