import pandas as pd
import matplotlib.pyplot as plt
import pydotplus
import re


caminhoBase = "data/database/database.csv"
df = pd.read_csv(caminhoBase)

data = df['ebairrnome'].to_string()


findlist = ['\n']
replacelist = [","]

def findReplace(find,replace):
    
    for item, replacement in zip(findlist,replacelist):
        s = data.replace(item,replacement)
      
    return s


findnumber = [" "]
replacenumber = [""]

    
lists = findReplace(findlist,replacelist)
def cleanNumber(find,replace):
    
    for item, replacement in zip(findnumber,replacenumber):
        
        s= re.sub("\d","",lists)
        b = s.replace(item,replacement)
      
    return b
c = cleanNumber(findnumber,replacenumber)



with open("Output.txt", "w") as text_file:
    text_file.writelines(c)
