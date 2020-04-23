import os
import re
import pdfkit
import difflib
import itertools
import collections
import pandas as pd
from datetime import datetime 
now = datetime.now() 
date_time = now.strftime("%m-%d-%Y-%H%M%S")

     

def getpercent(num,num2):
    return (num/num2)*100


def compareEach(x,y):
    """
    Compare the 2 files passed in using fuzzy string compare
    """
    with open('to_process/'+x, 'r') as myfile:
        data=myfile.read().replace('\n', '').lower()
        myfile.close()
    with open('to_process/'+y, 'r') as myfile2:
        data2=myfile2.read().replace('\n', '').lower()
        myfile2.close()

    return difflib.SequenceMatcher(None, data, data2).ratio()




#Get all of the files (.txt) in the directory into a list
txt_files = list(filter(lambda x: x.endswith('.txt'), os.listdir('to_process/')))
txt_files.sort()
comparecount = 1
#Grab all files in the directory.
for file in txt_files:
    #Only execute if the files count is more than 1
        if (len(txt_files)> 1):
            #Set up lists for file names and Fuzzy logic calculations
            aList = []
            filesim1 = []
            filesim2 = []
            total_operations = len(txt_files) * len(txt_files)
            bList = []
            qr = 1
            #Loop through each list item and compare it against the other items
            for a, b in itertools.combinations(txt_files, 2):
                comparecount = comparecount + 1
                aList.append("File ["+a+"] <> ["+b+"] ");
                filesim1.append(a)
                filesim2.append(b)
                bList.append(compareEach(a,b));
                print('Compare files process status:  [%d%%]\r'%getpercent(qr,total_operations), end="")
                qr = qr + 1


#Combine both lists into a corolary dictionary
d = dict(zip(aList, bList))

#Save sorted dict as new dictionary from most similar to least
d1 = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))

odsimilar = collections.OrderedDict(d1.items())
dfsimilar = pd.DataFrame.from_dict(odsimilar, orient='index').reset_index()
dfsimilar = dfsimilar.rename(columns={'index':'Files Comparison', 0:'Score'})
dfsimilar.to_html(open('filesimilarities.html', 'w'))
pdfkit.from_file('filesimilarities.html',date_time +'File-Similarity-Analysis.pdf')
#Delete the html file
if os.path.exists('filesimilarities.html'):
    os.remove('filesimilarities.html')
print('File Similarity process completed.')