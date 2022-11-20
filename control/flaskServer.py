'''
Created Date: Sunday, November 14th 2021
Author: Pawel Kremienowski
Author email: Kremienowski33@gmail.com
-----
Last Modified: Sat Nov 12 2022
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
    return flask.jsonify(True)


@app.route('/doTask/<command>', methods=["POST"])
def doTask(command):
    commandToPass = str(command).replace("_", " ")
    sendSocket.send_string(commandToPass)
    return "Command sent"


if __name__ == '__main__':
    print("Launching flask server...")
    app.run(host='0.0.0.0', port=5000)
