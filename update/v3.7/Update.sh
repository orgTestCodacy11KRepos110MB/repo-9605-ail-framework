#!/bin/bash

[ -z "$AIL_HOME" ] && echo "Needs the env var AIL_HOME. Run the script from the virtual environment." && exit 1;
[ -z "$AIL_REDIS" ] && echo "Needs the env var AIL_REDIS. Run the script from the virtual environment." && exit 1;
[ -z "$AIL_ARDB" ] && echo "Needs the env var AIL_ARDB. Run the script from the virtual environment." && exit 1;
[ -z "$AIL_BIN" ] && echo "Needs the env var AIL_ARDB. Run the script from the virtual environment." && exit 1;
[ -z "$AIL_FLASK" ] && echo "Needs the env var AIL_FLASK. Run the script from the virtual environment." && exit 1;

export PATH=$AIL_HOME:$PATH
export PATH=$AIL_REDIS:$PATH
export PATH=$AIL_ARDB:$PATH
export PATH=$AIL_BIN:$PATH
export PATH=$AIL_FLASK:$PATH

GREEN="\\033[1;32m"
DEFAULT="\\033[0;39m"

echo -e $GREEN"Shutting down AIL ..."$DEFAULT
bash ${AIL_BIN}/LAUNCH.sh -ks
wait

# SUBMODULES #
git submodule update


echo -e $GREEN"Updating thirdparty ..."$DEFAULT
bash ${AIL_BIN}/LAUNCH.sh -ut
wait

echo ""
echo -e $GREEN"Updating AIL VERSION ..."$DEFAULT
echo ""
python ${AIL_HOME}/update/v3.7/Update.py
wait
echo ""
echo ""


echo ""
echo -e $GREEN"Shutting down ARDB ..."$DEFAULT
bash ${AIL_BIN}/LAUNCH.sh -ks
wait

exit 0
