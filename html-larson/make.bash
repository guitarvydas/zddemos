#!/bin/bash
node ../zd/das2json.mjs <scanner.drawio >scanner.json
python3 main.py . - '' main scanner.json | node ../util/decodeoutput.js
