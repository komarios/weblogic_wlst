cd $DOMAIN_HOME/bin
. ./setDomainEnv.sh
cd /weblogic/bin

if [ -z "$1" ]
then
  echo "ERROR: not enough parameters"
  echo "USAGE:"
  echo " $0 {name_of_python_executable.py}"
  echo "e.g."
  echo " $0 myWLSTScript.py"
  exit 1
fi

java -classpath ${FMWCONFIG_CLASSPATH} ${MEM_ARGS} ${JVM_D64} ${JAVA_OPTIONS} weblogic.WLST $1 2>&1
