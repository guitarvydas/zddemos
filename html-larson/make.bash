#!/bin/bash
node ../zd/das2json.mjs <code-generator.drawio >code-generator.json
python3 main.py . - '' main code-generator.json | node ../util/decodeoutput.js
