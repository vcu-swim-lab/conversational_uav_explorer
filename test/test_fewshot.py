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


def parse_multiple_commands(text):
    text = text.lstrip('\n')
    lines = text.split("\n")
    first_action = lines[0].split()[0].lower()
    second_action = lines[1].split()[0].lower()
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


def test_take_off_synonym(fewshot):
    text = "Lift off."
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
    assert command == "none"


def test_snap_pic(fewshot):
    text = "Snap a photo."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "none"


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


def test_multiple_actions(fewshot):
    text = "Take a photo and then take off."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ('takephoto', 'takeoff')


def test_two_go_to(fewshot):
    text = "Go to the Kroger on Lombardy St and then go to Roots on W Grace St."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ('goto', 'goto')


def test_multiple_actions_and_locations(fewshot):
    text = "Fly to the park and take a picture of the red house."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ('goto', 'takephoto')

def test_action_and_location(fewshot):
    text = "Fly to the park and take a picture."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ('goto', 'takephoto')

def test_action_and_location_synonyms(fewshot):
    text = "Hover and head to the closest park."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ('takeoff', 'goto')

def test_action_synonyms(fewshot):
    text = "Ascend and then take a photo."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ('takeoff', 'takephoto')
    
def test_action_synonyms2(fewshot):
    text = "Descend and then take a photo."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ('land', 'takephoto')
    
def test_action_synonyms3(fewshot):
    text = "Descend"
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == 'land'
