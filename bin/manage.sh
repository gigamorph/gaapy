#!/bin/sh

if [ "$GAAPY_HOME" == "" ]; then
  export GAAPY_HOME=/Users/sk/workspace/git/gaapy
fi

export PYTHONPATH=$GAAPY_HOME

python $GAAPY_HOME/gaapy/manager.py --noauth_local_webserver "$1" "$2" "$3" "$4"
