from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import requests
from gradio_client import Client

app = Flask(__name__)
api = Api(app)


def get_latest_command():
    client = Client("http://127.0.0.1:7860")
    result = client.predict(
        "https://github.com/gradio-app/gradio/raw/main/test/test_files/audio_sample.wav",
        api_name="/record"
    )
    lines = result.split('\n')
    command = None
    for line in lines:
        if "UAV:" in line:
            command = line.split("UAV:", 1)[-1].strip()
            break
    return command


def send_command_to_uav_controller(command):
    url = "http://localhost:8080"  # replace with address for UAV's C++ code later
    data = {"command": command}
    response = requests.post(url, json=data)
    return response.text


class Command(Resource):
    def get(self):
        latest_command = get_latest_command()
        return jsonify({"latest_command": latest_command})

    def post(self):
        latest_command = get_latest_command()
        if latest_command:
            response = send_command_to_uav_controller(latest_command)
            return jsonify({"status": "Command sent to UAV controller.", "response": response}), 200
        else:
            return jsonify({"status": "No command available."}), 404

    def put(self):
        pass

    def delete(self):
        pass


api.add_resource(Command, '/command')

if __name__ == '__main__':
    app.run(debug=True)
