import os
import shutil

from_dir = "Users/michaes/Downloads/" #pls input different directories
to_dir = "Users/michaes/Desktop/" #pls input different directories

for file_name in os.listdir(from_dir):
    if file_name.endswith(".pdf") !="":
        ext = os.path.splitext(file_name)[-1]
        if ext in ['.pdf']:

                path1 = from_dir + '/' + file_name 
                
                to_dir_ext = to_dir + "/" + "Document_Files" 
                
                path2 = to_dir_ext 
                
                path3 = to_dir_ext + '/' + file_name 
                
                if os.path.exists(path2): 
                    print(f"Moving file {file_name} to {path3} ") 
                    shutil.move(path1, path3) 
                
                else: 
                    os.makedirs(path2) 
                    print(f"Moving file {file_name} to {path3} ") 
                    shutil.move(path1, path3) 
    print("Files moved successfully!")

    