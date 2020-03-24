import os.path
from os import path
from pathlib import Path

# Function check if file exist else CREATES NEW ONE 

def main(file_test):
   logic = (str(path.exists(file_test)))
   if logic == str('True'):
      print ("File exists:"+logic)
   else:
      Path(file_test).touch()

   
# Main Body    
b = input("enter file name with extension:")

main(b)
