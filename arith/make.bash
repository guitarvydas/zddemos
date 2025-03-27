#!/bin/bash
node ../zd/das2json.mjs <arith.drawio >arith.json
python3 main.py . - 'ex1.math' main arith.json | jq -M --compact-output .
