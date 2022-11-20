'''
Created Date: Sunday, November 14th 2021
Author: Pawel Kremienowski
Author email: Kremienowski33@gmail.com
-----
Last modified: 
Modified by: Pawel Kremienowski
'''


import zmq
import serial
import time
import os

import constants

def createSocket(ctx: zmq.Context) -> zmq.Socket:
    socket = ctx.socket(zmq.PULL) # reciv type
    socket.bind(constants.SOCKET)
    return socket


def createArduinoSerial() -> serial.Serial:
    if os.name == 'nt':# windows
        return serial.Serial(port='COM3', baudrate=9600, timeout=.1)
    elif os.name == "posix": # linux
        return serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)


def sendToArduino(arduino: serial.Serial, msg: str):
    arduino.write(bytes(msg, 'utf-8'))
    time.sleep(0.2)


def getData(socket: zmq.Socket):
    return str(socket.recv())


if __name__ == '__main__':
    print("Launching contol center...")
    ctx = zmq.Context()
    socket = createSocket(ctx)
    arduino = createArduinoSerial()

    try:
        while True:
            msg = getData(socket)
            sendToArduino(arduino, msg)
            print(msg)
    except KeyboardInterrupt:
        sendToArduino("diodes off")
        print("CTRL+C pressed. Finishing")
        exit()
