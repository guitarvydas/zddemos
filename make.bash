#!/bin/bash
cd hello-world
node ../zd/das2json.mjs <hello-world.drawio >hello-world.json
python3 main.py . - '' main hello-world.json
cd ..
