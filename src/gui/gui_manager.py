import tkinter as tk
from tkinter import messagebox, simpledialog


class GUIManager:
    _shared_state = {}
    _shared_state.setdefault('root', tk.Tk())
    _shared_state['root'].withdraw()

    def __init__(self, program_name= "DVR Viewer"):
        self.__dict__ = self._shared_state
        self.PROGRAM_NAME = program_name

    def show_info(self, message):
        messagebox.showinfo(
            title=self.PROGRAM_NAME,
            message=message
        )

    def show_error(self, message):
        messagebox.showerror(
            title=f"{self.PROGRAM_NAME}  -  Erro",
            message=message + "\n\nO programa será encerrado."
        )

    def request_an_integer(self, message, initial_value=None):
        return simpledialog.askinteger(
            title=self.PROGRAM_NAME,
            prompt=message,
            initialvalue=initial_value
        )

    def request_an_string(self, message, initial_value=None):
        return simpledialog.askstring(
            title=self.PROGRAM_NAME,
            prompt=message,
            initialvalue=initial_value
        )

    def request_password(self, message):
        return simpledialog.askstring(
            title=self.PROGRAM_NAME,
            prompt=message,
            show="*"
        )
