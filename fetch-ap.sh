#!/bin/sh

. ./funcs.sh

#download "AP" https://2022-election-production.newyorker.com/api/articles
#download "AP" https://interactives.ap.org/election-results/data-live/2022-11-08/results/national/progress.json
#download "AP" https://interactives.ap.org/election-results/data-live/2022-11-08/results/national/metadata.json

python3 fetch-updated.py ap-base-urls.txt
python3 gen-updated-urls.py

python3 fetch-updated.py updated-urls.txt