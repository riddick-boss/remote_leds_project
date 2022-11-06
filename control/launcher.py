'''
Created Date: Wednesday, November 17th 2021
Author: Pawel Kremienowski
Author email: Kremienowski33@gmail.com
-----
Last Modified: Sun Nov 06 2022
Modified By: Pawel Kremienowski
'''

import psutil
import terminalCommand


def _processExists(processName: str) -> bool:
    for pid in psutil.pids():
        p = psutil.Process(pid)
        if p.name() == "python.exe" and len(p.cmdline()) > 1 and processName in p.cmdline()[1]:
            return True
    return False


def _checkAndStartProcess(processName: str):
    if _processExists(processName): return
    terminalCommand.sendCommandNewTerminal(
        f"python3 {processName}")


def checkAndStartControlCenter():
    _checkAndStartProcess("controlCenter.py")


def checkAndStartFlaskServer():
    _checkAndStartProcess("flaskServer.py")


def checkAndStartAudio():
    _checkAndStartProcess("speechControl.py")
    

def checkAndStartManualCommander():
    _checkAndStartProcess("manualCommander.py")


def checkAllProcesses():
    checkAndStartFlaskServer()
    checkAndStartControlCenter()
    checkAndStartAudio()
    checkAndStartManualCommander()


if __name__ == '__main__':
    print("launcher starting...")
    checkAllProcesses()
    print("launcher done")
