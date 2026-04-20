#!/usr/bin/env python3
"""
MyLang Compiler + Interpreter
Usage:
  python main.py compile <source.ml>              # compile only, print code
  python main.py run     <source.ml>              # compile + run
  python main.py run     <source.ml> <input.txt>  # compile + run with input file
  python main.py interp  <code.instr>             # interpret existing instruction file
  python main.py interp  <code.instr> <input.txt>
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'generated'))

from antlr4 import CommonTokenStream, InputStream, BailErrorStrategy
from antlr4.error.ErrorListener import ErrorListener
from antlr4.error.Errors import ParseCancellationException

from MyLangLexer  import MyLangLexer
from MyLangParser import MyLangParser

from type_checker    import TypeChecker
from code_generator  import CodeGenerator
from interpreter     import run_interpreter


# ── Custom error listener that collects syntax errors ──────────────────────

class SyntaxErrorCollector(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.errors.append(f"Syntax error at line {line}:{column} - {msg}")


def compile_source(source_text):
    """
    Parse + type-check + generate code.
    Returns (code_string, None) on success, or (None, [errors]) on failure.
    """
    # ── Phase 1: Parsing ──────────────────────────────────────────────────
    input_stream = InputStream(source_text)
    lexer        = MyLangLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser       = MyLangParser(token_stream)

    error_listener = SyntaxErrorCollector()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.program()

    if error_listener.errors:
        return None, error_listener.errors

    # ── Phase 2: Type checking ───────────────────────────────────────────
    checker = TypeChecker()
    checker.visit(tree)

    if checker.errors:
        return None, checker.errors

    # ── Phase 3: Code generation ─────────────────────────────────────────
    generator = CodeGenerator(checker.variables)
    generator.visit(tree)

    return generator.get_code(), None


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        print(__doc__)
        sys.exit(1)

    mode = args[0]

    # ── Interpret a pre-compiled instruction file ─────────────────────────
    if mode == 'interp':
        code_file  = args[1]
        input_file = args[2] if len(args) > 2 else None
        with open(code_file) as f:
            code = f.read()
        input_lines = None
        if input_file:
            with open(input_file) as f:
                input_lines = f.read().splitlines()
        result = run_interpreter(code, input_lines)
        if result:
            print(result)
        return

    # ── Compile (and optionally run) a source file ────────────────────────
    source_file = args[1]
    with open(source_file) as f:
        source = f.read()

    code, errors = compile_source(source)

    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        sys.exit(1)

    if mode == 'compile':
        print(code)

    elif mode == 'run':
        input_file = args[2] if len(args) > 2 else None
        input_lines = None
        if input_file:
            with open(input_file) as f:
                input_lines = f.read().splitlines()
        result = run_interpreter(code, input_lines)
        if result:
            print(result)

    else:
        print(f"Unknown mode: {mode}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
