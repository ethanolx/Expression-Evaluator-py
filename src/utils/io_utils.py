import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def multiline_input(prompt: str):
    lines = []
    print(prompt)
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    return '\n'.join(lines)
