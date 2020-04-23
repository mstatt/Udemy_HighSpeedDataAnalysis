#Run This 2nd
import os
import glob
import pathlib
import pandas as pd


proc_dir = os.getcwd()+'//to_process//'
#Assign file names in the directory to a list for processing
mylist2 = os.listdir(proc_dir)
#Sort the list alphabetically
mylist2.sort()
#Change directories into to_process
os.chdir(proc_dir)
#Load the files into a new file for formatting.
with open('File_List.txt', 'w') as f:
    for item in mylist2:
        f.write("%s\n" % item)

f.close()


# GO through and remove any double quotes from files
for file in mylist2:
	with open(file, 'r') as myfile2:
            data2="".join(line for line in myfile2)
            myfile2.close()
            #Ensure our file in properly encoded
            with open (os.path.basename(file),"a",encoding="utf-8")as fp1:
                fp1.write(data2.replace('"', ''))
            fp1.close()

#Below we load the file into a Pandas Dataframe for seperation and output to the correct file based on star rating.

#Generate 5 star rating file
for file in mylist2:
	df = pd.read_table( file,names = ["Title", "Rating", "Body"]) #read in the file
	df = df[df.Rating == 5] #select the rows where column 2 = 5 [col 2 is the rating and 5 is the stars]
	df.to_csv( file[:-4] +'_5_star_reviews.txt', sep='\t', index=False, header=None) #write the output to a tab-separated file
	lst = [df]
	del lst


#Generate 4 star rating file
for file in mylist2:
	df = pd.read_table( file,names = ["Title", "Rating", "Body"]) #read in the file
	df = df[df.Rating == 4] #select the rows where column 2 = 4 [col 2 is the rating and 4 is the stars]
	df.to_csv( file[:-4] +'_4_star_reviews.txt', sep='\t', index=False, header=None) #write the output to a tab-separated file
	lst = [df]
	del lst


#Generate 3 star rating file
for file in mylist2:
	df = pd.read_table( file,names = ["Title", "Rating", "Body"]) #read in the file
	df = df[df.Rating == 3] #select the rows where column 2 = 3 [col 2 is the rating and 3 is the stars]
	df.to_csv( file[:-4] +'_3_star_reviews.txt', sep='\t', index=False, header=None) #write the output to a tab-separated file
	lst = [df]
	del lst



#Generate 2 star rating file
for file in mylist2:
	df = pd.read_table( file,names = ["Title", "Rating", "Body"]) #read in the file
	df = df[df.Rating == 2] #select the rows where column 2 = 2 [col 2 is the rating and 2 is the stars]
	df.to_csv( file[:-4] +'_2_star_reviews.txt', sep='\t', index=False, header=None) #write the output to a tab-separated file
	lst = [df]
	del lst



#Generate 1 star rating file
for file in mylist2:
	df = pd.read_table( file,names = ["Title", "Rating", "Body"]) #read in the file
	df = df[df.Rating == 1] #select the rows where column 2 = 1 [col 2 is the rating and 1 is the stars]
	df.to_csv( file[:-4] +'_1_star_reviews.txt', sep='\t', index=False, header=None) #write the output to a tab-separated file
	#df.to_html(open(file+'.html', 'w'))
	lst = [df]
	del lst
	os.remove(file)

os.remove('File_List.txt')
