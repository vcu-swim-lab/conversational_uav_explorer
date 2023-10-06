"""This module is a Flask API for the UAV server."""
from flask import Flask

app = Flask(__name__)


@app.route('/goto/<location>', methods=['POST'])
def goto(location):
    """Endpoint for 'go to <location>' """
    pass


@app.route('/land', methods=['POST'])
def land():
    """Endpoint for 'land' """
    pass


@app.route('/takeoff', methods=['POST'])
def takeoff():
    """Endpoint for 'takeoff' """
    print("sending takeoff cmd to grpc or ros node")
    pass


@app.route('/takepicture/<location>', methods=['POST'])
def takepicture(location):
    """Endpoint for 'take picture <description>' """
    pass

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

    pass


if __name__ == '__main__':
    app.run()
