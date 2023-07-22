import pytest
import re
from fewshot import FewShot4UAVs

@pytest.fixture
def fewshot():
    return FewShot4UAVs()

# format: <command> \t<goal>

# For testing sentences with one action
def parse_command(text):
    tokens = re.split(' \t|\n|: ', text.lower())
    print(tokens)
    if len(tokens) >= 2 and tokens[1] == 'command':
        return tokens[2]
    else:
        return 'None'

# For testing sentences with multiple actions
def parse_multiple_commands(text):
    text = text.lstrip('\n')
    lines = text.split("\n")
    first_action = lines[0].split()[1].lower()
    second_action = lines[1].split()[1].lower()
    return first_action, second_action

def test_red_house(fewshot):
    text = "Go to the red house on W Broad St."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"

def test_take_off(fewshot):
    text = "Take off from where you are."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "takeoff"


def test_land(fewshot):
    text = "Land now."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "land"


def test_picture(fewshot):
    text = "Take a picture."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "None"

# Testing actions using synonyms
def test_take_off_synonym(fewshot):
    text = "Lift off."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "takeoff"

def test_snap_pic(fewshot):
    text = "Snap a photo."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "None"


def test_purple_house(fewshot):
    text = "Travel to the purple house on the left side."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"


def test_parking_garage(fewshot):
    text = "Fly to the parking garage across the street."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"


def test_gym(fewshot):
    text = "Check out the Cary St Gym."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"


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

# Testing actions with no location
def test_no_location1(fewshot):
    text = "Check out."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "None"


def test_no_location2(fewshot):
    text = "Go to."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "None"


def test_no_location3(fewshot):
    text = "Travel to."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "None"


def test_no_location4(fewshot):
    text = "Head to."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "None"


# Testing invalid commands
def test_empty_input(fewshot):
    text = ""
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "None"


def test_invalid_command(fewshot):
    text = "Do something."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "None"

# Testing locations with no action specifically stated
def test_location_no_action(fewshot):
    text = "Willow Lawn."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"


def test_location_no_action2(fewshot):
    text = "Whole Foods on W Broad St."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"


def test_location_no_action3(fewshot):
    text = "Starbucks at N Robinson St."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"

# Testing with filler words
def test_with_extra_words(fewshot):
    text = "Please go to the Whole Foods on W Broad St."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"

def test_with_extra_words2(fewshot):
    text = "Go to the Whole Foods on W Broad St please."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"

# Testing multiple actions at the same location
def test_multiple_actions1(fewshot):
    text = "Check out the Starbucks and then land."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ("goto", "land")

def test_multiple_actions2(fewshot):
    text = "Take a picture of the green shed and then take off."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ("takepicture", "takeoff")

def test_multiple_actions3(fewshot):
    text = "Go to the park and take a picture."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ("goto", "takepicture")

def test_multiple_actions4(fewshot):
    text = "Take a photo and then land."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ("takepicture", "land")

def test_multiple_actions5(fewshot):
    text = "Rise and then take a photo."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ("takeoff", "takepicture")

# Testing multiple actions with different locations
def test_multiple_actions_and_locations1(fewshot):
    text = "Go to the maroon shack on Osborn Rd and then take a picture of Thomas Dale High School."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ("goto", "takepicture")

def test_multiple_actions_and_locations2(fewshot):
    text = "Travel to the park and take a picture of the red house."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ("goto", "takepicture")
