from .services.configuration_manager import ConfigurationManager
from src.gui.gui_manager import GUIManager

GUI = GUIManager()
PROGRAM_NAME = ConfigurationManager().program_name
PROGRAM_AUTHOR = ConfigurationManager().program_author
PROGRAM_VERSION = ConfigurationManager().program_version


def run():
    from .core.dvr_viewer import DVRViewer
    app = DVRViewer()
    app.start()
