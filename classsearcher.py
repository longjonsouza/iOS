import os
import sys
from datetime import datetime

if len(sys.argv) != 2:
    raise ValueError('Please provide the iOS app name.')
 
appname = sys.argv[1]
mynow = datetime.now().strftime("%m%d%Y%H%M%S")
classlistfilename = mynow + "_" + appname +"_classlist"

classstrings = ["Cert","SSL"]
methodstrings = ["Root", "Issue", "Cert","Pin"]
os.system("objection --gadget "+ appname +" run 'ios hooking list classes' > " + classlistfilename)
  
# opening a text file
classlistfile = open(classlistfilename, "r")
  
# setting flag and index to 0
flag = 0
index = 0
outputfile = open(appname+ "_" + mynow + "_output.txt","w+")  
# Loop through the file line by line
for line in classlistfile:  
    index += 1 
    for classstring in classstrings:
   # checking string is present in line or not
        if classstring in line:
            methodlistfilename = "methodlist_" + line.strip() + ".txt"
            os.system("objection --gadget "+sys.argv[1]+" run 'ios hooking list class_methods "+line.strip()+" --include-parents' > " + methodlistfilename)
            methodlistfile=open(methodlistfilename,"r")
            for methodline in methodlistfile:
                for methodstring in methodstrings:
                    if methodstring in methodline:
                        outputfile.write(line.strip() + "->" + methodline)
                        print(line.strip() +"->"+ methodline)
# closing text file   
classlistfile.close() 
methodlistfile.close()
outputfile.close() 
