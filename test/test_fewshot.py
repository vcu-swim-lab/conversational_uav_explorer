import pytest
import re
from fewshot import FewShot4UAVs

@pytest.fixture
def fewshot():
    return FewShot4UAVs()

# format: command: <command> \t<goal>
def parse_command(text):
    tokens = re.split(' \t|\n|: ', text.lower())
    print(tokens)
    assert tokens[1] == 'command'
    return tokens[2]

def test_red_house(fewshot):
    text = "Go to the red house on W Broad St."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "go to"