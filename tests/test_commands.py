import pytest
from commands.basic import AddCommand

def test_add():
    command = AddCommand()
    assert command.execute(2, 3) == 5
