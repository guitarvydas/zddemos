#!/bin/bash
node ../zd/das2json.mjs <rt.drawio >rt.json
python3 main.py . - '' main rt.json | node ../util/decodeoutput.js
