#!/bin/sh
#
#  Purpose: Compile a Java program
#
#  $Id: jcompile.sh,v 4.2.1.1 2007/10/07 07:10:43 stevej098 Exp $
#
#---------------------------------------------------------------------

# export JAVA_HOME=/c/PROGRA~1/Java/j2sdk1.4.2_08

echo "JAVA_HOME => $JAVA_HOME"

ARGS=$*

WRK=`pwd`; export WRK

CLASSPATH="..\..\..\java\lib\braju.jar:$..\..\..\java\lib\pdq.jar:."; export CLASSPATH

echo "CLASSPATH => $CLASSPATH"

V=-verbose
V=

for ARG in $ARGS; do
   $JAVA_HOME/bin/javac $V -classpath $CLASSPATH $ARG
done

