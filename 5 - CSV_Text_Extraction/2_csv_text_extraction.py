import os
import re
import glob
import pdfkit
import pandas as pd


proc_dir = os.getcwd()+'//to_process//'
#Get list of all .csv's in the directory
for filename in glob.glob(proc_dir+"*.csv"):
	#Get basename without file extension
	basename = os.path.splitext(filename)[0]
	data = pd.read_csv(filename) 
	#Load Data into dataframe
	df = pd.DataFrame(data)
	#Create a new dataframe containing only the columns we want.
	df2 = df[['headline', 'keywords']]
	#Export the df to an html file
	df2.to_html(open(proc_dir+'1.html', 'w'))
	#Create a .pdf from the html file
	pdfkit.from_file(proc_dir+'1.html',basename+'_out.pdf')
	#Delete the html file
	if os.path.exists(proc_dir+'1.html'):
		os.remove(proc_dir+'1.html')




