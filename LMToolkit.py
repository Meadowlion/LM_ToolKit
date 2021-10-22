#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 17:08:19 2021

@author: sb069
"""
import subprocess
import errno
import os 


def main():
    global outpathgupfinal
    global qinputgup
    global q1
    global Alignq
    global Assembleq
    global basecallconfig
    global basecall
    global folderoutgup
    global outfilename
    global plasmid
    global outpathgup
    global refpath
    with open("config.txt","r") as basecallpath:
        basecall=basecallpath.read()
        print("This is your basecaller path " + basecall)
    with open("guppyconfig.txt","r") as configpath:
        basecallconfig=configpath.read()
        print("This is your config file path " + basecallconfig)    
    qinputgup=input("What is the name of the input fast5 folder (drag and drop it here): ")
    folderoutgup=input("What would you like to the name the output folder?:  ")
    q1=input("Are you expecting plasmids? [y/N]:  ")
    Alignq=input("Would you like to run an alignment [y/N]:  ")
    Assembleq=input("Would you like to run an assembly [y/N]:  ")
    print("The output of guppy will be found here: MinionOut/"+folderoutgup)
    outpathgup="MinionOut/"+folderoutgup
    outpathgupfinal=outpathgup
    if Alignq == "y":
        refpath=input("What is the path to your reference file? (drag and drop it here): ")
        basecalling()
    else:
        basecalling()
        
    
    
    
def basecalling(): 
    global outpathgupfinal
    global qinputgup
    global q1
    global Alignq
    global Assembleq
    global basecallconfig
    global basecall
    global folderoutgup
    global outfilename
    global plasmid
    global outpathgup
    try:
        os.system("mkdir " + outpathgup)
    except OSError as e:
	    if e.errno != errno.EEXIST:
		    raise
    string1='sudo  ' + basecall + '  -i ' + qinputgup +  ' -s ' + outpathgupfinal +  ' -c ' + basecallconfig
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
    if Assembleq == "y" and Alignq == "y" :
        flye()
    elif Assembleq == "N" and Alignq== "y":
        Align()
    elif Assembleq == "N" and Alignq == "N":
        pass
    elif Assembleq == "y" and Alignq == "N":
        flye()
    else:
        (flye)
#Flye Start

def flye():
    global outfilename
    global q1
    global plasmid
    global outpathgupfinal
    global qinputgup
    global q1
    global Alignq
    global Assembleq
    global basecallconfig
    global basecall
    global folderoutgup
    global outfilename
    global plasmid
    global outpathgup
    global inassemble
    global outpath1   
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
    string2='flye ' '-o ' + outpath1 + ' --threads 14 ' '-i 3 ' ' --nano-raw ' + inassemble + " " + plasmid 
    print(string2)
    os.system(string2)
    if Alignq=="N":
        print("This program has now finished!") 
    else:
        Align()

def Align():
    global outpathgupfinal
    global basecall
    global outpath1
    global refpath 
    
    alignpath=basecall.replace("basecaller","aligner")
    stringalign= 'sudo ' + alignpath +  "-i " + outpathgupfinal + " -s " + outpath1 + " -a " + refpath
    print(stringalign)
    os.system(stringalign)
    
main()
    
