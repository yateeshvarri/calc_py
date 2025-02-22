class Invoker:
    def __init__(self):
        self.commands = {}

    def register_command(self, name, command):
        """Registers a new command."""
        self.commands[name] = command

    def execute_command(self, name, *args):
        """Executes a registered command."""
        if name in self.commands:
            return self.commands[name].execute(*args)
        else:
            raise ValueError(f"Command '{name}' not found.")

    def execute_command_async(self, name, *args):
        """Executes a command asynchronously using multiprocessing."""
        if name in self.commands:
            from multiprocessing import Process
            process = Process(target=self.commands[name].execute, args=args)
            process.start()
            process.join()
        else:
            raise ValueError(f"Command '{name}' not found.")
