import os
import glob
import pathlib

#Of note, certain instances, you will want to remove duplicate lines.
#In situations of customer generated data, it increases the accuracy to leave them.
#As some commenting and reviewing will repeat others.

#Set process directory
proc_dir = os.getcwd()+'//to_process//'
#Load all filenames in the directory into a list
mylist = os.listdir(proc_dir)
#Sort the list alphabetically
mylist.sort()
#Change directories into to_process
os.chdir(proc_dir)
#Iterate through the list of files
for file in mylist:
	#Cut the following col6[book title],col8[star rating] and col13[review body]
	#We do this with the Unix "cut" command formatted below
	cmd = 'cut -f6,8,13 '+file+' > '+file+'-6-8-13-processed.txt'
	#Send the formatted command to be executed
	os.system(cmd)
	#Delete the initial file, leaving only our cleaned data
	os.remove(file)
