import sys
from pathlib import Path
from colorama import Fore, Back, Style

def log_error_message(message: str) -> None:
  print(f"{Back.RED}{Fore.WHITE}[ERROR]{Fore.RED}{Back.RESET}: {message}{Style.RESET_ALL}")

def print_folder(name: str, indent: str) -> None:
  print(f"{indent}🗂️ {Fore.BLUE}{name}/{Style.RESET_ALL}")

def print_file(name: str, indent: str) -> None:
  print(f"{indent}{Style.DIM}📑{Style.RESET_ALL} {Fore.LIGHTBLUE_EX}{name}{Style.RESET_ALL}")

def print_folder_structure(path: Path, depth = 0) -> None:
  indent = "  " * depth
  if path.is_file():
    print_file(path.name, indent)
    return

  print_folder(path.name, indent)

  for inner_path in path.iterdir():
    print_folder_structure(inner_path, depth + 1)

def show_directory_structure() -> None:
  if len(sys.argv) <= 1:
    log_error_message("The directory path was not passed. Please pass the path.")
    return

  root_path = Path(sys.argv[1])

  if not root_path.exists():
    log_error_message("The directory path is incorrect.")
    return

  if not root_path.is_dir():
    log_error_message("The path is not a dir. Please pass the dir path.")
    return

  print_folder_structure(root_path)

if __name__ == "__main__":
  show_directory_structure()
