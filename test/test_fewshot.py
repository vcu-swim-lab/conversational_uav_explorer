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

def test_take_off(fewshot):
    text = "Take off from where you are."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "take off"

def test_land(fewshot):
    text = "Land now."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "land"

def test_picture(fewshot):
    text = "Take a picture."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "take picture"

def test_snap_pic(fewshot):
    text = "Snap a photo."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "take picture"

def test_purple_house(fewshot):
    text = "Travel to the purple house on the left side."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "go to"

def test_parking_garage(fewshot):
    text = "Fly to the parking garage across the street."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "go to"

def test_gym(fewshot):
    text = "Check out the Cary St Gym."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "go to"

def test_cease_flight(fewshot):
    text = "Cease flight."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "land"

def test_stop_flight(fewshot):
    text = "Stop the flight."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "land"

def test_lift_off(fewshot):
    text = "Lift off."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "take off"

def test_no_location1(fewshot):
    text = "Check out."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "None"

def test_no_location2(fewshot):
    text = "Go to"
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "None"

def test_no_location3(fewshot):
    text = "Travel to"
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "None"
