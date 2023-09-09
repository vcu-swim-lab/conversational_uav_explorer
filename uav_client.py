"""
This module sends HTTP requests to the UAV server.
"""

import re
import requests


def send_command(server_url, command, location=None):
    """
    Sends a command to the server.

    :param server_url: server where the UAV is live
    :param command: command to send
    :type command: str
    :param location: location for the command, defaults to None
    :type location: str
    :return: server response content
    :rtype: bytes
    """
    base_url = server_url

    if location:
        endpoint = f"/{command}/{location}"
    else:
        endpoint = f"/{command}"

    response = requests.post(f"{base_url}{endpoint}")

    return response.content


def get_uav_status(server_url):
    """
    Retrieves the status of the UAV from the server.

    :param server_url: URL of the server where the UAV is live
    :type server_url: str
    :return: UAV status if successful, None otherwise
    :rtype: bytes
    """
    response = requests.get(f"{server_url}/get_uav_status")
    return response.text


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
    return tokens[0]
