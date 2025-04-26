#!/usr/bin/env bash
#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#*                                                                                    *#
#*                           Copyright (c) 2025 Terminus LLC                          *#
#*                                                                                    *#
#*                                All Rights Reserved.                                *#
#*                                                                                    *#
#*          Use of this source code is governed by LICENSE in the repo root.          *#
#*                                                                                    *#
#**************************** INTELLECTUAL PROPERTY RIGHTS ****************************#
#
set -e

PYTHON_BIN='python3'

function usage() {
    echo "usage: $(basename $0)"
    echo 
    echo '-p <python-exe> : Specify unique python environment to build env off of.'
    echo
}

function check_python_version() {

    PYVERSION="$(${PYTHON_BIN} --version | awk '{print $2}' )"
    PYVERSION2="$( echo ${PYVERSION} | sed 's/\./ /g' )"
    
    PYVERSION_MAJOR="$(echo ${PYVERSION2} | awk '{ print $1 }' )"
    PYVERSION_MINOR="$(echo ${PYVERSION2} | awk '{ print $2 }' )"

    if [ "${PYVERSION_MAJOR}" != '3' ]; then
        echo "Must use Python 3."
        exit 1
    fi
    if [ "${PYVERSION_MINOR}" -lt 11 ]; then
        echo "Must use at least Python version 3.11. Current: ${PYVERSION}"
        exit 1
    fi
    echo "Python Version: [${PYVERSION}] Installed"
}

while [ $# -gt 0 ]; do

    case $1 in

        -h|--help)
            usage
            exit 0
            ;;

        -p)
            shift
            PYTHON_BIN=$1
            echo "using Python ${PYTHON_BIN}"
            ;;

        *)
            echo "unsupported flag: ${1}"
            exit 1
            ;;
    esac
    shift
done


if [ ! -d './.git' ]; then 
    echo 'Run this script from the base repo folder!'
    exit 1
fi

#  Check the version
check_python_version

#  Create venv
${PYTHON_BIN} -m venv venv

#  Activate Virtual Environment
. venv/bin/activate

#  Run pip install upgrade
pip install --upgrade pip
pip install build


