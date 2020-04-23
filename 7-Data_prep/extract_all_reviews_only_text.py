import os
import glob
import pathlib

proc_dir = os.getcwd()+'//process_reviews//'
#os.listdir(os.getcwd()+'/job_queue/amazon_reviews/')
mylist = os.listdir(proc_dir)
os.chdir(proc_dir)
for file in mylist:
	#Cut the 13th column from the tabbed file to isolate the actual user review text
	cmd = 'cut -f13 '+file+' > '+file+'-processed.txt'
	os.system(cmd)
print(mylist)
