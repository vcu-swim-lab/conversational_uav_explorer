import pytest
import re
from chatgpt4uavs import get_command


# format: command: <command> \t<goal>
def parse_command(text):
    tokens = re.split(' \t|\n|: ', text.lower())
    print(tokens)
    assert tokens[1] == 'command'
    return tokens[2]

def test_red_house():
    text = "Go to the red house on W Broad St."
    output = get_command(text)
    command = parse_command(output)
    assert command == "go to"