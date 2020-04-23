import os
import re
import sys
import glob
import shutil
import pdftotext


def extract_Text_pdf(pdfdir):

    print("Starting Text Extraction for pdf files......")

    number_of_files = str(len([item for item in os.listdir(pdfdir) if os.path.isfile(os.path.join(pdfdir, item))]))
    print("Processing ("+ number_of_files + ") .pdf files.....")
    os.chdir(pdfdir)
    file_list2 = []
    for filename in glob.glob("*.pdf"):
        #Get the filename without the extension for nameing later
        base=os.path.basename(filename)
        filenameNoExt = os.path.splitext(base)[0]
        #Create a list of the text files
        file_list2.append("pdf_"+filenameNoExt+".txt")
        with open(filename, "rb") as f:
            pdf = pdftotext.PDF(f)

        filecontents = re.sub(' +', ' ', " ".join(pdf).replace("\n"," ").strip())
        #Remove Non ASCII characters
        filecontents2 = re.sub(r'[^\x00-\x7f]',r'', filecontents)
        # content_list = list(filter(None, content_list))
        with open ("pdf_"+filenameNoExt+".txt","a")as fp1:
            fp1.write(filecontents2)
        fp1.close()

    print("Text extraction completed for ("+ number_of_files + ") .pdf files ********************")



pdf_files = 'to_process/'
extract_Text_pdf(pdf_files)