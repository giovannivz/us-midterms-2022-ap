#!/bin/sh

. ./funcs.sh

download "AP" https://2022-election-production.newyorker.com/api/articles
download "AP" https://interactives.ap.org/election-results/data-live/2022-11-08/results/national/progress.json
download "AP" https://interactives.ap.org/election-results/data-live/2022-11-08/results/national/metadata.json

python3 updated.py

cat updated-urls.txt | xargs -n 2 -P 5 ./download.sh

sleep 5