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
	#Cut all but the review text
	cmd = 'cut -f3 '+file+' > '+file[:-4]+'_review_only.txt'
	os.system(cmd)
	os.remove(file)