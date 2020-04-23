import os
import gc
from datetime import datetime
import pandas as pd 
import matplotlib.pyplot as plt 
from wordcloud import WordCloud, STOPWORDS 



text = ''
now = datetime.now()
currentDT = now.strftime("%m%d%Y-%H%M%S")
proc_dir = os.getcwd()+'//to_process/'
mylist = os.listdir(proc_dir)
os.chdir(proc_dir)
 
#Read files into "text" variable
for file in mylist:
	#Load only text files (in case there are .pdf's still in the directory)
	if file.endswith('.txt'):
		text = text + open(file,'r').read()



# Create the wordcloud object with Red words.
wordcloud = WordCloud(width=480, height=480, colormap="Blues", background_color="black").generate(text)
 
# Display the generated image:
fig = plt.figure()
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.margins(x=0, y=0)
plt.show()
#Save image as .pdf with time prefix
fig.savefig(str(currentDT) +'_tag_cloud.pdf')

gc.collect()
