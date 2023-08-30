"""This module is a Flask API for the UAV server."""
from flask import Flask

app = Flask(__name__)


@app.route('/goto/<location>', methods=['POST'])
def goto(location):  # pylint disable=unused-argument,unnecessary-pass
    """Endpoint for 'go to <location>' """
    pass


@app.route('/land', methods=['POST'])
def land():
    """Endpoint for 'land' """
    pass


@app.route('/takeoff', methods=['POST'])
def takeoff():
    """Endpoint for 'takeoff' """
    pass


@app.route('/takepicture/<location>', methods=['POST'])
def takepicture(location):
    """Endpoint for 'take picture <description>' """
    pass


if __name__ == '__main__':
    app.run()
