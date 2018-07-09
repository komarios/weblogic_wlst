# Create response file :
# Installation Type : "Fusion Middleware Infrastructure", "Fusion Middleware Infrastructure With Examples"
echo "[ENGINE]
Response File Version=1.0.0.0.0
[GENERIC]
ORACLE_HOME=/weblogic/product/12.2.1.2
INSTALL_TYPE=Fusion Middleware Infrastructure
MYORACLESUPPORT_USERNAME=
MYORACLESUPPORT_PASSWORD=<SECURE VALUE>
DECLINE_SECURITY_UPDATES=true
SECURITY_UPDATES_VIA_MYORACLESUPPORT=false
PROXY_HOST=
PROXY_PORT=
PROXY_USER=
PROXY_PWD=<SECURE VALUE>
COLLECTOR_SUPPORTHUB_URL=" > /weblogic/tmp/binaries.rsp

mkdir -p /weblogic/oraInventory

echo "inst_group=wlogic
inventory_loc=/weblogic/oraInventory" > /weblogic/oraInventory/oraInst.loc

java -d64 -jar /weblogic/tmp/fmw_12.2.1.2.0_infrastructure.jar -silent -responseFile /weblogic/tmp/binaries.rsp -invPtrLoc /weblogic/oraInventory/oraInst.loc

# Show WebLogic Version
. /weblogic/product/12.2.1.2/wlserver/server/bin/setWLSEnv.sh
java weblogic.version
