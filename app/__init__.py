import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command
from app.plugins.menu import MenuCommand

class App:
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):  # Assuming a BaseCommand class exists
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore
    def start(self):
        # Register commands here
        self.load_plugins()
        self.command_handler.execute_command('menu')
        while True:  #REPL Read, Evaluate, Print, Loop
            command_input = input(">>> ").strip()
            # if command_input == 'exit':
            #     break
            command_name, *args = command_input.split()
            self.command_handler.execute_command(command_name, *args)

# import inspect
# import pkgutil
# import importlib
# from app.commands import CommandHandler, Command

# class App:
#     def __init__(self):
#         self.command_handler = CommandHandler()
#         self.command_history = []

#     def load_plugins(self):
#         plugins_package = 'app.plugins'
#         for _, plugin_name, _ in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
#             plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
#             for item_name in dir(plugin_module):
#                 item = getattr(plugin_module, item_name)
#                 if hasattr(item, 'execute') and issubclass(item, Command) and not inspect.isabstract(item):
#                     self.command_handler.register_command(item_name.lower(), item())


#     def start(self):
#         self.load_plugins()
#         print("Type 'menu' for available commands or 'exit' to quit.")
#         while True:
#             command_input = input(">>> ").strip()
#             if command_input:
#                 self.command_history.append(command_input)  # Add command to history
#             if command_input == 'exit':
#                 self.command_handler.execute_command('exit')
#                 break  # This break is now technically redundant if exit executes sys.exit(0)
#             command_name, *args = command_input.split()
#             self.command_handler.execute_command(command_name, *args)
