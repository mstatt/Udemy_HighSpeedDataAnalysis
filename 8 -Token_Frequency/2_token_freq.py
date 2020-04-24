import os
import re
import glob
import spacy
import pdfkit
import pandas as pd
from collections import Counter
nlp = spacy.load('en')



def token_segment(filename):
	text = ''
	#Get base name
	basename = os.path.splitext(filename)[0]
	#Read file into "text" variable
	text = text + open(filename,'r').read()
	#Load text into Spacy document object.
	#Removing non-Ascii chars and lowercaseing the string to prevent duplicates
	doc = nlp(re.sub(r'[^\x00-\x7f]',r'', text.lower()))
	# Ignore stopwords, punctuations, empty spaces and replace newline characters
	words = [token.text.replace('\n', "").replace(' ', "").strip() for token in doc if token.is_stop != True and token.is_punct != True]
	#remove empty items from list
	words_cleaned = filter(lambda x: x != "", words)

	#Load sentences into a list
	sent_lst = []
	for i, token in enumerate(doc.sents):
	        sent_lst.append(token.text.replace('\n', "").strip())


	#remove empty items from list
	sent_cleaned = filter(lambda x: x != "", sent_lst)
	#Load sentences counter and dataframe
	sent_freq = Counter(sent_cleaned)
	#Load most common sentences
	slst = sent_freq.most_common()
	#Load list into dataframe
	sdf = pd.DataFrame.from_dict(slst)
	#Add column names
	sdf2 = sdf.rename(columns={0:'Sentence', 1:'Count'})
	#Remove sentences appearing only once
	sdf3 = sdf2[sdf2.Count != 1]


	#Load word counter and dataframe
	word_freq = Counter(words_cleaned)
	#Load most common words
	lst = word_freq.most_common()
	#Load list into dataframe
	df = pd.DataFrame.from_dict(lst)
	#Add column names
	df2 = df.rename(columns={0:'Word', 1:'Count'})
	#Remove words appearing only once
	df3 = df2[df2.Count != 1]


	#Build html files for .pdf generation
	df3.to_html(open(basename+'_word_count.html', 'w'))
	pdfkit.from_file(basename+'_word_count.html',basename+'_Word_Count-Analysis.pdf')
	#Build html files for .pdf generation
	sdf3.to_html(open(basename+'_sent_count.html', 'w'))
	pdfkit.from_file(basename+'_sent_count.html',basename+'_Sent_Count-Analysis.pdf')

	#Delete the html files
	if os.path.exists(basename+'_word_count.html'):
	    os.remove(basename+'_word_count.html')

	if os.path.exists(basename+'_sent_count.html'):
	    os.remove(basename+'_sent_count.html')




proc_dir = os.getcwd()+'//to_process//'
for filename in glob.glob(proc_dir+"*.txt"):
	#Parse file for tokens and output
	token_segment(filename)
	
#Signal Process Completion
print('Count process completed.')



