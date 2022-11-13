#!/bin/sh

. ./funcs.sh

while [ 1 ]; do
    ./fetch-ap.sh
    gitupload .
    sleep 10
done
