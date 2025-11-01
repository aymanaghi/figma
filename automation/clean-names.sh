#!/bin/bash
# clean-names.sh
# remove spaces and uppercase from exported file names

for f in *.png; do
  new=$(echo "$f" | tr '[:upper:]' '[:lower:]' | tr ' ' '_')
  mv "$f" "$new"
  echo "🧼 $f → $new"
done
