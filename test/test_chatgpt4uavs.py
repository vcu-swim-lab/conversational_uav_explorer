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

def test_red_house():
    text = "Go to the red house on W Broad St."
    output = get_command(text)
    command = parse_command(output)
    assert command == "go to"

def test_take_off():
    text = "Take off from where you are."
    output = get_command(text)
    command = parse_command(output)
    assert command == "take off"

def test_land():
    text = "Land now."
    output = get_command(text)
    command = parse_command(output)
    assert command == "land"

def test_picture():
    text = "Take a picture."
    output = get_command(text)
    command = parse_command(output)
    assert command == "take picture"

def test_snap_pic():
    text = "Snap a photo."
    output = get_command(text)
    command = parse_command(output)
    assert command == "take picture"

def test_purple_house():
    text = "Travel to the purple house on the left side."
    output = get_command(text)
    command = parse_command(output)
    assert command == "go to"

def test_parking_garage():
    text = "Fly to the parking garage across the street."
    output = get_command(text)
    command = parse_command(output)
    assert command == "go to"

def test_gym():
    text = "Check out the Cary St Gym."
    output = get_command(text)
    command = parse_command(output)
    assert command == "go to"

def test_cease_flight():
    text = "Cease flight."
    output = get_command(text)
    command = parse_command(output)
    assert command == "land"

def test_stop_flight():
    text = "Stop the flight."
    output = get_command(text)
    command = parse_command(output)
    assert command == "land"

def test_lift_off():
    text = "Lift off."
    output = get_command(text)
    command = parse_command(output)
    assert command == "take off"

def test_no_location1():
    text = "Check out."
    output = get_command(text)
    command = parse_command(output)
    assert command == "None"

def test_no_location2():
    text = "Go to"
    output = get_command(text)
    command = parse_command(output)
    assert command == "None"

def test_no_location3():
    text = "Travel to"
    output = get_command(text)
    command = parse_command(output)
    assert command == "None"
