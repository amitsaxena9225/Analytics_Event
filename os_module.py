# will cover whole os module --corey Schafer

# importing os module
from os import open
import os
import re
from datetime import datetime

#it will give all attribute and methods inside os module.
print (dir(os))

#get current working directory 
print (os.getcwd())

#print
os.chdir(r'C:\Users\ab48915\Desktop\Python_Topics')  ## use double backslash or r
print (os.getcwd())

#print all dir

print (os.listdir("C:\\Users\\ab48915\\Desktop\\Python_Topics\\"))

#create new directory only

#print os.mkdir("New_Folder134",1)

#create new directory and sub directory under new Directory

#print os.makedirs(r'C:\Users\ab48915\Desktop\Python_Topics\Dir\subDir',1)

#remove folder

#os.rmdir(r'C:\Users\ab48915\Desktop\Python_Topics\New_Folder1234')

#remove folder and subfolder

#os.removedirs('')

#rename a file or folder
#os.rename(r"C:\Users\ab48915\Desktop\Python_Topics\Dir\subDir",r"C:\Users\ab48915\Desktop\Python_Topics\Dir\sy")

#info for a file/folder
print (os.stat(r"C:\Users\ab48915\Desktop\Python_Topics\Dir\sy"))

#particular info for a file/folder
print (os.stat(r"C:\Users\ab48915\Desktop\Python_Topics\Dir\sy").st_size )#it will give size 
print os.stat(r"C:\Users\ab48915\Desktop\Python_Topics\Dir\sy").st_atime # it will give last updated file time
#need humanreadable format time
var_1 =os.stat(r"C:\Users\ab48915\Desktop\Python_Topics\Dir\sy").st_atime
print datetime.fromtimestamp(var_1)

#walk ()method gives three value of tuple so'''

for dirpath,dirnames,filenames in os.walk(r'C:\Users\ab48915\Desktop'):
    
    print ('Current_path',dirpath)
    print ('Current_directory name',dirnames)
    print ('Current file name',filenames)

#check envrionment variable
print os.environ #o/p will come in dicitonary format

print os.environ.get('HOME')

#want to add file in home path

file_path = os.environ.get('HOME') + "C:\Users\ab48915\Desktop\Python_Topics\Dir\sy"
print file_path

#it will add this path to HOME directlty 
file_path1 =os.path.join(os.environ.get('HOME'),'C:\Users\ab48915\Desktop\Python_Topics\Dir\sy')
print file_path1

#it will give last name 
print os.path.basename("C:\Users\ab48915\Desktop\Python_Topics\Dir\sy")
#it will give directory name

print os.path.dirname("C:\Users\ab48915\Desktop\Python_Topics\Dir\sy")
#it will split directory and last folder/file name

print os.path.split("C:\Users\ab48915\Desktop\Python_Topics\Dir\sy") #o/p will be in tuple

print os.path.exists("C:\Users\ab48915\Desktop\Python_Topics\Dir\sy")

print os.path.isdir("C:\Users\ab48915\Desktop\Python_Topics\Dir\sy")# check is it directory 
print os.path.isfile("C:\Users\ab48915\Desktop\Python_Topics\Dir\sy")# check is it file 
print os.path.splitext("C:\Users\ab48915\Desktop\Python_Topics\Dir\sy")#split file and extension








