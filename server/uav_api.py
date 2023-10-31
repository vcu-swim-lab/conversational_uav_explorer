"""This module is a Flask API for the UAV server."""
from flask import Flask

app = Flask(__name__)

uav_current_status = "0"  # default status? waiting for a command


@app.route('/goto/<location>', methods=['POST'])
def goto(location):
    """Endpoint for 'go to <location>' """
    global uav_current_status
    uav_current_status = "2"


@app.route('/land', methods=['POST'])
def land():
    """Endpoint for 'land' """
    global uav_current_status
    uav_current_status = "3"


@app.route('/takeoff', methods=['POST'])
def takeoff():
    """Endpoint for 'takeoff' """
    global uav_current_status
    uav_current_status = "1"


@app.route('/takepicture/<location>', methods=['POST'])
def takepicture(location):
    """Endpoint for 'take picture <description>' """
    global uav_current_status
    uav_current_status = "4"


@app.route('/get_uav_status', methods=['GET'])
def uav_status():
    """Endpoint for retrieving the UAV's status """

    """status_messages
        -1: Error executing command
        1: Take off
        2: Go to
        3: Land
        4: Take picture
    """
    global uav_current_status
    return uav_current_status


if __name__ == '__main__':
    app.run()
