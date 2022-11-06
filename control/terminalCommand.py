'''
Created Date: Wednesday, November 17th 2021
Author: Pawel Kremienowski
Author email: Kremienowski33@gmail.com
-----
Last Modified: Sun Nov 06 2022
Modified By: Pawel Kremienowski
'''


import os


# open new cmd/terminal and run command there
def sendCommandNewTerminal(com: str):
    if os.name == 'nt': # windows
        os.system(f"start \"\" cmd /k \"{com}\"")
    elif os.name == 'posix': # linux
        os.system(f"gnome-terminal -- {com}")


# run command from same cmd/terminal
def sendCommand(com: str):
    if os.name == 'nt': # windows
        os.system(com)
    elif os.name == 'posix': # linux
        os.system(com)
