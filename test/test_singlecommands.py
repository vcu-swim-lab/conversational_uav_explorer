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

def test_action_synonyms3(fewshot):
    text = "Descend"
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == 'land'