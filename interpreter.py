import sys


def _format_value(value):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if isinstance(value, float):
        if value == int(value):
            return f'{value:.1f}'
        return str(value)
    return str(value)

def run_interpreter(code_text, input_lines=None):
    """
    Execute stack-based instruction code.
    code_text: string of instructions
    input_lines: list of strings for stdin (or None to use real stdin)
    """
    lines = [l.strip() for l in code_text.strip().splitlines() if l.strip()]

    # Build label map: label_number -> instruction index
    label_map = {}
    instructions = []
    for line in lines:
        parts = line.split()
        if parts[0] == 'label':
            label_map[int(parts[1])] = len(instructions)
        instructions.append(parts)

    stack = []
    variables = {}
    stream_vars = set()
    pc = 0
    input_iter = iter(input_lines) if input_lines is not None else None

    def read_input():
        if input_iter is not None:
            return next(input_iter)
        return sys.stdin.readline().rstrip('\n')

    output_parts = []

    while pc < len(instructions):
        parts = instructions[pc]
        op = parts[0]
        pc += 1

        if op == 'push':
            T = parts[1]
            val_str = ' '.join(parts[2:])
            if T == 'I':
                stack.append(int(val_str))
            elif T == 'F':
                stack.append(float(val_str))
            elif T == 'B':
                stack.append(val_str == 'true')
            elif T == 'S':
                # strip surrounding quotes, handle escape sequences
                s = val_str
                if s.startswith('"') and s.endswith('"'):
                    s = s[1:-1]
                s = s.replace('\\n', '\n').replace('\\t', '\t').replace('\\"', '"').replace('\\\\', '\\')
                stack.append(s)

        elif op == 'pop':
            stack.pop()

        elif op == 'load':
            name = parts[1]
            stack.append(variables[name])

        elif op == 'save':
            name = parts[1]
            value = stack.pop()
            if name in stream_vars:
                variables[name] = str(variables.get(name, '')) + _format_value(value)
            else:
                variables[name] = value

        elif op == 'mkstream':
            name = parts[1]
            stream_vars.add(name)
            variables[name] = ''

        elif op == 'add':
            T = parts[1]
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)

        elif op == 'sub':
            T = parts[1]
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)

        elif op == 'mul':
            T = parts[1]
            b, a = stack.pop(), stack.pop()
            stack.append(a * b)

        elif op == 'div':
            T = parts[1]
            b, a = stack.pop(), stack.pop()
            if T == 'I':
                stack.append(int(a / b))
            else:
                stack.append(a / b)

        elif op == 'mod':
            b, a = stack.pop(), stack.pop()
            stack.append(a % b)

        elif op == 'uminus':
            a = stack.pop()
            stack.append(-a)

        elif op == 'concat':
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)

        elif op == 'append':
            rhs, lhs = stack.pop(), stack.pop()
            stack.append(str(lhs) + _format_value(rhs))

        elif op == 'and':
            b, a = stack.pop(), stack.pop()
            stack.append(a and b)

        elif op == 'or':
            b, a = stack.pop(), stack.pop()
            stack.append(a or b)

        elif op == 'not':
            a = stack.pop()
            stack.append(not a)

        elif op == 'gt':
            b, a = stack.pop(), stack.pop()
            stack.append(a > b)

        elif op == 'lt':
            b, a = stack.pop(), stack.pop()
            stack.append(a < b)

        elif op == 'eq':
            b, a = stack.pop(), stack.pop()
            stack.append(a == b)

        elif op == 'itof':
            a = stack.pop()
            stack.append(float(a))

        elif op == 'label':
            pass  # already handled in preprocessing

        elif op == 'jmp':
            n = int(parts[1])
            pc = label_map[n]

        elif op == 'fjmp':
            n = int(parts[1])
            cond = stack.pop()
            if not cond:
                pc = label_map[n]

        elif op == 'print':
            n = int(parts[1])
            # Pop n items — they are in order on stack (first pushed = deepest)
            items = stack[-n:]
            stack = stack[:-n]
            output_parts.append(''.join(_format_value(item) for item in items))

        elif op == 'fwrite':
            filename = stack.pop()
            value = stack.pop()
            with open(str(filename), 'w') as handle:
                handle.write(_format_value(value))

        elif op == 'read':
            T = parts[1]
            raw = read_input()
            if T == 'I':
                stack.append(int(raw))
            elif T == 'F':
                stack.append(float(raw))
            elif T == 'B':
                stack.append(raw.strip() == 'true')
            elif T == 'S':
                stack.append(raw)

        else:
            raise RuntimeError(f"Unknown instruction: {op}")

    return '\n'.join(output_parts)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python interpreter.py <code_file> [input_file]")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        code = f.read()
    input_lines = None
    if len(sys.argv) >= 3:
        with open(sys.argv[2]) as f:
            input_lines = f.read().splitlines()
    result = run_interpreter(code, input_lines)
    if result:
        print(result)
