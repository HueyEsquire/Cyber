import subprocess
import os


def runCommand(command, simple=False, returncode=False):

    if not type(command) == str:
        print("ERROR: run command passed non string type")
        return

    if simple:
        os.system(command)
        return
    
    command = command.split(" ")

    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout = process.communicate()[0]
    rc = process.returncode

    if returncode:
        return (stdout, rc)
    else:
        return stdout