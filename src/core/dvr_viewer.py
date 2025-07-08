from src.services.configuration_manager import ConfigurationManager
from src.services.credentials_manager import CredentialsManager
from src.gui.gui_manager import GUIManager


class DVRViewer:
    def __init__(self):
        self.gui = GUIManager()
        self._configuration_manager = ConfigurationManager()
        self._credentials_manager = CredentialsManager(
            self._configuration_manager.program_name)

    def start(self):
        from src.core.automation import Automation
        import asyncio
        from playwright._impl._errors import TargetClosedError

        self.validate_data()

        automation = Automation(
            self._configuration_manager.dvr_url,
            self._configuration_manager.last_username,
            self._credential.password,
            self._configuration_manager.channel_numbers
        )

        del self._credential

        try:
            asyncio.run(automation.run())

        except ValueError as exception:
            self.gui.show_error(f"{exception}")

            self._credentials_manager.delete_credential(
                self._configuration_manager.last_username)
            self._configuration_manager.last_username = None

        except TargetClosedError as exception:
            self.gui.show_error(
                "Verifique se o URL é válido e se está acessível.")

        except Exception as exception:
            self.gui.show_error(f"Erro ao iniciar a automação: {exception}")

        finally:
            del automation
            del self.__dict__

    def validate_data(self):
        if not self._configuration_manager.exists_dvr_url:
            self.request_url()

        if not self._configuration_manager.exists_last_username:
            self.request_username()

        self._credential = self._credentials_manager.get_credential(
            self._configuration_manager.last_username)

        if self._credential is None:
            self.request_password()

        self._credential = self._credentials_manager.get_credential(
            self._configuration_manager.last_username)

        if not self._configuration_manager.channel_numbers:
            self.request_channel_numbers()

    def request_url(self):
        response = self.gui.request_an_string(
            "Insira a URL de login do DVR:",
            self._configuration_manager.dvr_url
        )

        if response is not None and response.strip() != "":
            self._configuration_manager.dvr_url = response.strip()

        else:
            raise ValueError("URL de login do DVR não informada.")

    def request_username(self):
        response = self.gui.request_an_string(
            "Insira o seu nome de usuário do DVR:",
            self._configuration_manager.last_username
        )

        if response is not None and response.strip() != "":
            self._configuration_manager.last_username = response.strip()

        else:
            raise ValueError("Nome de usuário não informado.")

    def request_password(self):
        response = self.gui.request_password("Insira a sua senha do DVR:")

        if response is not None:
            self._credentials_manager.set_credential(
                self._configuration_manager.last_username,
                response.strip()
            )

        else:
            raise ValueError("Senha não informada.")

    def request_channel_numbers(self):
        response = self.gui.request_an_integer(
            "Insira a quantidade de canais para visualização:",
            self._configuration_manager.channel_numbers
        )

        if response is not None and response > 0:
            self._configuration_manager.channel_numbers = response

        else:
            raise ValueError("Quantidade de canais é inválida.")
