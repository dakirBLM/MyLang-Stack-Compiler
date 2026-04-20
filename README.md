# MyLang Stack Compiler

MyLang is a small imperative language implemented with a full compiler pipeline:
parse, type-check, code generation, and virtual machine execution.

## Highlights

- ANTLR grammar and generated parser.
- Static type checking with readable error messages.
- Stack-machine instruction generation.
- Interpreter runtime for compiled instructions.
- Stream support with append behavior via save.
- File output using fwrite.

## Language Features

- Types: int, float, bool, string, stream.
- Variables and assignment.
- Arithmetic: +, -, *, /, %.
- String concatenation: .
- Boolean logic: &&, ||, !.
- Comparisons: ==, !=, <, >, <=, >=.
- Control flow: if/else, while, blocks.
- I/O: read, write, fwrite.
- Stream operations:
  - a << expr; appends expr to stream a.
  - save a; appends current value of a into itself using VM stream-save semantics.

## Project Structure

- MyLang.g4: grammar source of truth.
- generated/: generated ANTLR lexer/parser/visitor.
- main.py: compile and run entrypoint.
- type_checker.py: semantic and type validation.
- code_generator.py: VM instruction emission.
- interpreter.py: stack VM execution engine.
- test files: sample and validation programs.

## Setup

Install runtime dependency:

```bash
pip install antlr4-python3-runtime==4.11.1
```

Regenerate parser files (requires Java and ANTLR tool):

```bash
ANTLR4_TOOLS_ANTLR_VERSION=4.11.1 antlr4 -Dlanguage=Python3 -visitor -o generated MyLang.g4
```

If antlr4 is not available in PATH, activate your virtual environment first.

## Usage

Compile source to VM instructions:

```bash
python3 main.py compile test1.ml
```

Compile and run:

```bash
python3 main.py run test1.ml
```

Run with input file:

```bash
python3 main.py run test_read.ml input.txt
```

Interpret precompiled instruction text:

```bash
python3 main.py interp program.instr
```

## Pipeline Overview

1. Parser builds a parse tree from source text.
2. Type checker validates declarations, operations, and control-flow conditions.
3. Code generator emits stack-machine instructions.
4. Interpreter executes instructions and returns output lines.

## Stream and File Output Notes

- Stream variables are tracked at runtime.
- save <name> appends stack value when name is a stream.
- fwrite expects two values on stack:
  1. value to write
  2. output filename string

## Suggested Tests

- test_errors.ml for semantic error reporting.
- test_complex.ml for control flow.
- test_exam.ml for stream, save, and fwrite behavior.

