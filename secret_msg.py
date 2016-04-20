import os
import re
files=os.listdir("prank/")
print("List of files:")
print (files)
original_path=os.getcwd()
path_prank=os.getcwd()+"/prank"
print("current working directory:" + original_path)
os.chdir(path_prank)
for file in files:
    os.rename(file,re.sub("0123456789","",file))
    print("New file name:" + file)

os.chdir(original_path)