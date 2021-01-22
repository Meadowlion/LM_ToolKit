#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 17:08:19 2021

@author: sb069
"""

import errno
import os 
#Guppy Start 

#basecall=input("Drag and Drop the guppy_basecaller you wish to use here (should be found in /ont-guppy/bin/):  ")
#basecall=basecall.strip()
#basecall=basecall[:-1]
#basecallconfig=input("Drag and Drop the guppy_basecaller you wish to use here (should be found in /ont-guppy/data/):  ")
with open("Documents/LMToolkit/config.txt","r") as basecallpath:
    basecall=basecallpath.read()
    print(basecall)
with open("Documents/LMToolkit/guppyconfig.txt","r") as configpath:
    basecallconfig=configpath.read()
    print(basecallconfig)    
qinputgup=input("What is the name of the input fast5 folder (drag and drop it here): ")
folderoutgup=input("What would you like to the name the output folder?:  ")
q1=input("Is this a plasmid? [y/N]:  ")
q2=input("How big is the expected output?:  ")

print("The output of guppy will be found here: /Documents/LMToolkit/MinionOut/"+folderoutgup)
outpathgup="Documents/LMToolkit/MinionOut/"+folderoutgup
print(outpathgup)
outpathgupfinal=outpathgup
try:
	os.system("mkdir " + outpathgup)
except OSError as e:
	if e.errno != errno.EEXIST:
		raise
string1='sudo  ' + basecall + '  -i ' + qinputgup +  ' -s ' + outpathgupfinal +  ' -c ' + basecallconfig + ' -x ' '"cuda:0"'
os.system(string1)

#Merger Start

folderin=outpathgupfinal
folderin.strip()
#folderin=folderin[:-1]
#folderin=folderin[1:]
print(folderin) #check 1 for strip
outfilename=folderoutgup
outfilename=outfilename +'.fastq'
print("the merged file will be located in " + folderin + " named as " + outfilename)
os.chdir(folderin) #Check 2 for strip 

os.system('cat ' '*.fastq ' '>' +outfilename)

#Flye Start
print(folderin)

qinput=outfilename

if q1=='y':
    plasmid= '--plasmid '
elif q1=='N':
    plasmid=" "
else:
    q1

print("The assembled output will be found here: Documents/LMToolkit/Assembly_Out/"+folderoutgup)
outpath="Documents/LMToolkit/Assembly_Out/"+folderoutgup
outpath1="'"+outpath+"'"
try:
	os.system("mkdir -p " +outpath )
except OSError as e:
	if e.errno != errno.EEXIST:
		raise


string2='flye ' '-o ' + outpath1 + ' --threads 14 ' '-i 6 ' ' --nano-raw ' + qinput + " " + plasmid 
print(string2)
os.system(string2)

