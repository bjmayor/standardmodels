import shutil
import os
backup= os.path.join(os.getcwd(),"backup")
if not os.path.exists(backup):
   os.mkdir(backup)
for file in os.listdir("."):
    if os.path.splitext(file)[1] == ".py":
        print file
        shutil.copy(file, os.path.join("backup", file))