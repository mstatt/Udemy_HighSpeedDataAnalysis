import os
import glob
import docx
from docx import Document
import shutil

def extract_Text_doc(docdir):

    print("Starting Text Extraction for word doc's......")
    number_of_files = str(len([item for item in os.listdir(docdir) if os.path.isfile(os.path.join(docdir, item))]))
    print("Processing ("+ number_of_files + ") .docx files.....")

    for filename3 in glob.glob(docdir+"*.docx"):
        #Get the filename without the extension for nameing later
        base=os.path.basename(filename3)
        filenameNoExt = os.path.splitext(base)[0]
        doc = docx.Document(filename3)
        fullText = []
        for para in doc.paragraphs:
            fullText.append(para.text)
        textstream = '\n'.join(fullText)
        # content_list = list(filter(None, content_list))
        with open (docdir+'doc_'+filenameNoExt+".txt","a")as fp11:
            fp11.write(textstream)
            fp11.close()
    print("Writing extracted doc output files ***************************************")
    print("Text extraction completed for ("+ number_of_files + ") .docx files  ******************************")




word_files = 'to_process/'
extract_Text_doc(word_files)