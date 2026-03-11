#!/usr/bin/env bash
# Smoke test: run example .nova files and ensure they exit 0.
# Usage: ./test_smoke.sh   (from project root)

set -e
cd "$(dirname "$0")"
echo "Running example files..."
for f in examples/*.nova; do
  python interpreter.py "$f" > /dev/null && echo "OK   $f" || { echo "FAIL $f"; exit 1; }
done
echo "All example files ran successfully."
