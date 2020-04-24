 
import os
import re
import spacy
import pdfkit
import pandas as pd
import collections
from spacy import displacy 
from datetime import datetime 



def getnames(inputfilename):
	#Read in the file contents
    f = open(inputfilename)
    txtstream = f.read()
    f.close()
    lst = []
    text = re.sub(r'[^\x00-\x7f]',r'', txtstream)
    nlp = spacy.load("en")
    doc = nlp(text)
    for ent in doc.ents:
    	"""
    	Grab only the labeled entities you want,
    		PERSON: People, including fictional. 
    	    NORP: Nationalities or religious or political groups.
    	    ORG: Companies, agencies, institutions, etc.
    	    GPE: Countries, cities, states. 
    	    EVENT: Named hurricanes, battles, wars, sports events, etc.

            Example to extract only people:
            if (ent.label_ == 'PERSON'):
    	 """
         #Extract Organizations, People and Countries
    	if (ent.label_ == 'ORG' or ent.label_ == 'PERSON' or ent.label_ == 'GPE'):
    		lst.append(''.join([c[0] for c in ent.text]))

    names = list(dict.fromkeys(lst))
    final_names = ', '.join(map(str, names))
    return final_names



now = datetime.now() 
date_time = now.strftime("%m-%d-%Y-%H%M%S")
#Get all of the files (.txt) in the directory into a list
txt_files = list(filter(lambda x: x.endswith('.txt'), os.listdir('to_process/')))
txt_files.sort()
total_txt_cnt = len(txt_files)
names_entities = {}



#Grab all files in the directory.
for file in txt_files:
    #Load only text files (in case there are .pdf's still in the directory)
    if file.endswith('.txt'):
    #Print name of the file currently being processed
        print('Name Entity extraction processing '+str(file))
    # Pass each file to the Getnames function to extract the entities
        names_entities[str(file)] = getnames('to_process/'+ file)


#Build the ordered dictionary
odnames = collections.OrderedDict(names_entities.items())
#Pass the dictionary into a Pandas Dataframe
dffileentities = pd.DataFrame.from_dict(odnames, orient='index').reset_index()
pd.set_option('display.max_colwidth', 100)
dffileentities.style.set_table_styles([dict(selector="th",props=[('max-width', '50px')])])
dffileentities = dffileentities.rename(columns={'index':'Filename', 0:'Named Entities Found'})
dffileentities = dffileentities.sort_values(by ='Filename')
#Write the dataframe to an html page
dffileentities.to_html(open('dfNameEntities.html', 'w'))
#Generate a pdf from the html file of Dataframes
pdfkit.from_file('dfNameEntities.html',date_time +'NER-Analysis.pdf')
#Delete the html file
if os.path.exists('dfNameEntities.html'):
    os.remove('dfNameEntities.html')
print('Name Entity extraction process completed.')