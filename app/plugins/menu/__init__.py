import sys
from app.commands import Command

class MenuCommand(Command):
    def execute(self):
        print("\n\n:: Plugins Instructions ::")
        print("Plugin Menu - menu")
        print("Addition - add <number> <number>")
        print("Subtraction - sub <number> <number>")
        print("Multiplication - multi <number> <number>")
        print("Division - div <number> <number>")
        print("Exit - exit\n\n")