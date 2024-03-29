#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 10:19:44 2021

@author: sb069
"""
import os
import errno
from os.path import expanduser
os.system("sudo apt-get update")
os.system("sudo apt install nvidia-cuda-toolkit") 
os.system("sudo apt install python3.8")
os.system("conda install flye")

try:
	os.system("mkdir -p ~/Documents/LMToolkit")
except OSError as e:
	if e.errno != errno.EEXIST:
		raise
try:
	os.system("mkdir -p ~/Documents/LMToolkit/MinionOut")
except OSError as e:
	if e.errno != errno.EEXIST:
		raise
try:
	os.system("mkdir -p ~/Documents/LMToolkit/Assembly_Out")
except OSError as e:
	if e.errno != errno.EEXIST:
		raise
#Downloads=str(os.environ['_'])


#Downloads=Download.replace('/LMToolkit_Setup.py','')
#print("THIS IS A TEST " + Downloads)
#os.chdir(Downloads)
#print("mv LMToolKit.py ~/Documents/LMToolkit")
try:
	os.system("mv LMToolkit.py ~/Documents/LMToolkit/LMToolkit.py")
except OSError as e:
	if e.errno != errno.EEXIST:
		raise
try:
	os.system("mv README.md ~/Documents/LMToolkit/README.md")
except OSError as e:
	if e.errno != errno.EEXIST:
		raise
try:
	os.system("mv LMToolKit_License ~/Documents/LMToolkit/LMToolKit_License")
except OSError as e:
	if e.errno != errno.EEXIST:
		raise

def main():
    hdir=os.path.expanduser('~')
   
    os.chdir(hdir+'/Documents/LMToolkit')
    with open("config.txt", 'w') as config1:
        Basecall=input("What is the path of your guppy basecaller (ont-guppy/bin/guppy_basecaller)?:  ")
        config1.write(Basecall)
        config1.close()
    with open("guppyconfig.txt", "w") as config2:
        Basecallconfig=input("What is the path of your guppy basecaller config file (ont-guppy/data/config) please read readme for details )?:  ")
        config2.write(Basecallconfig)
        config2.close()
    print("LMToolKit is now setup! Happy Basecalling!")

main() 
