#!/bin/sh

for dir in AP/2022*; do
  race=$(basename $dir)
  echo $dir
  mkdir -p CSV/$race/
  python3 json2csv.py $dir/summary.json CSV/$race/summary.csv
  python3 json2csv.py $dir/detail.json CSV/$race/detail.csv
  python3 json2csv.py $dir/metadata.json CSV/$race/metadata.csv
done
