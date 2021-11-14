# import zmq
import serial
import time

'''
Created Date: Sunday, November 14th 2021
Author: Pawel Kremienowski
Author email: Kremienowski33@gmail.com
-----
Last modified: 
Modified by: Pawel Kremienowski
'''


arduino = serial.Serial(port='COM3', baudrate=9600, timeout=.1)


def sendToArduino(msg: str):
    arduino.write(bytes(msg, 'utf-8'))
    time.sleep(0.2)


if __name__ == '__main__':
    try:
        msg = input("Enter message to Arduino: ")
        sendToArduino(msg)
    except KeyboardInterrupt:
        sendToArduino("diodes off")
        print("CTRL+C pressed. Finishing")
        exit()
