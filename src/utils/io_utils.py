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


def load_config(config_file: str, default_config):
    with open(file=config_file, mode='r') as f:
        config = f.read().splitlines()
        return (*config, *default_config[len(config):])
