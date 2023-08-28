"""
This module tests commands with multiple actions and locations.
"""

import pytest
from fewshot import FewShot4UAVs


@pytest.fixture
def fewshot():  # pylint: disable=redefined-outer-name
    """Fixture for creating a FewShot4UAVs instance."""
    return FewShot4UAVs()


# format: <command> \t<goal>
def parse_multiple_commands(text):
    """
    Parses the command from the transcribed sentence.

    :param text: text to parse
    :type text: str
    :return: two parsed commands
    :rtype: str
    """
    text = text.lstrip('\n')
    lines = text.split("\n")
    first_action = lines[0].split()[0].lower()
    second_action = lines[1].split()[0].lower()
    return first_action, second_action


def test_multiple_actions(fewshot):
    """Test for 'Take a photo' and 'Take off'"""
    text = "Take a photo and then take off."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ('takephoto', 'takeoff')


def test_two_go_to(fewshot):
    """Test 'Go to' with two locations"""
    text = "Go to the Kroger on Lombardy St and then go to Roots on W Grace St."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ('goto', 'goto')


def test_multiple_actions_and_locations(fewshot):
    """Test 'Go to' as a synonym and 'Take a picture'"""
    text = "Fly to the park and take a picture of the red house."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ('goto', 'takephoto')


def test_action_and_location(fewshot):
    """Test 'Go to' and 'Take a picture' as a synonym"""
    text = "Fly to the park and take a picture."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ('goto', 'takephoto')


def test_action_and_location_synonyms(fewshot):
    """Test 'Take off' and 'Go to' as a synonym"""
    text = "Hover and head to the closest park."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ('takeoff', 'goto')


def test_action_synonyms(fewshot):
    """Test 'Take off' and 'Take a picture' as a synonym"""
    text = "Ascend and then take a photo."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ('takeoff', 'takephoto')


def test_action_synonyms2(fewshot):
    """Test 'Land' and 'Take a picture' as a synonym"""
    text = "Descend and then take a photo."
    output = fewshot.get_command(text)
    command = parse_multiple_commands(output)
    assert command == ('land', 'takephoto')
