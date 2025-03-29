# Various demos of 0D
### hello world
- simple "Hello World" example
- 7 examples of various ways to express parallelism and order of operation
### arith 
- a simple expression grammar compiled to Python, Javascript, Common Lisp, WASM (WAT?) all at once

### dpink 
- an LLM experiment based on Daniel Pink's advice to ask the question "Why?" 5 times

### 0d kernel 
- written in rt and compiled to Python, Javascript, Common Lisp

### Larson scanner running in a browser
- used generated code for the components

# Usage:
./make.bash

# Source Code
## Hello World

![](hello-world/hello-world-nondeterministic.drawio.png)
## 

## Arith
![](arith/arith-main.drawio.png)



## LLM (Daniel Pink LLM)

![](dpink/dpink.drawio.png)


## RT (0D Kernel Source)
![](rt/rt-main.drawio.png)



## Larson Scanner (in a browser)

### Code Generator
![](html-larson/code-generator-main.drawio.png)



### Larson Scanner
#### top level (main)
![](html-larson/scanner-main.drawio.png)

#### main body (Larson)
![](html-larson/scanner-Larson.drawio.png)



## Source File Paths
I think that the drawware source code is more important than the 0D kernel source code (the Python version is used in these examples).

The source code for the examples is in .drawio files, i.e. 
- `hello-world/hello-world.drawio`
- `arith/arith0d.drawio`
- `dpink/dpink.drawio`
- `rt/rt.drawio`
- The Larson scanner code is in `html-larson/scanner.drawio` and the code-generator is in `html-larson/code-generator.drawio`

Given the diagrams, it should be possible to create a kernel yourself. If you need to refer to textual code, look at `rt/0d.rt` and `rt/stock.rt` and `rt/shellout.rt`. Or, look at the kernel used for these demos `zd/kernel0d.py`. Caveat: the kernel used for these demos contains a fair amount of historical cruft that hasn't been culled. Zac Nowicki at Kagi.com has created several kernels from scratch in various programming languages (Go, Crystal, Odin). Zac (and I) can be contacted at the `programming simplicity` discord `https://discord.gg/65YZUh6Jpq` or by sending email to me at `ptcomputingsimplicity@gmail.com`. I found it easier to use a REPL when building the kernel - see `Miscellaneous` below.

# Details:
## Hello World
Output is directly sent to the console. You should see 7 JSON arrays containing mevents - a string key and a string value. 
1. The first response is nondeterministic. It might be `[{"" : "Hello"},{"" : "World"}]` or `[{"" : "World"},{"" : "Hello"}]` depending on the actual implementation of the kernel. In each of these cases, the Key is the empty string `""` and the value is the second string. The code is found on the tab `nondeterministic` in `hello-world/hello-world.drawio`.
2. The second output is deterministic ensuring that "World" is sent out before "Hello". The code is in tab `seq1` of `hello-world/hello-world.drawio`.
3. The third output is deterministic ensuring that "Hello" is sent out before "World". The code is in tab `seq2` of `hello-world/hello-world.drawio`.
4. The fourth output sends 3 messages {"" : "Hello"}, {"" : "Cruel"}, {"" : "World"} and demonstrates one possible way to get deterministic behaviour using a de-racer component called `1then2` (essentially a 2-input sequencer).  Two copies of `1then2` are used to express *very explicit* ordering. The code is in tab `seq3` of `hello-world/hello-world.drawio`. The de-racer `1then2` is implemented in the host language and is fairly trivial. The code uses a state-based approach to check which input is being fired, in what order. The code uses a simple buffer to hold incoming messages and re-output them in the correct order. This part is especially easy to write using a garbage-collected language, but, could be implemented in a non-GC language.
5. The code in tab `seq3a` shows the same diagram redrawn to look neater (to my eyes).
6. The code in tab `seq4` another way to achieve determinism by placing the `1then2` Parts to the right of the `Hello`, `Cruel` and `World` Parts.
7. The code in tab `seq5` shows another way to achieve determinism without using any `1then2` Parts. The actual string messages are used as triggers for downstream components. Each component fans-out its output to the output and to the next stage in the pipeline. The of the downstream stages ignore the actual data and are triggered only by the arrival of the mevent from upstream. In the kernel code, we call this a *Bang* (in electronics, this is called *edge-triggered*)

Each of the versions demonstrate issues of human-readability and efficiency. The Software Architect, Software Engineer, and Software Production Engineer must choose the most appropriate method based on latencies and other factors. In contrast, a single, one-size-fits-all, general purpose solution cannot result in efficient code for all cases. The best approach is to document various approaches, while leaving the final implementation decision up to the Software Architect (and the rest of team).
### Usage
./make.bash

## Arith
This is a simple example of "compiling" VHLL code to multiple HLL languages at the same time.

This example code does "nothing".

If you want to see a full-blown implementation of this technique, see the "0D Kernel Written In VHLL RT" below. Recommendation: don't bother looking at the 0D Kernel code implementation until you understand what this simple `arith` example does.

The `arith` grammar is borrowed from the stock example that comes with OhmJS.

### Usage
./make.bash

## Daniel Pink LLM
Daniel Pink recommends, in [Masterclass](https://www.youtube.com/watch?v=My7hjBp4wH0), that, to determine the _real_ problem, one shoud dig into issues by asking "Why ... ?" at least 5 times.

I slapped together a feedback loop using two instances of LLM components and a bit of Python code that counts to 5, to prompt an LLM then re-prompt the main LLM 5 more times after extracting the main issue described in response to the previous response.

Unlike recursion, which uses stacks, feedback uses queues. The difference can be described by analogy. Imagine a line of people waitint to buy tickets for a movie at the ticket window. Recursion means that someone gets to cut to the front of the line without waiting their turn, while queueing means that people have to go to the end of the line and wait their turn.

The 6 responses to the question "Why is concurrency so difficult" are in `dpink/out.md`. The dpink LLM code uses two instances of the LLM component. The original prompt enters the system and a response is generated by the 1st LLM. The response is fed back to another LLM which extracts the main issue and asks "Why?" five more times. All of the 5+1 responses are gathered, in order of generation in `dpink/out.md`.

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
