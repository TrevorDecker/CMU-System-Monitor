#!/bin/bash

#reads what the file shuld be saved as
computer="$(hostname)"

who="www/data/who_"$computer".txt"
psaux="www/data/psaux_"$computer".txt"


#removes the old copy of the files
rm $who || echo "no file to delete"
rm $psaux || echo "no file to delete"

#runs the who command and saves the result to a file
who>>$who

#runs the ps aux command and saves the result to a file
ps aux>>$psaux
