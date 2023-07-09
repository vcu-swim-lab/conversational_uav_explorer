import pytest
import re
from chatgpt4uavs import get_command


# format: \ncommand: <command> \t<goal>
def parse_command(text):
    print(text)
    tokens = re.split(' \t|\n|: ', text.lower())
    print(tokens)
    assert tokens[1] == 'command'
    return tokens[2]

def test_red_house():
    text = "Go to the red house on W Broad St."
    command = get_command(text)
    output = command.run(text)
    command = parse_command(output)
    assert command == "go to"