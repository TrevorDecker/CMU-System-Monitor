#!/usr/bin/python
from subprocess import call
from datetime import datetime
import os
import errno
import sys

#you need to have sshpass installed from a terminal run
# $ sudo apt-get install sshpass
# souce your bashrc file 

#creates a folder to put the files into 
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

#Setup automatic execution possibly scheduling an event 
#save into a better data structure (some type of a database)
#remove need to type password for each computer 

#the list of all computers ips or url that we wish to log from 
with open('computers.txt') as f:
    computers = f.read().splitlines()

#prompts the user for the password and username to loginto each server with
if len(sys.argv) != 3:
    print("correct usage is python AutoLogger.py [username] [password] \n")
    exit(1)
else:
    user =  str(sys.argv[1])
    password = str(sys.argv[2])
    

#creates folder 
time = str(datetime.now().isoformat());
folder = time #consider creating a better name for the folder
make_sure_path_exists(folder)

# ssh's into each computer in computers and creates a 
# log file noting the time and the computer we are logging from
for computer in computers:
    fileName = folder+"/"+computer+".txt"
    command = "sshpass -p "+ password+" ssh "+user+"@"+computer+" 'last'  >> "+fileName
    call(command,shell=True)


