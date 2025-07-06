import sys
import os
import shutil
import platformdirs
from pathlib import Path
from src import run, PROGRAM_NAME, PROGRAM_AUTHOR, PROGRAM_VERSION, GUI
from src.services.shortcut_creator import ShortchutCreator


CURRENT_FILE_PATH = Path(sys.argv[0]).resolve()
CORRECT_FILE_PATH = Path(platformdirs.user_data_dir(
    PROGRAM_NAME, PROGRAM_AUTHOR)) / CURRENT_FILE_PATH.name
CORRECT_ASSETS_DIRECTORY = CORRECT_FILE_PATH.parent / "assets"


def main():
    try:
        if CURRENT_FILE_PATH != CORRECT_FILE_PATH:
            create_files_in_correct_location()

            ShortchutCreator(
                PROGRAM_NAME,
                CORRECT_FILE_PATH,
                CORRECT_ASSETS_DIRECTORY,
                PROGRAM_VERSION
            ).create_shortcut()

            GUI.show_info(
                "O DVR Viewer foi instaldo.\n\nAbra o DVR Viewer no menu do seu sistema operacional.")
        else:
            run()

    except Exception as exception:
        GUI.show_error(f"Ocorreu o erro:\n{exception}")


def create_files_in_correct_location():
    os.makedirs(CORRECT_FILE_PATH.parent, exist_ok=True)
    shutil.copy2(CURRENT_FILE_PATH, CORRECT_FILE_PATH)

    assets_directory = Path(sys.executable).parent / "assets"

    if CORRECT_ASSETS_DIRECTORY.exists():
        shutil.rmtree(CORRECT_ASSETS_DIRECTORY)

    shutil.copytree(assets_directory, CORRECT_ASSETS_DIRECTORY)


if __name__ == "__main__":
    main()
