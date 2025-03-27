#!/bin/bash
cd agency
make
cd ..
node ../zd/das2json.mjs <dpink.drawio >dpink.json
python3 main.py . - 'What is 1.6kg in lb?' main dpink.json | jq -M .
