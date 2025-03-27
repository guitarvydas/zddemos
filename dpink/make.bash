#!/bin/bash
cd agency
make
cd ..
node ../zd/das2json.mjs <dpink.drawio >dpink.json
python3 main.py . - '' main dpink.json | jq -M .
