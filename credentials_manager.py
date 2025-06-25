import keyring


class CredentialsManager:
    def __init__(self, service_name):
        self.service_name = service_name

    def set_credential(self, username, value):
        keyring.set_password(self.service_name, username, value)

    def get_credential(self, username):
        return keyring.get_credential(self.service_name, username)

    def delete_credential(self, username):
        keyring.delete_password(self.service_name, username)
