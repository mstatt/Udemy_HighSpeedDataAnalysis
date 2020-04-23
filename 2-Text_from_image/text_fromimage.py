import os
from pytesseract import image_to_string
from PIL import Image

#Extract text from a specific image
txtstring = image_to_string(Image.open('to_process/Course_Description.png'), lang='eng')
#Write extracted text to output file
with open ("example_03.jpg.txt","w")as fp1:
	fp1.write(txtstring)
fp1.close()

print('Process completed')
