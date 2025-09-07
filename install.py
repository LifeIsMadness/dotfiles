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


def install() -> None:
    COPY_DIR.mkdir(exist_ok=True)
    for df_name in DOTFILES:
        f_path_home = HOME_DIR / df_name

        if f_path_home.is_dir():
            print(f"{f_path_home} is a dir")
            continue

        backup_existing_dotfile(df_name, f_path_home)
        create_symlink(df_name, f_path_home)


def create_symlink(df_name: str, f_path_home: Path):
    f_path_curr = CURRENT_DIR / df_name
    try:
        f_path_home.symlink_to(f_path_curr)
    except Exception as e:
        print(e)
    else:
        print(f"Created symlink {f_path_home} for {f_path_curr}")


def backup_existing_dotfile(df_name: str, f_path_home: Path) -> None:
    f_path_copy = COPY_DIR / (df_name + ".copy")
    try:
        f_path_home.rename(f_path_copy)
    except FileNotFoundError:
        print(f"File {f_path_home} not found")
    except Exception as e:
        print(e)
    else:
        print(f"{f_path_home} moved to {f_path_copy}")


if __name__ == "__main__":
    if Path(__file__).resolve().parent != CURRENT_DIR:
        print("You should run install.py within the same dir")
    else:
        install()
