import os 
import shutil
source= input("Enter the source name")
destination= input("Enter the destination name")
source = source+"/"
destination = destination+"/"
list_of_files=os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file), destination)