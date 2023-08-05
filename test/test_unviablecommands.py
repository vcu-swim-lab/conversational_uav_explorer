import pytest
import re
from fewshot import FewShot4UAVs


@pytest.fixture
def fewshot():
    return FewShot4UAVs()

# format: <command> \t<goal>
def parse_command(text):
    tokens = re.split(' \t|\n|: ', text.lower())
    print(tokens)
    if len(tokens) >= 2:
        return tokens[1]
    else:
        return 'none'

def test_picture(fewshot):
    text = "Take a picture."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "none"


def test_snap_pic(fewshot):
    text = "Snap a photo."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "none"

def test_no_location1(fewshot):
    text = "Check out."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "none"


def test_no_location2(fewshot):
    text = "Go to."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "none"


def test_no_location3(fewshot):
    text = "Travel to."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "none"


def test_no_location4(fewshot):
    text = "Head to."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "none"


def test_empty_input(fewshot):
    text = ""
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "none"

def test_invalid_command(fewshot):
    text = "Do something."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "none"

