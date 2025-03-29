#!/bin/bash
echo ' the Info messages are progress indicators'
node ../zd/das2json.mjs <code-generator.drawio >code-generator.json
python3 main.py . - '' main code-generator.json | node ../util/decodeoutput.js
echo 'open a browser on ./ledst.html'
echo 'the leds should cycle from left to right then back right to left for a while, then stop'
