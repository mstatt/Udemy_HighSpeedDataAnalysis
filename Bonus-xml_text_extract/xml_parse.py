import os
import glob
from bs4 import BeautifulSoup


#Data obtained from (https://archive.ics.uci.edu/ml/machine-learning-databases/00239/)
#More information about the dataset is located in the readme.txt file

# Set the URL you want to webscrape from
def xml_text(filename):
#Get the base name of the image
	basename = os.path.splitext(filename)[0]
	articletext = ''
	# Load the xml file as a soup object for parsing
	with open(filename) as fp:
	    soup = BeautifulSoup(fp, 'xml')

	#Grab the specific tag we need for text extraction
	article_news = soup.find_all('sentence')

	#Combine all of the sentence tags text into a single var with a newline seperator.
	for s in article_news:
		articletext = articletext + s.get_text() + '\n'

	#Output the text to a file in the same folder.
	with open(basename+"_xml.txt", "w") as text_file:
	    text_file.write(articletext)



proc_dir = os.getcwd()+'//to_process//'
#Loop through the directory using glob to obtain only .xml files
for file in glob.glob(proc_dir+"*.xml"):
	#Call function to extract text from file
	xml_text(file)
