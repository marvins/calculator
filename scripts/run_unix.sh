#!/usr/bin/env bash

# Define path to Micropython
MP_PATH='../lv_micropython/ports/unix/build-lvgl/micropython'
MPC_PATH='../lv_micropython/mpy-cross/build/mpy-cross'

CONFIG_PATH='../data/options.unix.json'

GEN_CONFIG=0
SKIP_RESET=0

function usage() {
    echo 'usage:  run_unix.sh [optional]'
    echo
    echo '-g   : Generate config file'
    echo
    echo '-c   : Config-file to use.'
    echo "       Default: ${CONFIG_PATH}"
    echo
}

#  Command-line options
while [ $# -gt 0 ]; do
    case $1 in 
        -g)
            GEN_CONFIG=1
            ;;
        
        -c)
            shift
            CONFIG_PATH=$1
            ;;
        
        -s)
            SKIP_RESET=1
            ;;
    esac
    shift
done

#  Enter Application Folder
pushd app

#  Launch Application
if [ "${GEN_CONFIG}" = '1' ]; then
    ../${MP_PATH} main.py -c ${CONFIG_PATH} -g
else
    ../${MP_PATH} -i main.py -c ${CONFIG_PATH}
fi

#  Exit
popd

#  Reset terminal
if [ "${SKIP_RESET}" = '0' ]; then
    reset
fi
