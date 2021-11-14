'''
Created Date: Sunday, November 14th 2021
Author: Pawel Kremienowski
Author email: Kremienowski33@gmail.com
-----
Last Modified: Sun Nov 14 2021
Modified By: Pawel Kremienowski
'''


import zmq
import flask

app = flask.Flask(__name__)

ctx = zmq.Context()
sendSocket = ctx.socket(zmq.REQ)
sendSocket.connect("tcp://localhost:5555")


@app.route('/testConnection', methods=["GET"])
def testConnection():
    return "Connection successful"


@app.route('/name', methods=["GET"])
def name():
    return flask.jsonify(msg="RemoteLedsProject")


@app.route('/isRobot', methods=["GET"])
def isRobot():
    return "True"


@app.route('/login', methods=["POST"])
def login():
    if flask.request.form['password'] == "admin":
        return "Pass_OK"
    else:
        flask.abort(401)


@app.route('/doTask/<command>', methods=["POST"])
def doTask(command):
    command = str(command)
    sendSocket.send_string(f"{command}")
    sendSocket.recv()
    return "Command sent"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
