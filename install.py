import os
from pathlib import Path

DOTFILES = (
    ".tmux.conf",
    ".vimrc",
    ".zshrc",
)

# DOTFILES = (".yarnrc",)
HOME_DIR = Path.home()
CURRENT_DIR = Path.cwd()
COPY_DIR = HOME_DIR / "dotfiles-copy"


def install():
    COPY_DIR.mkdir(exist_ok=True)
    for f in DOTFILES:
        f_path_home = HOME_DIR / f
       
        if f_path_home.is_dir():
            print(f"{f_path_home} is a dir.")
            continue

        f_path_curr = CURRENT_DIR / f
        f_path_copy = COPY_DIR / (f + ".copy")
        try:
            f_path_home.rename(f_path_copy)
        except FileNotFoundError:
            print(f"File {f_path_home} not found")
        except Exception as e:
            print(e)
        else:
            print(f"{f_path_home} moved to {f_path_copy}")

        try:
            f_path_home.symlink_to(f_path_curr)
        except Exception as e:
            print(e)
        else:
            print(f"Created symlink {f_path_home} for {f_path_curr}")

if __name__ == "__main__":
    if Path(__file__).resolve().parent != Path.cwd():
        print(f"You should run install.py within the same dir")
    else:
        install()
