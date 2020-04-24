import os
import re
import glob



#Set process directory
proc_dir = os.getcwd()+'//to_process//'
#Create list
content_list = []
#Get list of all .csv's in the directory
for filename in glob.glob(proc_dir+"*.csv"):
	with open(filename) as f:
		#Get basename without file extension
		basename = os.path.splitext(filename)[0]
		#Read the file into a list on lines
		content_list = f.readlines()
	f.close()


	#Write output to text file
	with open (basename+"_keywords.txt","a")as fp1:
		#Loop trough list 
		for line in content_list:
			#Extract only the keywords by setting the start and end chars.
			#We do it this way because they have placed commas within the variable length keywords.
			#This is not the most dynamic way of accomplishing this, but it works
			start = line.find("[")
			end = line.find("]")
			line2 = line[start:end+1]
			#and remove non-Ascii chars
			content2 = re.sub(r'[^\x00-\x7f]',r'', line2)
			#Write output to file
			fp1.write(content2)
		
	#close the file
	fp1.close()


