from colorama import Fore, Style
from pathlib import Path

def print_tree(path, indent=''):
    if path.is_file():
        print(indent + Fore.RED + path.name + Style.RESET_ALL)
    else:
        print(indent + Fore.BLUE + path.name + Style.RESET_ALL)
        for child in path.iterdir():
            print_tree(child, indent + '  ')


# print root project folder tree
print_tree(Path('.'))