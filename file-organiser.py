import os 
import shutil as sh
import time 

# system folder files path 
path = r'C:\Users\parve\Downloads'
files_path = os.listdir(path)

# define the destination system folder 

D_path = os.listdir("D:")

#file dictionary to compare with the system files 

file_name_dictionary = {
    "PDF" : [".pdf"],
    "Document" : [".docx" , ".txt"] ,
    "Spreadsheet" : [".xlsx", ".csv"],
    "Presentation" :[".pptx"],
    "Pictures" : [".jpg", ".jpeg", ".png" , ".gif", ".webp"],
    "Movies": [".mp4", ".mkv", ".webm"],
    "Music" : [".mp3", ".wav"],
    "Archive / ZIP" : [".zip", ".rar", ".7z"],
    "Software / Installer" : [".exe", ".msi", ".apk"],
    "Chrome Temporary Download" : [".crdownload"]
}

count = 0

# loop : split the file and extension into two parts 
for file in files_path:
    primary_name , extension = os.path.splitext(file)
    Extension = extension.lower()
    # store the folder name and extension list from the dictionary
    for category , ext_list in file_name_dictionary.items():
        # iterate all the extension from the extension list 
        for ext in ext_list:
            # compare system file folder extension with the dictionary file extension 
            if Extension == ext:
                print("Extension Matched !")
                # after match , add system folder path with the matched file that creates new system folder path 
                src = os.path.join(path,file)
                # searching folder in D disk to move file 
                for folder in D_path:
                    if folder == category :
                        destination = os.path.join("D:\\" , category,file)
                        time.sleep(3)
                        print("Files Moved in few Seconds !")
                        moving = sh.move(src,destination)
                        print("your files are moved from another folder !")
                count = count+1
                print(f"file moved : {count}")
                        
print("organizer have ran successfully !")         