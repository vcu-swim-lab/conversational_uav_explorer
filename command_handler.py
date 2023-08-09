import re
import requests


def send_command(command, location=None):
    base_url = f"http://url" # replace with UVA's URL

    if location:
        endpoint = f"/{command}/{location}"
    else:
        endpoint = f"/{command}"

    response = requests.post(f"{base_url}{endpoint}")

    return response.content


def parse_command(text):
    # does not support multiple commands
    tokens = re.split(' \t|\n|: ', text.lower())
    print(tokens)
    if len(tokens) >= 2:
        return tokens[0], tokens[1]
    else:
        return tokens[0]
