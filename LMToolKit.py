#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 17:08:19 2021

@author: sb069
"""
import subprocess
import errno
import os 
#Guppy Start 

#basecall=input("Drag and Drop the guppy_basecaller you wish to use here (should be found in /ont-guppy/bin/):  ")
#basecall=basecall.strip()
#basecall=basecall[:-1]
#basecallconfig=input("Drag and Drop the guppy_basecaller you wish to use here (should be found in /ont-guppy/data/):  ")
with open("config.txt","r") as basecallpath:
    basecall=basecallpath.read()
    print("This is your basecaller path " + basecall)
with open("guppyconfig.txt","r") as configpath:
    basecallconfig=configpath.read()
    print("This is your config file path " + basecallconfig)    
qinputgup=input("What is the name of the input fast5 folder (drag and drop it here): ")
folderoutgup=input("What would you like to the name the output folder?:  ")
q1=input("Are you expecting plasmids? [y/N]:  ")


print("The output of guppy will be found here: MinionOut/"+folderoutgup)
outpathgup="MinionOut/"+folderoutgup

outpathgupfinal=outpathgup
try:
	os.system("mkdir " + outpathgup)
except OSError as e:
	if e.errno != errno.EEXIST:
		raise
string1='sudo  ' + basecall + '  -i ' + qinputgup +  ' -s ' + outpathgupfinal +  ' -c ' + basecallconfig + ' -x ' '"cuda:0"'
print(string1)
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
#os.chdir(folderin) #Check 2 for strip 
string3 = str('cd ' + folderin + ";" + "cat *.fastq > " + outfilename)
print(string3)
subprocess.run(string3, shell=True)

#Flye Start


qinput=outfilename

if q1=='y':
    plasmid= '--plasmid '
elif q1=='N':
    plasmid=" "
else:
    plasmid='--plasmid'

print("The assembled output will be found here: " , folderoutgup)
outpath="Assembly_Out/"+folderoutgup
outpath1="'"+outpath+"'"
try:
	os.system("mkdir -p " +outpath )
except OSError as e:
	if e.errno != errno.EEXIST:
		raise
inassemble=outpathgupfinal+"/"+outfilename
print(inassemble)
string2='flye ' '-o ' + outpath1 + ' --threads 14 ' '-i 6 ' ' --nano-raw ' + inassemble + " " + plasmid 
print(string2)
os.system(string2)
print("This program has now finished!") 
