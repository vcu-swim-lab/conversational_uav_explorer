import re
from flask import requests


def send_command(command, location=None):
    url = f"http://url/{command}"
    data = {}
    if location:
        data["location"] = location
    response = requests.post(url, json=data)
    return response.content


def parse_command(text):
    tokens = re.split(' \t|\n|: ', text.lower())
    print(tokens)
    if len(tokens) >= 2:
        return tokens[1]
    else:
        return 'none'
