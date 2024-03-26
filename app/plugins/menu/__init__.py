import sys
from app.commands import Command

class DisplayMenu(Command):
    def __init__(self, command_handler):
        self.command_handler = command_handler

    def execute(self):
        menu_list = self.command_handler.menu_list()
        print("menu", list(menu_list))



