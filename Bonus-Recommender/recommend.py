import spacy
import operator

def get_next(strinput):
	#Load Spacy
	#nlp = spacy.load("en") 
	nlp = spacy.load("en_core_web_md")
	#Initialize filename
	filename = "items.txt"

	#Initialize dictionaries
	title_text = {}
	simranking = {}

	#Read file into 1st dictionary
	with open(filename) as f:
	    for line in f:
	       (key, val) = line.split(":")
	       title_text[str(key)] = val

	#Compare input text with text value of description from file
	for keys,values in title_text.items():
	    main_txt = nlp(strinput)
	    search_txt = nlp(str(values))
	    simranking.update( {str(keys) : main_txt.similarity(search_txt)} )


	#Return the Key (Item name) with the highest similarity score   
	return max(simranking.items(), key=operator.itemgetter(1))[0]



#Pass in input text
strinput = "refreshing deodorant Soap The invigorating scent opens your eyes while the thick, rich lather leaves you feeling fresh and clean"
print(get_next(strinput))
