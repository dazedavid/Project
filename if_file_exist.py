import os.path
from os import path
from pathlib import Path
def main():

   print ("File exists:"+str(path.exists('abc.txt')))
   print ("File exists:" + str(path.exists('xyz.txt')))
   print ("directory exists:" + str(path.exists('Python')))

if __name__== "__main__":
   main()

#if file does not exist create file 

check = (str(path.exists('abc.txt')))

if check == str('True'):
    print ("The file exist")
else: 
    Path('abc.txt').touch()