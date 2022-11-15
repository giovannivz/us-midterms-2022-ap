#!/bin/bash

. ./funcs.sh

while [ 1 ]; do
    ./fetch-ap.sh

    gitcommit .
    sh gen-ref-csv-files.sh HEAD

    if (( $RANDOM % 30 == 0 )); then
        gitupload
    fi

    sleep 5
done
