#!/bin/bash
cd hello-world
node ../zd/das2json.mjs <hello-world.drawio >hello-world.json
python3 main.py . - '' indeterminate hello-world.json
python3 main.py . - '' seq1 hello-world.json
python3 main.py . - '' seq2 hello-world.json
cd ..
