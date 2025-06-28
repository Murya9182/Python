# Pythons biggest power:
#
#    there is a "zillion" of already implemented solutions ...
#    ... you just need to bring your own problem to solve


# let us start the import business.
# we import our first module
import subprocess

# Caution!
#  shell=True is needed here to spawn a system shell.
#  NEVER do this forward to system with unknown/unsafe commands ...
subprocess.run("dir", shell=True)

# for the case, you want to "save" the output for processing inside your script:
completedProcess = subprocess.run("dir", shell=True, capture_output=True)
for line in completedProcess.stdout.splitlines():
    print(line)

# before we can use those nifty tools, you need to
#    0) install git
#    1) initialize your repository using "git init ."
#    2) bundle files for a commit using "git add fileName.py"
#    3) commit using a *meaningful* message "git commit -m 'I AM A MEANINGFUL COMMIT MESSAGE' "
# TASK: check out the usage and meaning of git push and git pull
subprocess.run(["git", "status"])
subprocess.run(["git", "log"])

# back to the import business. we can import a module
import os
print(os.name)

# or import specific functions from a module as in
from os import getcwd
currentWorkingDirectory=getcwd()
print(currentWorkingDirectory)

# we can rename things while importing them
import configparser as cfgParser
config = cfgParser.ConfigParser()
config.read("lec_01a_config_file.ini")

# while we are here, use the config parser a little
print("Sections inside of the config file:")
print(config.sections())
print("Defaults of the config")
print(config.defaults())
for key in config['HM2']:
    print(key, ":=", config['HM2'][key])

# now create a new python file named universe.py
# inside the file, define to random variables
from lec_01b_universe import *
print(father)

# now let us have some fun
import turtle
screen = turtle.Screen()
bob = turtle.Turtle()

# caution when shadowing modules
# create a python file named turtle.py
# see if the above still works








