'''
Created Date: Wednesday, November 17th 2021
Author: Pawel Kremienowski
Author email: Kremienowski33@gmail.com
-----
Last Modified: Wed Nov 17 2021
Modified By: Pawel Kremienowski
'''


import os


# open new cmd/terminal and run command there
def sendCommandNewTerminal(com: str):
    # windows
    if os.name == 'nt':
        os.system(f"start \"\" cmd /k \"{com}\"")
    # linux
    elif os.name == 'posix':
        os.system(f"gnome-terminal -- {com}")


# run command from same cmd/terminal
def sendCommand(com: str):
    # windows
    if os.name == 'nt':
        os.system(com)
    # linux
    elif os.name == 'posix':
        os.system(com)
