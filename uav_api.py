from flask import Flask
import requests

app = Flask(__name__)


def send_command(command, location=None):
    url = f"http://url/{command}"
    data = {}
    if location:
        data["location"] = location
    response = requests.post(url, json=data)
    return response.content


@app.route('/goto/<location>', methods=['POST'])
def goto(location):
    send_command('goto', location)


@app.route('/land', methods=['POST'])
def land():
    send_command('land')


@app.route('/takeoff', methods=['POST'])
def takeoff():
    send_command('takeoff')


@app.route('/takepicture/<location>', methods=['POST'])
def takepicture(location):
    send_command('takepicture', location)


if __name__ == '__main__':
    app.run()
