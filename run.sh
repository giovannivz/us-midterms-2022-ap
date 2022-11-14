#!/bin/bash

. ./funcs.sh

while [ 1 ]; do
    ./fetch-ap.sh

    gitcommit .

    if (( $RANDOM % 30 == 0 )); then
        gitupload
    fi

    sleep 5
done
