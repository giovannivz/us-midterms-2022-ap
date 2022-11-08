#!/bin/sh

. ./funcs.sh

download "AP" https://2022-election-production.newyorker.com/api/articles
download "AP" https://interactives.ap.org/election-results/data-live/2022-11-08/results/national/progress.json
download "AP" https://interactives.ap.org/election-results/data-live/2022-11-08/results/national/metadata.json

cat ap-urls.txt | xargs -n 2 -P 5 ./download.sh
