#!/bin/bash
set -euo pipefail

curl "https://s3.amazonaws.com/ds2002-resources/labs/lab3-bundle.tar.gz" -o lab3-bundle.tar.gz

tar -xzf lab3-bundle.tar.gz

# awk can remove blank / whitespace-only lines
awk '!/^[[:space:]]*$/' lab3_data.tsv > cleaned.tsv

tr '\t' ',' < cleaned.tsv > cleaned.csv

LINECOUNT=$(wc -l < cleaned.csv)
ROWS=$((LINECOUNT - 1))
echo "There are $ROWS lines in the file."

tar -czf converted-archive.tar.gz cleaned.csv


