#!/bin/sh

. ./funcs.sh

while [ 1 ]; do
    ./fetch-ap.sh
    ./fetch-nyt.sh
    gitupload .
done
