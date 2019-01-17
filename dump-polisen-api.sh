#!/bin/sh
set -o errexit
set -o pipefail

dir='api'
mkdir -p "$dir"

file="$dir/$(date -I).json.gz"
curl -sS 'https://polisen.se/api/events' | gzip >"$file" && echo "==> $file"
