"""
This module sends a POST request to the UAV server.
"""

import re
import requests


def send_command(command, location=None):
    """
    Sends a command to the server.

    :param command: command to send
    :type command: str
    :param location: location for the command, defaults to None
    :type location: str
    :return: server response content
    :rtype: bytes
    """
    base_url = f"http://url"

    if location:
        endpoint = f"/{command}/{location}"
    else:
        endpoint = f"/{command}"

    response = requests.post(f"{base_url}{endpoint}")

    return response.content


def parse_command(text):
    """
    Parses the command from the transcribed sentence.

    :param text: text to parse
    :type text: str
    :return: command and location if available, else command
    :rtype: str
    """
    tokens = re.split(' \t|\n|: ', text.lower())
    print(tokens)
    if len(tokens) >= 2:
        return tokens[0], tokens[1]
    else:
        return tokens[0]
