import os
import spacy
import pdfkit
import pandas as pd
from collections import Counter
nlp = spacy.load('en')


text = ''
proc_dir = os.getcwd()+'//to_process//'
mylist = os.listdir(proc_dir)
os.chdir(proc_dir)

#Delete previously run analysis files:
if os.path.exists('Word_Count-Analysis.pdf'):
    os.remove('Word_Count-Analysis.pdf')
if os.path.exists('Sent_Count-Analysis.pdf'):
    os.remove('Sent_Count-Analysis.pdf')


#Read files into "text" variable
for file in mylist:
	if file.endswith('.txt'):
		text = text + open(file,'r').read()


#Load text into Spacy document object.
#Removing newline chars and lowercaseing the string
doc = nlp(text.lower())
# Ignore stopwords and punctuations
words = [token.text.replace('\n', " ") for token in doc if token.is_stop != True and token.is_punct != True]


#Load sentences into a list
sent_lst = []
for i, token in enumerate(doc.sents):
        sent_lst.append(token.text.replace('\n', " "))


#Load sentences counter and dataframe
sent_freq = Counter(sent_lst)
slst = sent_freq.most_common()
sdf = pd.DataFrame.from_dict(slst)
sdf2 = sdf.rename(columns={0:'Sentence', 1:'Count'})
sdf3 = sdf2[sdf2.Count != 1]

#Load word counter and dataframe
word_freq = Counter(words)
lst = word_freq.most_common()
df = pd.DataFrame.from_dict(lst)
df2 = df.rename(columns={0:'Word', 1:'Count'})
df3 = df2[df2.Count != 1]
#df4 = df3.sort_values(by ='Count', ascending=False)


#Build html files for .pdf generation
df3.to_html(open('word_count.html', 'w'))
pdfkit.from_file('word_count.html','Word_Count-Analysis.pdf')
#Build html files for .pdf generation
sdf3.to_html(open('sent_count.html', 'w'))
pdfkit.from_file('sent_count.html','Sent_Count-Analysis.pdf')

#Delete the html files
if os.path.exists('word_count.html'):
    os.remove('word_count.html')

if os.path.exists('sent_count.html'):
    os.remove('sent_count.html')


#Signal Process Completion
print('Count process completed.')



