'''
Class   : DAAA/FT/2B03
Member 1: Ethan Tan (P2012085)
Member 2: Reshma    (P2011972)

'''
import os


# Clears the terminal output (emulates refreshing a window)
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


# Retrieves input from the user which spans multiple lines
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


# Loads an arbitrary configuration file
def load_config(config_file: str, default_config):
    if os.path.exists(config_file):
        with open(file=config_file, mode='r') as f:
            config = f.read().rstrip().splitlines()
            return (*config, *default_config[len(config):])
    return default_config
