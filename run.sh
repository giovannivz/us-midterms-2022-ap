#!/bin/bash

. ./funcs.sh

while [ 1 ]; do
    ./fetch-ap.sh

    gitcommit .

    if (( $RANDOM % 30 == 0 )); then
        sh gen-ref-csv-files.sh HEAD
        gitupload
    fi

    sleep 5
done
