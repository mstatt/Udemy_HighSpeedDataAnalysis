import os
import glob
import pathlib
import shutil

proc_dir = os.getcwd()+'//to_process//'

outfilename = 'Sentences.txt'
with open(outfilename, 'wb') as outfile:
    for filename in glob.glob(proc_dir+'*.txt'):
        if filename == outfilename:
            # don't want to copy the output into the output
            continue
        with open(filename, 'rb') as readfile:
            shutil.copyfileobj(readfile, outfile)
