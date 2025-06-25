import os
import platformdirs
from pathlib import Path
import json


class ConfigurationManager:
    _shared_state = {}
    _shared_state.setdefault(
        'settings', {
            'user_data': {
            },
            'program_data': {
                'name': 'DVR-Viewer',
                'author': 'Eugenio Jefferson',
                'version': 'alpha 1.0'
            },
        }
    )
    config_dir_path = Path(platformdirs.user_config_dir(
        _shared_state['settings']['program_data']['name'],
        _shared_state['settings']['program_data']['author']))

    def __init__(self):
        self.__dict__ = self._shared_state

        self._ensure_directory_exists()

        if self.is_empty:
            self.save_config()
        else:
            self.load_config()

    def _ensure_directory_exists(self):
        os.makedirs(self.config_dir_path, exist_ok=True)

    @property
    def config_file_path(self):
        return self.config_dir_path / "config.json"

    @property
    def is_empty(self):
        return not self.config_file_path.exists() or os.path.getsize(self.config_file_path) == 0

    def save_config(self):
        try:
            with open(self.config_file_path, 'w', encoding='utf-8') as file:
                json.dump(self.settings, file, indent=4)

        except Exception as e:
            print(f"Exception in save_config: {e}")

    def load_config(self):
        if self.is_empty:
            print("Config file is empty or does not exist.")

        try:
            with open(self.config_file_path, 'r', encoding='utf-8') as file:
                self.settings = json.load(file)

        except Exception as e:
            print(f"Exception in load_config: {e}")
