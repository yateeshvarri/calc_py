from commands.base import Command

class SquareCommand(Command):
    def execute(self, a):
        return a * a

def register(invoker):
    invoker.register_command("square", SquareCommand())
