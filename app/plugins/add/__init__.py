import sys
from app.commands import Command


class AddCommand(Command):
    def execute(self, *args):
        if len(args) != 2:
            print("Require exact two arguments")
            return
        try:
            numbers = map(float, args)
            print(round(sum(numbers), 1))
        except ValueError:
            print("Error: All arguments must be numeric")
