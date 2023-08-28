"""
This module contains tests for commands with a single action.
"""

import re
import pytest
from fewshot import FewShot4UAVs


@pytest.fixture
def fewshot():  # pylint: disable=redefined-outer-name
    """Fixture for creating a FewShot4UAVs instance."""
    return FewShot4UAVs()


# format: <command> \t<goal>
def parse_command(text):
    """
    Parses the command from the transcribed sentence.

    :param text: text to parse
    :type text: str
    :return: parsed command
    :rtype: str
    """
    tokens = re.split(' \t|\n|: ', text.lower())
    if len(tokens) >= 2:
        return tokens[1]
    return 'none'


def test_red_house(fewshot):
    """Test for the 'Go to <location>.' command"""
    text = "Go to the red house on W Broad St."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"


def test_take_off(fewshot):
    """Test for 'Take off' with extra words."""
    text = "Take off from where you are."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "takeoff"


def test_take_off_synonym(fewshot):
    """Test for a synonym of 'Land.'"""
    text = "Lift off."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "takeoff"


def test_land(fewshot):
    """Test for 'Land.' with an extra word"""
    text = "Land now."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "land"


def test_purple_house(fewshot):
    """Test for a synonym of 'Go to <location>.'"""
    text = "Travel to the purple house on the left side."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"


def test_parking_garage(fewshot):
    """Test for a synonym of 'Go to <location>.'"""
    text = "Fly to the parking garage across the street."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"


def test_gym(fewshot):
    """Test for a synonym of 'Go to <location>.'"""
    text = "Check out the Cary St Gym."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"


def test_cease_flight(fewshot):
    """Test for a synonym of 'Land.'"""
    text = "Cease flight."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "land"


def test_stop_flight(fewshot):
    """Test for a synonym of 'Land.'"""
    text = "Stop the flight."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "land"


def test_location_no_action(fewshot):
    """Test for a command with an unspecified action."""
    text = "Willow Lawn."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"


def test_location_no_action2(fewshot):
    """Test for a command with an unspecified action."""
    text = "Whole Foods on W Broad St."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"


def test_location_no_action3(fewshot):
    """Test for a command with an unspecified action."""
    text = "Starbucks at N Robinson St."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"


def test_with_extra_words(fewshot):
    """Test for unnecessary words in the command."""
    text = "Please go to the Whole Foods on W Broad St."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"


def test_with_extra_words2(fewshot):
    """Test for unnecessary words in the command."""
    text = "Go to the Whole Foods on W Broad St please."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "goto"


def test_action_synonyms3(fewshot):
    """Test for a synonym of 'Land.'"""
    text = "Descend"
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == 'land'
