# LMToolkit
This pipeline is only for Linux due to its reliance on Flye and the GPU Based Version of ONT's Guppy. It may run on windows using WSL2 and Ubuntu. 
This is just small command line pipeline to simplify going from ONT Unbasecalled data using Guppy to Assembly using Flye, all of the tools are existing tools.
(The setup is for debian based Linux Distros due to APT but should run on other Linux distros if Flye and Python3 are installed manually) 


The program will automatically install Flye

GETTING STARTED 
To get started you will 
cd to the LMToolkit directory
run LMToolKit_Setup.py (python3 LMToolKit_Setup.py, (this will run  "sudo apt-get update" , "sudo apt-get install python3.8" and "conda install flye". These will install python3.8 and flye for you if you do not already have them.) 

The program next will create a directory in Documents; Ie Documents/LMToolkit/ with /MinionOut and /Assembly_Out as subdirectories.

It will then ask for the location of your guppy_basecaller and guppy_basecall config file (fast_450bps is recommended for DNA). 

If you want to change the config file just rerun the setup.

RUNNING LM_TOOLKIT:
Now that the setup is done cd to LM_Toolkit and run LMToolkit.py in terminal.
The program is going to ask for the location of the fast5 folder created by Minknow, what you wish to name the output folder and whether your sample contained plasmids (used by Flye for assembly). 

The outputs from Guppy will be found in /MinionOut as .fastq files the program will also combine them into a singular .fastq file named what you named the output without modifying any of the original FASTQ files.

The output from Flye will be found in /Assembly_Out as assembly.fasta. 

All information and errors from the individual program will also show in the terminal along with the programs data as well.


I hope this simplifies analysis for anyone new to ONT basecalling and assembly! 



https://github.com/fenderglass/Flye required (installed during setup)

and

ONT's GPU Based Guppy Required (needs to be installed from ONT) version 4.2.2. 

if bioconda is not installed first install bioconda: 
```
curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
sh Miniconda3-latest-Linux-x86_64.sh
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
```
