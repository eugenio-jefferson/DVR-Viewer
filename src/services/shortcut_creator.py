import sys
import os
from pathlib import Path


class ShortcutCreator:
    def __init__(self, program_name: str, executable_path: Path, icon_directory_path: Path, program_version: str):
        self.PROGRAM_NAME = program_name
        self.executable_path = executable_path
        self.icon_directory_path = icon_directory_path
        self.PROGRAM_VERSION = program_version

    def create_shortcut(self):
        if sys.platform.startswith("linux"):
            self._create_shortcut_in_linux()

        elif sys.platform.startswith("win"):
            self._create_shortcut_in_windows()

        else:
            raise OSError(
                f"O sistema operacional '{sys.platform}' não é suportado.")

    def _create_shortcut_in_linux(self):
        application_directory = Path.home() / ".local/share/applications"
        shortcut_path = application_directory / f"{self.PROGRAM_NAME}.desktop"

        os.makedirs(application_directory, exist_ok=True)

        shortcut_file_content = f"""
[Desktop Entry]
Version={self.PROGRAM_VERSION}
Type=Application
Name={self.PROGRAM_NAME}
Comment=Wizard to quickly view cameras on the Intelbras DVR
Comment[pt_BR]=Assistente para visualizar rapidamente as câmeras no DVR Intelbras
Exec="{self.executable_path}"
Icon={self.icon_directory_path / "icon.png"}
Type=Application
Categories=Utility;
Terminal=false
"""
        with open(shortcut_path, 'w') as shortcut:
            shortcut.write(shortcut_file_content.strip())
        os.chmod(shortcut_path, 0o755)

    def _create_shortcut_in_windows(self):
        import win32com.client
        
        start_menu_directory = Path.home(
        ) / "AppData/Roaming/Microsoft/Windows/Start Menu/Programs" / self.PROGRAM_NAME
        shortcut_path = start_menu_directory / f"{self.PROGRAM_NAME}.lnk"

        os.makedirs(start_menu_directory, exist_ok=True)
        
        shell = win32com.client.Dispatch("WScript.Shell")
        shortcut = shell.CreateShortCut(str(shortcut_path))

        shortcut.TargetPath = str(self.executable_path)
        shortcut.IconLocation = str(self.icon_directory_path / "icon.ico")
        shortcut.Description = "Assistente para visualizar rapidamente as câmeras no DVR Intelbras"

        shortcut.Save()
