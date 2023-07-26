from flask import Flask, jsonify
from flask_restful import Resource, Api
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


class Command(Resource):
    def get(self):
        latest_command = get_latest_command()
        return jsonify({"latest_command": latest_command})


api.add_resource(Command, '/record')

if __name__ == '__main__':
    app.run(debug=True)
