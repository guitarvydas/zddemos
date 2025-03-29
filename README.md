# Various demos of 0D
### hello world
- simple "Hello World" example
- 7 examples of various ways to express parallelism and order of operation
### arith 
- a simple expression grammar compiled to Python, Javascript, Common Lisp, WASM (WAT?) all at once

### dpink 
- an LLM experiment based on Daniel Pink's advice to repeatedly ask the question "Why?" 5 times

### 0d kernel 
- written in `rt` and compiled to Python, Javascript, Common Lisp

### Larson scanner running in a browser
- uses generated code for the components

## notes
The `kernel` and `scanner` examples contain the most code, but, the `dpink` LLM example stands out as shining example of how easily ideas can be realized, when thinking this way.

The `hello-world` and `arith` examples are good warm-ups, but, are geared towards simple examples of the techniques instead of being something practical.
# Usage:
./make.bash

# Source Code

The source code for these examples uses a syntax that is more modern than ASCII. To edit and view the actual source code, use [draw.io](https://app.diagrams.net). Caveat: draw.io is meant for editing diagrams and not source code, but, it's one of the best editors I've found for this kind of thing. I would hope that, in the future, someone will create a code editor that uses graphML/XML/SVG/??? instead of just using 1960s style grids of non-overlapping pixmaps (called "characters"), but, that doesn't exist yet, to the best of my knowledge.
## Hello World

![](hello-world/hello-world-nondeterministic.drawio.svg)

## Arith

![](arith/arith-main.drawio.svg)

## LLM (Daniel Pink LLM)

![](dpink/dpink.drawio.svg)

## RT (0D Kernel Source)

![](rt/rt-main.drawio.svg)


## Larson Scanner (in a browser)

### Code Generator


![](html-larson/code-generator-main.drawio.svg)

### Larson Scanner
#### top level (main)
![](html-larson/scanner-main.drawio.svg)

#### main body (Larson)

![](html-larson/scanner-Larson.drawio.svg)


## Source File Paths
I think that the drawware source code is more important than the 0D kernel source code (the Python version is used in these examples).

The source code for the examples is in .drawio files, i.e. 
- `hello-world/hello-world.drawio`
- `arith/arith0d.drawio`
- `dpink/dpink.drawio`
- `rt/rt.drawio`
- The Larson scanner code is in `html-larson/scanner.drawio` and the code-generator is in `html-larson/code-generator.drawio`

Given the diagrams, it should be possible to create a kernel yourself. If you need to refer to textual code, look at `rt/0d.rt` and `rt/stock.rt` and `rt/shellout.rt`. This would be akin to someone asking to see the assembler code emitted by a C compiler in the 1970s, or looking at the source code for an operating system. Additionally, you can look at the kernel used for these demos `zd/kernel0d.py`. Caveat: the kernel used for these demos contains a fair amount of historical cruft that hasn't been culled (I'm having more fun writing new code in DPL format (Diagrammatic Programming Language) rather than revisiting "assembler" code (written in `rt`)). The kernel is, itself, generated from `.rt` code (as witnessed by the line-number comments on just about every line which refer back to the original line numbers in the `.rt` code). Zac Nowicki at Kagi.com has created several kernels from scratch in various programming languages (Go, Crystal, Odin). Zac (and I) can be contacted at the `programming simplicity` discord `https://discord.gg/65YZUh6Jpq` or by sending email to me at `ptcomputingsimplicity@gmail.com`. I found it easier to use a REPL when building the kernel - see `Miscellaneous` below.

# Details:
When you run `./make.bash` from the top level directory of this project, you should see output from the 5 examples.
## Hello World
Output is directly sent to the console. You should see 7 JSON arrays containing mevents - a string key and a string value. 
1. The first response is nondeterministic. It might be `[{"" : "Hello"},{"" : "World"}]` or `[{"" : "World"},{"" : "Hello"}]` depending on the actual implementation of the kernel and on the whims of the code editor. In each of these cases, the Key is the empty string `""` and the value is the second string. The code for this example is found on the tab `nondeterministic` in `hello-world/hello-world.drawio`.
2. The second output is deterministic ensuring that "World" is sent out before "Hello". The code is in tab `seq1` of `hello-world/hello-world.drawio`.
3. The third output is deterministic ensuring that "Hello" is sent out before "World". The code is in tab `seq2` of `hello-world/hello-world.drawio`.
4. The fourth output sends 3 messages {"" : "Hello"}, {"" : "Cruel"}, {"" : "World"} and demonstrates one possible way to get deterministic behaviour using a de-racer component called `1then2` (essentially a 2-input sequencer).  Two copies of `1then2` are used to express *very explicit* ordering. The code is in tab `seq3` of `hello-world/hello-world.drawio`. The de-racer `1then2` is implemented in the host language and is fairly trivial. The code uses a state-based approach to check which input is being fired, in what order. The code uses a simple buffer to hold incoming messages and re-output them in the correct order. This part is especially easy to write using a garbage-collected language, but, could be implemented in a non-GC language.
5. The code in tab `seq3a` shows the same diagram redrawn to look neater, to my eyes. Notably, I tried to remove line crossings by judiciously renaming ports and repositioning them on the diagram (look at the positions of the 1 and 2 ports on the `1then2` Parts - the compiler doesn't care that the ports have been moved).
6. The code in tab `seq4` shows another way to achieve determinism by placing the `1then2` Parts to the right of the `Hello`, `Cruel` and `World` Parts. Note that the input from the white input gate is sent to each of the 3 string Parts. This is called "fan-out" and requires copying of mevents. This is especially easy when the host language contains implicit garbage collection. Production Engineers might want to tighten this code up (or might not want to do so) by performing some kind of explicit garbage collection or ownership tracking. This is an example of MVI - Minimum Viable Implementation. The Software Architect does the minimum amount of work to implement ideas. Later, the final design is punted to Production Engineers who assess the need (if any) for further optimization. MVI differs from MVP, in that MVI skimps on "efficiency" while MVP skimps on "product features". The historical technique of "RAD" - Rapid Application Development - was similar to MVI.
7. The code in tab `seq5` shows another way to achieve determinism without using any `1then2` Parts. The actual string messages are used only as triggers for downstream components. Each component fans-out its output to, both, the output and to the next stage in the pipeline. The  downstream stages ignore the actual data and are triggered only by the arrival of the mevent from upstream. In the kernel code, we call this a *Bang* (in electronics, this is called *edge-triggered*).

Each of the versions demonstrate issues of human-readability and efficiency. The Software Architect, Software Engineer, and Software Production Engineer must choose the most appropriate method based on latencies and other factors. In contrast, a single, one-size-fits-all, general purpose solution cannot result in efficient code for all use-cases. The best approach is to document various approaches, while leaving the final implementation decision up to the Software Architect (and the rest of team).
### Usage
./make.bash

## Arith
This is a simple example of "compiling" VHLL code to multiple HLL languages at the same time.

This code generated by this example does "nothing".

If you want to see a full-blown practical use of this technique, see the "0D Kernel Written In VHLL RT" below. Recommendation: don't bother looking at the 0D Kernel code implementation until you understand what this simple `arith` example does.

The `arith` grammar is borrowed from the stock example that comes with [OhmJS](ohmjs.org).

### Usage
./make.bash

## Daniel Pink LLM
Daniel Pink recommends, in [Masterclass](https://www.youtube.com/watch?v=My7hjBp4wH0), that, to determine the _real_ problem, one should dig into issues by repeatedly asking "Why ... ?" at least 5 times.

I slapped together a feedback loop using two instances of an LLM component and a bit of Python code that counts to 5, to prompt an LLM, then re-prompt the main LLM 5 more times after extracting the main issue described in response to the previous response. Aside: this is an example of how 0D encourages freedom of thought - it was easy to imagine using the same LLM Part twice, when the concept of an LLM was abstracted down into a single Part. It was easy to create the source code for this using simple edit operations like COPY/PASTE. The LLM Parts lean on little Bash scripts to invoke the *agency* LLM CLI. I could have done this in different ways, but, thought that this looked simple enough for the purposes of this example.

Unlike recursion, which uses stacks, feedback uses queues. The difference can be described by analogy. Imagine a line of people waiting to buy tickets for a movie at the ticket window. Recursion means that someone gets to cut to the front of the line without waiting their turn, while queueing means that people have to go to the end of the line and wait their turn.

The 6 (5+1) responses to the question "Why is concurrency so difficult?" are in `dpink/out.md`. The dpink LLM code uses two instances of the LLM component. The original prompt enters the system and a response is generated by the 1st LLM. The response is fed back to another LLM which extracts the main issue and asks "Why?" five more times. All of the 5+1 responses are gathered, in order of generation in `dpink/out.md`.

### Usage
./make.bash

## 0D Kernel Written in VHLL "RT".
See `rt/out.py`, `rt/out.js` and `rt/out.lisp` for the generated kernels. (The sources are in rt/0d.rt, rt/stock.rt and rt/shellout.rt).

### Usage
./make.bash

## Larson Scanner
The generated JS code is in `html-larson/out.js`. When you load `html-larson/leds.html` into a browser, the generated code is load via a <script ...> ...  </script> element. The Larson scanner runs for a while, then stops.

### Usage
./make.bash

# Miscellaneous
If you want to try tweaking the kernel or want to try porting it to another language (say, Lua), use the REPL development environment. It is in a repo (https://github.com/guitarvydas/rt) which is not included here. See the README.md there and feel free to contact me.
