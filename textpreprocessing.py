# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 21:18:05 2022

@author: iceb0
"""
import os 
import pandas as pd
from nltk.corpus import stopwords
import nltk

# file chooser gui 
def open_file_tk():
    from tkinter import Tk     # from tkinter import Tk for Python 3.x
    from tkinter.filedialog import askopenfilename
    
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)
    return filename 

# select sheet from excel
def get_sheets(file):
    # determine sheets within the file
    print("\n\nAvailable sheet(s): '%s'" % file.sheet_names)
    sheetname = input("\nSpecify the sheet name to open: ")
    
    # Load selected sheet
    df = pd.read_excel(file, sheet_name=sheetname)
    print("Selected sheet: ", sheetname)        
    return df

# remove common punctuations    
def remov_punctuations(withpunct):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~+'''
    without_punct = ""
    char = 'nan'
    for char in withpunct:
        if char not in punctuations:
            without_punct = without_punct + char
    return(without_punct)

def preprocess(text):
    import re
    from nltk.corpus import stopwords
    from nltk.stem import WordNetLemmatizer
#    from pattern.en import pluralize, singularize
    lemmatizer = WordNetLemmatizer()
    
    text = re.sub(r'\([^)]*\)', '', text)   # remove words inside parenthesis 
    text = remov_punctuations(text)
    text = re.sub(r'PHILS', 'PHILIPPINES', text)  
    text = re.sub(r'  ', ' ', text)    
    
    stop_words = set(stopwords.words('english'))
    stop_words |= {"INC","INCORPORATED","CO","COMPANY","CORP", "CORPORATION", "AND", "&", "ASSOC", "ASSN","ASSOCIATION", "DEVT",  "DEVELOPMENT","INDUS", "IND", "INDUSTRY","INDUSTRIAL"\
                  "COOP", "COOPERATIVE","TECH","TECHNOLOGY","TECHNOLOGIES","ON","IN","AT","THE","OF","BY","FOR", "IS",\
                   "SYS","SYSTEM","GRP","GROUP","MFG","MANUFACTURING","SHOP","ORG", "ORGANIZATION", "INTL","INTERNATIONAL", "ENTERPRISE","ENTERPRISES","LTD", "LIMITED","+", "'S"}

    tokens = nltk.word_tokenize(text)                   # Tokenization
 #   text = nltk.Text(tokens)
 #   tokens = [singularize(token) for token in tokens]    
 #   tokens = [token.upper() for token in tokens]    
    text = [lemmatizer.lemmatize(token) for token in tokens]
    filtered_words = [w for w in text if not w in stop_words] # remove stop words
    return(" ".join(filtered_words))

# get the difference between two strings
def Diff_1(list_1, list_2):
    list_1 = [str(x) for x in list_1]
    list_2 = [str(x) for x in list_2]
    print("Difference: ", len(list(set(list_1)-set(list_2))))
    diff1 = list(sorted(set(list_1)-set(list_2)))
    return diff1, print(diff1)

# Main
in_file =  open_file_tk()
file = open_file(in_file)
df = get_sheets(file)
mylist = list(df.iloc[:,1])

# process and clean list one by one
proc_list = []
for item in mylist :
    procd_comp = preprocess(str(item))
    proc_list.append(procd_comp)    

# check for duplicates within a list
from collections import Counter
Counter(proc_list)
dupes = [key for key in Counter(proc_list).keys() if Counter(proc_list)[key] > 1]

# check difference between lists
difference = Diff_1(all_list,contacted_list)
