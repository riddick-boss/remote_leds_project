'''
Created Date: Sunday, November 6th 2022
Author: Pawel Kremienowski
Author email: Kremienowski33@gmail.com
-----
Last Modified: Sun Nov 06 2022
Modified By: Pawel Kremienowski
'''


import zmq

import constants

ctx = zmq.Context()
sendSocket = ctx.socket(zmq.PUSH)
sendSocket.connect(constants.SOCKET)

if __name__ == "__main__":
    print("Launching manual commander...")
    try:
        while True:
            data = input("Insert command for arduino: ")
            print(f"You said: {data}")
            sendSocket.send_string(f"{data}")
    except KeyboardInterrupt:
        print("CTRL+C pressed. Finishing")
        exit