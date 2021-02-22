from zipfile import ZipFile
import os
from pathlib import Path
import zipfile
import shutil

#from time import sleep

'''
This script extracts from any instrument that you want from the zip files (and also non zipped files for the 
instrument)and merges all of them to a single file. This also removed duplicate lines in the merged file 

STEPS to follow to extract data for any instruments

1. Go to the following google drive where RM Sharma has generously shared the 1 min data from 2008 till date
https://drive.google.com/drive/folders/0B8mlk4xRW1kOVkk0M3FVR0M0aEE
2. Right click and download this folder. GDrive will zip and download this. THis will take time depending on the
internet speed. It is almost 2GB
3. On your computer, unzip this big file once it is downloaded
4. Give the path of your folder where you have unzipped below
5. Mention the instrument name that you want to extract, merge and remove duplicates

'''

##use this https://www.btelligent.com/en/blog/best-practice-working-with-paths-in-python-part-2/

#Update the path of the folder where you unzipped the large file downloaded from gdrive
input_path = 'C:/Users/STYLETAG/Downloads/one_minutedata-20210210T102058Z-001/oneminutedata/2021/'

#Update the path where you want to extract the files
output_path = "C:/Users/STYLETAG/Downloads/2021/"

#Update the name of the instrument that you want to extract
instrument_name = "NIFTY.txt"

#update the path of the merged final file where you want to store
output_merged_file_path = "C:/Users/STYLETAG/Downloads/"

#IMPORTANT - Ensure that the path you give above is correct.

#print(instrument_name, input_path)
#for recursively traversing directories https://stackoverflow.com/questions/16953842/using-os-walk-to-recursively-traverse-directories-in-python

def walk_error_handler(exception_instance):
    print("Check the folder path.. Cannot find !")
    exit(1)

for dirpath, dirnames, filenames in os.walk(input_path, onerror=walk_error_handler):
    for item in filenames:
        if item.endswith('.zip'):
            #print(dirpath/item)
            filename_with_full_path = dirpath + "/" + item
            # Create a ZipFile Object and load sample.zip in it
            zip_file = zipfile.ZipFile(filename_with_full_path, 'r')
            for name in zip_file.namelist():

                #use the rsplit to get the instrument name and seperate zip file \txtfile - 03FEB\NIFTY_F1.txt
                #https://www.w3schools.com/python/ref_string_rsplit.asp
                #print(name)
                if '/' in name :
                    current_instrument_name = name.rsplit('/', 1)[1]
                else:
                    current_instrument_name = name

                if current_instrument_name == instrument_name:
                    #use the join method to get the path right https://www.geeksforgeeks.org/python-os-path-join-method/
                    file_name_with_path = os.path.join(dirpath, Path(name))
                    #print(file_name_with_path)
                    #replace the input_path with the new output path and get the new path
                    #https://stackoverflow.com/questions/27258720/replace-part-of-path-python
                    output_filename_with_path = Path(file_name_with_path.replace(file_name_with_path[:file_name_with_path.index("oneminutedata")], output_path))
                    #print(output_filename_with_path)
                    # Need to get the file path https://stackoverflow.com/questions/8384737/extract-file-name-from-path-no-matter-what-the-os-path-format
                    head = Path(os.path.split(output_filename_with_path)[0])
                    #print(head)
                    #now make directory if it doesnt exist https://stackoverflow.com/questions/23793987/write-file-to-a-directory-that-doesnt-exist
                    head.mkdir(parents=True, exist_ok=True)

                    #Now extract the particular file to the directory that we want
                    #if directory is not existing create it..

                    zip_file.extract(name,head,pwd=None)

            zip_file.close()

        elif (str(item) == instrument_name):
            file_name_with_path = os.path.join(dirpath, Path(item))
            #print(file_name_with_path)
            # replace the input_path with the new output path and get the new path
            # https://stackoverflow.com/questions/27258720/replace-part-of-path-python
            output_filename_with_path = Path(file_name_with_path.replace(file_name_with_path[:file_name_with_path.index("oneminutedata")],output_path))
            #print(output_filename_with_path)
            # Need to get the file path https://stackoverflow.com/questions/8384737/extract-file-name-from-path-no-matter-what-the-os-path-format
            head = Path(os.path.split(output_filename_with_path)[0])
            #print(head)
            # now make directory if it doesnt exist https://stackoverflow.com/questions/23793987/write-file-to-a-directory-that-doesnt-exist
            head.mkdir(parents=True, exist_ok=True)
            #print(head)
            #copy from one location to another - https://www.tutorialspoint.com/How-to-copy-files-from-one-folder-to-another-using-Python
            shutil.copy(file_name_with_path, head)


#lets merge the extracted files
#used this https://stackoverflow.com/questions/13613336/python-concatenate-text-files

input_file_path = output_path
output_merged_file = output_merged_file_path + "merged_" + instrument_name

with open(output_merged_file, 'w') as outfile:
  for dirpath, dirnames, filenames in os.walk(input_file_path):
    for item in filenames:
      if  (str(item) == instrument_name):
        file_name_with_path = Path(os.path.join(dirpath, item))
        #print(file_name_with_path)
        with open(file_name_with_path) as infile:
          for line in infile:
              outfile.write(line)
outfile.close()


#Now lets remove duplicates
# Use this - https://www.codevscolor.com/python-remove-duplicate-lines-text-file
import hashlib

#1
input_file_path = output_merged_file
output_file_path = output_merged_file_path+"merged_removed_duplicate_"+instrument_name

#2
completed_lines_hash = set()

#3
output_file = open(output_file_path, "w")

#4
for line in open(input_file_path, "r"):
  #5
  hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
  #6
  if hashValue not in completed_lines_hash:
    output_file.write(line)
    completed_lines_hash.add(hashValue)
#7
output_file.close()