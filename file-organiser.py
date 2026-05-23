import os 
import shutil as sh
import time 

path = r'C:\Users\parve\Downloads'
files_path = os.listdir(path)
d = "D:"
d_path = os.listdir(d)
checking = os.path.getsize(d)
print(checking)

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
for file in files_path:
    primary_name , extension = os.path.splitext(file)
    Extension = extension.lower()
    for category , ext_list in file_name_dictionary.items():
        for ext in ext_list:
            if Extension == ext:
                print("Extension Matched !")
                src = os.path.join(path,file)
                for folder in d_path:
                    if folder == category :
                        destination = os.path.join("D:\\" , category,file)
                        checking = os.path.exists(destination)
                        time.sleep(3)
                        print("Files Moved in few Seconds !")
                        moving = sh.move(src,destination)
                        print("your files are moved from another folder !")
                        
    

            