"""
This module contains tests for unviable commands.
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


def test_picture(fewshot):
    """Test the 'Take a picture.' command with no location"""
    text = "Take a picture."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "none"


def test_snap_pic(fewshot):
    """Test the 'Snap a photo.' command with no description of what to take a picture of"""
    text = "Snap a photo."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "none"


def test_no_location1(fewshot):
    """Test the 'Check out.' command with no location"""
    text = "Check out."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "none"


def test_no_location2(fewshot):
    """Test the 'Go to.' command with no location"""
    text = "Go to."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "none"


def test_no_location3(fewshot):
    """Test the 'Travel to.' command with no location"""
    text = "Travel to."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "none"


def test_no_location4(fewshot):
    """Test the 'Head to.' command with no location"""
    text = "Head to."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "none"


def test_empty_input(fewshot):
    """Test empty input"""
    text = ""
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "none"


def test_invalid_command(fewshot):
    """Test an invalid command"""
    text = "Do something."
    output = fewshot.get_command(text)
    command = parse_command(output)
    assert command == "none"
