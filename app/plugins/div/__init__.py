import sys
from app.commands import Command


class DivCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            print("Require exact two arguments")
            return
        if float(args[1]) == 0:
            print("Can't division by zero")
            return
        result = float(args[0]) / float(args[1])
        print(round(result, 1))
