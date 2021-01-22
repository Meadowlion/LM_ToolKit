# LMToolkit
This pipeline is only for Linux due to its reliance on Flye and the GPU Based Version of ONT's Guppy.
This is just small command line pipeline to simplify going from ONT Unbasecalled data using Guppy to Assembly using Flye, all of the tools are existing tools.
(The setup is for ubuntu specifically but should run on other Linux distros if Flye and Python3 are installed manually) 

The program will automatically install Flye

To get started you will run LMToolkit_Setup.py in the terminal, this will run  "sudo apt-get update" , "sudo apt-get install python3.8" and "conda install flye". These will install python3.8 and flye for you if you do not already have them. 

The program next will create a directory in Documents; Ie Documents/LMToolkit/ with /MinionOut and /Assembly_Out as subdirectories.

It will then ask for the location of your guppy_basecaller and guppy_basecall config file (fast_450bps is recommended for DNA). 

If you want to change the config file just rerun the setup.

Now that the setup is done run LMToolkit.py in terminal.
The program is going to ask for the location of the fast5 folder created by Minknow, what you wish to name the output folder and whether your sample contained plasmids (used by Flye for assembly). 

The outputs from Guppy will be found in /MinionOut as .fastq files the program will also combine them into a singular .fastq file named what you named the output.

The output from Flye will be found in /Assembly_Out as assembly.fasta. 

All information and errors from the individual program will also show in the terminal along with the programs data as well.


I hope this simplifies analysis for anyone new to ONT basecalling and assembly! 



https://github.com/fenderglass/Flye

and

ONT's GPU Based Guppy Required. 
