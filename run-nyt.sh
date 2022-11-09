#!/bin/sh

. ./funcs.sh

while [ 1 ]; do
    ./fetch-nyt.sh
    gitupload NYT
done
