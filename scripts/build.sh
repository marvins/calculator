#!/usr/bin/env bash
#
#    File:    build.sh
#    Author:  Marvin Smith
#    Date:    8/2/2025
#

#  Path to pico-sdk
#  - Users should set their own path
PICO_SDK_PATH="${HOME}/Desktop/Projects/pico-sdk"
export PICO_SDK_PATH

function build_software() {
    mkdir -p build
    pushd build
    cmake ..
    make
    popd
}

while [ $# -gt 0 ]; do

    case $1 in
        -c|--clean)
            rm -rf build
            ;;

    *)
        echo "Unsupported argument: $1"
        exit 1
        ;;
    esac

    shift

done

#--------------------------------#
#-      Build the Software      -#
#--------------------------------#
build_software
