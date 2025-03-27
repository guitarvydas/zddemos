#!/bin/bash
cd hello-world
node ../zd/das2json.mjs <hello-world.drawio >hello-world.json
python3 main.py . - '' nondeterministic hello-world.json
python3 main.py . - '' seq1 hello-world.json
python3 main.py . - '' seq2 hello-world.json
python3 main.py . - '' seq3 hello-world.json
python3 main.py . - '' seq3a hello-world.json
python3 main.py . - '' seq4 hello-world.json
python3 main.py . - '' seq4a hello-world.json
cd ..

cd arith
./make.bash
cd ..
