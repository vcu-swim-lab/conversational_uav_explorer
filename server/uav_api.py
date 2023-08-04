from flask import Flask

app = Flask(__name__)


@app.route('/goto/<location>', methods=['POST'])
def goto(location):
    pass


@app.route('/land', methods=['POST'])
def land():
    pass

@app.route('/takeoff', methods=['POST'])
def takeoff():
    pass

@app.route('/takepicture/<location>', methods=['POST'])
def takepicture(location):
    pass

if __name__ == '__main__':
    app.run()
