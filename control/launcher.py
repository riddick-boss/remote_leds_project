'''
Created Date: Wednesday, November 17th 2021
Author: Pawel Kremienowski
Author email: Kremienowski33@gmail.com
-----
Last Modified: Wed Nov 17 2021
Modified By: Pawel Kremienowski
'''

import psutil
import terminalCommand


def checkAndStartControlCenter():
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if p.name() == "python.exe" and len(p.cmdline()) > 1 and "controlCenter.py" in p.cmdline()[1]:
            return
    terminalCommand.sendCommandNewTerminal(
        "python3 controlCenter.py")


def checkAndStartFlaskServer():
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if p.name() == "python.exe" and len(p.cmdline()) > 1 and "flaskServer.py" in p.cmdline()[1]:
            return
    terminalCommand.sendCommandNewTerminal(
        "python3 flaskServer.py")


def checkAndStartAudio():
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if p.name() == "python.exe" and len(p.cmdline()) > 1 and "speechControl.py" in p.cmdline()[1]:
            return
    terminalCommand.sendCommandNewTerminal(
        "python3 speechControl.py")


def checkAllProcesses():
    checkAndStartFlaskServer()
    checkAndStartControlCenter()
    checkAndStartAudio()


if __name__ == '__main__':
    print("launcher starting...")
    checkAllProcesses()
    print("launcher done")
