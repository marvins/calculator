#!/usr/bin/env bash

# Define path to Micropython
MP_PATH='../lv_micropython/ports/unix/build-lvgl/micropython'
MPC_PATH='../lv_micropython/mpy-cross/build/mpy-cross'

GEN_CONFIG='0'

function usage() {
    echo 'usage:  run_unix.sh [optional]'
    echo
    echo '-g   : Generate config file'
    echo
}

#  Command-line options
while [ $# -gt 0 ]; do
    case $1 in 
        -g)
            GEN_CONFIG=1
            ;;
    esac
done

#  Enter Application Folder
pushd app

#  Launch Application
if [ "${GEN_CONFIG}" = '1' ]; then
    ../${MP_PATH} main.py -c ../data/options.unix.json -g
else
    ../${MP_PATH} -i main.py -c ../data/options.unix.json
fi

#  Exit
popd

#  Reset terminal
reset
