import sys
from app.commands import Command


class SubCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            print("Require exact two arguments")
            return
        result = float(args[0]) - float(args[1])
        print(round(result, 1))
