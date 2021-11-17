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

# for pc (windows)
# arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)

# for raspberry pi
arduino = serial.Serial(port='/dev/ttyACM0', baudrate=9600, timeout=.1)


ctx = zmq.Context()
recivSocket = ctx.socket(zmq.REP)


def sendToArduino(msg: str):
    arduino.write(bytes(msg, 'utf-8'))
    time.sleep(0.2)


def prepareSocket():
    global recivSocket
    recivSocket.bind("tcp://*:5555")


def getData():
    global recivSocket
    data = str(recivSocket.recv())
    recivSocket.send_string(f"received")
    return data


if __name__ == '__main__':
    prepareSocket()
    try:
        while True:
            msg = getData()
            sendToArduino(msg)
            print(msg)
    except KeyboardInterrupt:
        sendToArduino("diodes off")
        print("CTRL+C pressed. Finishing")
        exit()
