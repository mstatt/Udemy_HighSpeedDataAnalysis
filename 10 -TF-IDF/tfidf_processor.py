# -*- coding: utf-8 -*-
def tfidf_calc(x):
    import os
    import glob
    import shutil
    import math
    import nltk
    import pdfkit
    #nltk.download('stopwords')
    from textblob import TextBlob as tb
    from nltk.corpus import stopwords


    cachedStopWords = stopwords.words("english")

    compdir =  x + '/'
    numofwords = 20
    #To calculate process completion %
    def getpercent(num,num2):
        return (num/num2)*100

    def tf(word, blob):
        return blob.words.count(word) / len(blob.words)

    def n_containing(word, bloblist):
        return sum(1 for blob in bloblist if word in blob.words)

    def idf(word, bloblist):
        return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

    def tfidf(word, blob, bloblist):
        return tf(word, blob) * idf(word, bloblist)

    number_of_files = str(len([item for item in os.listdir(compdir) if os.path.isfile(os.path.join(compdir, item))]))
    print("Processing ("+ number_of_files + ") files for TFIDF.....")
    #Create a blob list for the words
    bloblist = []
    #List of files
    filename_listtf = []
    print("Building list and stream for TFIDF calculation......")
    #Run through the directory and process each text file in the directory
    for filename2tf in sorted(glob.glob(compdir+"*.txt")):
        with open(filename2tf, 'r') as myfile2tf:
        	#Joining the lines of the file, stripping trailing whitespace and making them uppercase
            initstream = "".join(line.rstrip() for line in myfile2tf).upper()
            #loading the words from the text blob object that are not stop words
            txtstreamtf =tb(" ".join([word for word in initstream.split() if word not in cachedStopWords]))
            #Adding the basename without the directory path to the file list
            filename_listtf.append(os.path.basename(filename2tf))
            #Adding the text stream to the blob list
            bloblist.append(txtstreamtf)
            myfile2tf.close()


    print("Writing web page for TFIDF calculation......")
    #Open the html output file for writing
    with open (compdir+"tfidf.html","a",encoding="utf-8")as fp1tfidf:
        fp1tfidf.write("<!DOCTYPE html><html><!DOCTYPE html><html lang='en'><head><title>TF/IDF Calculation</title></head><body>")
        fp1tfidf.write("<table border=1>")
        total = len(bloblist)
        for i, blob in enumerate(bloblist):
            fp1tfidf.write("<tr><td colspan=2>")
            fp1tfidf.write("Top words "+ str(numofwords) +" in document {}".format(filename_listtf[i]))
            fp1tfidf.write("</td></tr>")
            #Alert the user to the % processed 
            print('Process status:  [%d%%]\r'%getpercent(i,total), end="")
            #The actual Term frequency processing is done
            scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
            #Sort the scores from highest to lowest
            sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
            #write the output to html page
            for word, score in sorted_words[:numofwords]:
            	#Loop through the list of words, writing them out to the html table
                fp1tfidf.write("<tr><td>")
                fp1tfidf.write("\tWord: {}</td><td> TF-IDF: {} </td></tr>".format(word, round(score, 5)))
            fp1tfidf.write("</tr>")

        fp1tfidf.write("</table></body></html>")
    fp1tfidf.close()

    #Generate a pdf from the html file 
    pdfkit.from_file(compdir+"tfidf.html",compdir+'TF-IDF-Analysis.pdf')
    #Delete the html file
    if os.path.exists(compdir+"tfidf.html"):
    	os.remove(compdir+"tfidf.html")

    print("TF/IDF calculation completed on ("+ number_of_files + ") files******************************")





#**************2 File minimum to execute TF-IDF
#Call the function passing in the directory.
tfidf_calc('to_process')