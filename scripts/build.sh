#!/usr/bin/env bash
#


#  Path to pico-sdk
#  - Users should set their own path
PICO_SDK_PATH="${HOME}/Desktop/Projects/pico-sdk"

export PICO_SDK_PATH

mkdir -p build

pushd build

cmake ..

popd