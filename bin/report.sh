#!/bin/sh

QUERY_PARAMS_FILE=$1
START_DT=$2
END_DT=$3

if [ "$GAAPY_HOME" == "" ]; then
  export GAAPY_HOME=/Users/sk/workspace/git/gaapy
fi

export PYTHONPATH=$GAAPY_HOME

python $GAAPY_HOME/gaapy/reporter.py --noauth_local_webserver --params=$QUERY_PARAMS_FILE --start $START_DT --end $END_DT
