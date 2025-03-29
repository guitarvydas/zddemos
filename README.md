# 4 demos of 0D
- hello world
- arith - a simple expression grammar compiled to Python, Javascript, Common Lisp all at once
- dpink - an LLM experiment based on Daniel Pink's advice to ask the question "Why?" 5 times
- 0d kernel written in rt and compiled to Python, Javascript, Common Lisp


# Usage:
./make.bash

# Source Code
I think that the drawware source code is more important than the 0D kernel.

The source code for the examples is in .drawio files, i.e. 
- `hello-world/hello-world.drawio`
- `arith/arith0d.drawio`
- `dpink/dpink.drawio`
- `rt/rt.drawio`

Given the diagrams, it should be possible to create a kernel yourself. If you need to refer to existing code, look at `rt/0d.rt` and `rt/stock.rt` and `rt/shellout.rt`. Or, look at the kernel used for these demos `zd/kernel0d.py`. Caveat: the kernel used for these demos contains a fair amount of historical cruft that hasn't been culled. Zac Nowicki at Kagi.com has created several kernels from scratch. Zac (an I) can be contacted at the `programming simplicity` discord `https://discord.gg/65YZUh6Jpq` or by sending email to me at `ptcomputingsimplicity@gmail.com`. I found it easier to use a REPL when building the kernel - see `Miscallaneous` below.

# Output:
The final response (of 5) to the questions "Why is concurrency so difficult" is in `dpink.md`.

See `rt/out.py`, `rt/out.js` and `rt/out.lisp` for the generated kernels. (The sources are in rt/0d.rt, rt/stock.rt and rt/shellout.rt).

# Miscellaneous
If you want to try tweaking the kernel or want to try porting it to another language (say, Lua), use the REPL development environment. It is in a repo (https://github.com/guitarvydas/rt) which is not included here. See the README.md there and feel free to contact me.

