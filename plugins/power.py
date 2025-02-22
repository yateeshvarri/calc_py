from commands.base import Command

class PowerCommand(Command):
    def execute(self, a, b):
        return a ** b

def register(invoker):
    invoker.register_command("power", PowerCommand())
