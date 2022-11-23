import pandas as pd
import csv

files = "data/controller/controller_social.csv"

f = open(files)
csv_f = csv.reader(f)

findlist = [',']
replacelist = [',\n']

def findReplace(find,replace):
    s = f.read()
    for item, replacement in zip(findlist,replacelist):
        s = s.replace(item,replacement)
        
    return s
    
lists = findReplace(findlist,replacelist)
print(lists)

with open("Output.csv", "w") as text_file:
    text_file.writelines(lists)

f.close()