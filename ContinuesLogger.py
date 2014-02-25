#!/usr/bin/python
from subprocess import call
from datetime import datetime
import os
import errno
import sys
import time
import thread

#you need to have sshpass installed from a terminal run
# $ sudo apt-get install sshpass
# souce your bashrc file 

#Setup automatic execution possibly scheduling an event 
#save into a better data structure (some type of a database)
#remove need to type password for each computer 


#creates a folder to put the files into 
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

#will create folder based on the computers name and then every minute will run ps aux on that computer dumping the result into a log file
def runUpdates(computer,delay,user,password):
   #creates folder 
   folder = "ps_aux_"+computer 
   make_sure_path_exists(folder)
   print("created folder: "+folder)

   while True:
       now = str(datetime.now().isoformat());
       fileName = folder+"/"+now+".txt"
       command = "sshpass -p "+ password+" ssh "+user+"@"+computer+" 'ps aux'  >> "+fileName
       call(command,shell=True)
       print ("copied "+computer) 
       time.sleep(delay)

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
    
delay = 60 #set ps_aux to run once every minute 
# ssh's into each computer in computers and creates a 
# log file noting the time and the computer we are logging from
for computer in computers:
    try:
        thread.start_new_thread(runUpdates, (computer,delay,user,password))
    except:
        print "shit"
while 1:
    time.sleep(100000);

