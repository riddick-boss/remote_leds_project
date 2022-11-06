'''
Created Date: Sunday, November 14th 2021
Author: Pawel Kremienowski
Author email: Kremienowski33@gmail.com
-----
Last Modified: Sun Nov 06 2022
Modified By: Pawel Kremienowski
'''


import zmq
import flask

import constants

app = flask.Flask(__name__)

ctx = zmq.Context()
sendSocket = ctx.socket(zmq.PUSH)
sendSocket.connect(constants.SOCKET)


@app.route('/testConnection', methods=["GET"])
def testConnection():
    return "Connection successful"


@app.route('/name', methods=["GET"])
def name():
    return flask.jsonify(msg="RemoteLedsProject")


@app.route('/areRemoteLeds', methods=["GET"])
def isRobot():
    return "True"


@app.route('/doTask/<command>', methods=["POST"])
def doTask(command):
    command = str(command)
    sendSocket.send_string(f"{command}")
    return "Command sent"


if __name__ == '__main__':
    print("Launching flask server...")
    app.run(host='0.0.0.0', port=5000)
