import os
import re
import pdfkit
import pandas as pd
import collections
from pytesseract import image_to_string
from PIL import Image



def gettext(inputfilename):
	#Get the base name of the image
	basename = os.path.splitext(inputfilename)[0]
	#Read in the image contents
	txtstring = image_to_string(Image.open(inputfilename), lang='eng')
	#Remove non-ASCII characters
	text = re.sub(r'[^\x00-\x7f]',r'', txtstring)
	#Create text file and output imge contents
	with open (basename+"_text.txt","w")as fp1:
		fp1.write(text)
	fp1.close()
	#Return extracted text
	return text


proc_dir = os.getcwd()+'//to_process//'
#Assign file names in the directory to a list for processing
mylist2 = os.listdir(proc_dir)
#Sort the list
mylist2.sort()
ne_cnt =1
image_text = {}
#Grab all files in the directory.
for file in mylist2:
    #Print name of the file currently being processed
        print('Image Text extraction processing '+str(file))
    # Pass each image file to the gettext function to extract the text
        image_text[str(file)] = gettext(proc_dir + file)
        ne_cnt = ne_cnt +1


#Build the ordered dictionary
odimagetext = collections.OrderedDict(image_text.items())
#Pass the dictionary into a Pandas Dataframe
dfimagetext = pd.DataFrame.from_dict(odimagetext, orient='index').reset_index()
pd.set_option('display.max_colwidth', 100)
dfimagetext = dfimagetext.replace('\n',' ', regex=True)
dfimagetext.style.set_table_styles([dict(selector="th",props=[('max-width', '50px')])])
dfimagetext = dfimagetext.rename(columns={'index':'Imagefile', 0:'Extracted Text'})
dfimagetext = dfimagetext.sort_values(by ='Imagefile')
#Write the dataframe to an html page
dfimagetext.to_html(open(proc_dir+'image_text.html', 'w'))
#Generate a pdf from the html file of Dataframes
pdfkit.from_file(proc_dir+'image_text.html',proc_dir+'Image_Text_Extraction.pdf')
#Delete the html file
if os.path.exists(proc_dir+'image_text.html'):
    os.remove(proc_dir+'image_text.html')
print('Image text extraction process completed.')
