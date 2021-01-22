#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 22 10:19:44 2021

@author: sb069
"""
import os
import errno

try:
	os.system("mkdir -p Documents/LMToolkit")
except OSError as e:
	if e.errno != errno.EEXIST:
		raise
try:
	os.system("mkdir -p Documents/LMToolkit/MinionOut")
except OSError as e:
	if e.errno != errno.EEXIST:
		raise
try:
	os.system("mkdir -p Documents/LMToolkit/Assembly_Out")
except OSError as e:
	if e.errno != errno.EEXIST:
		raise
def main():
    with open("Documents/LMToolkit/config.txt", "w") as config1:
        Basecall=input("What is the path of your guppy basecaller?:  ")
        config1.write(Basecall)
        config1.close()
    with open("Documents/LMToolkit/guppyconfig.txt", "w") as config2:
        Basecallconfig=input("What is the path of your guppy basecaller?:  ")
        config2.write(Basecallconfig)
        config2.close()

main() 