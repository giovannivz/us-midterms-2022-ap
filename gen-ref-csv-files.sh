#!/bin/bash

ref=$1

if [ -z "$ref" ]; then
  ref=HEAD
fi

files=$(git show --pretty="" --name-only $ref)

for file in $files; do
  dir=$(basename $(dirname $file))

  if [ "$dir" = "AP" -o "$dir" = "timestamps" -o "$dir" = "." ]; then
    continue
  fi

  csvfile="CSV/$dir/$(basename -s '.json' $file).csv"

  echo $file $csvfile

  mkdir -p CSV/$dir
  python3 json2csv.py $file $csvfile
done
