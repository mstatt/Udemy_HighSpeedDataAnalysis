import os
import glob
import pathlib

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
	#Cut the 13th column from the tabbed file to isolate the actual user review text
	cmd = 'cut -f13 '+file+' > '+file+'-processed.txt'
	os.system(cmd)
print(mylist)
