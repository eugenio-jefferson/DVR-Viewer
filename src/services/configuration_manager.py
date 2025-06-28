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
                'version': '1.0'
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

    @property
    def program_name(self):
        return self.settings['program_data'].get('name')

    @property
    def dvr_url(self):
        return self.settings['user_data'].get('dvr_url')

    @dvr_url.setter
    def dvr_url(self, value):
        self.settings['user_data']['dvr_url'] = value
        self.save_config()

    @property
    def exists_dvr_url(self):
        return self.dvr_url != None and self.dvr_url != ""

    @property
    def last_username(self):
        return self.settings['user_data'].get('last_username')

    @last_username.setter
    def last_username(self, value):
        self.settings['user_data']['last_username'] = value
        self.save_config()

    @property
    def exists_last_username(self):
        return self.last_username is not None and self.last_username != ""

    @property
    def channel_numbers(self):
        return self.settings['user_data'].get('channel_numbers')

    @channel_numbers.setter
    def channel_numbers(self, value):
        self.settings['user_data']['channel_numbers'] = value
        self.save_config()

    @property
    def exists_channel_numbers(self):
        return self.channel_numbers is not None and self.channel_numbers > 0

    def save_config(self):
        try:
            with open(self.config_file_path, 'w', encoding='utf-8') as file:
                json.dump(self.settings, file, indent=4)

        except Exception as e:
            print(f"Exception in save_config: {e}")

    def load_config(self):
        if self.is_empty:
            print("Config file is empty or does not exist.")
        
        app_version = self._shared_state['settings']['program_data']['version']
        
        try:
            with open(self.config_file_path, 'r', encoding='utf-8') as file:
                self.settings = json.load(file)
            
            if self.settings['program_data']['version'] != app_version:
                self.settings['program_data']['version'] = app_version
                self.save_config()
        except Exception as e:
            print(f"Exception in load_config: {e}")
