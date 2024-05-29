import pandas as pd
import os
"""
A collection of small scripts that help with organizing and structuring the data sets
"""

#TODO add the season into the full stat cs

def add_value(file: str, value: str, title: str, sep: str = '-', copy = False, New_file = ""):
    """
    Assumes A title on csv

    Args:
        file (str): _description_
        value (str): _description_
        title (str): _description_
        sep (str, optional): _description_. Defaults to '-'.
        copy (bool, optional): _description_. Defaults to False.
        New_file (str, optional): _description_. Defaults to "".
    """
    f = open(file, 'r')
    hold = f.readline()
    counter = 0
    for line in f:
        if counter == 0:
            hold += line[:-1]+ sep + title + '\n'
        else:
            hold += line[:-1] + sep + value + '\n'
        counter += 1
    f.close()
    if copy:
        file = New_file
    f = open(file, 'w')
    f.write(hold)
    f.close
    return 

def combine(path: str, new_path):
    """
    Combines a folder into a csv file
    """
    new_file = open(new_path, 'w')
    counter = 0
    folder = os.scandir(path)
    
    for file in folder:
        f = open(path+file.name, "r")
        f.readline()
        if counter != 0:
            f.readlines(2)
            
        new_file.write(f.read())
        f.close()
        counter += 1
        
    new_file.close()
    
        
        
if __name__ == "__main__":
    
    path = "./Stats/Player_stats"
    folder = os.scandir(path)
    
    for file in folder:
        value = file.name[:-4]
        #add_value(path+ '/'+file.name, value, "Year", sep = '\t', copy = True, New_file="./Stats/Combined_Stats/"+file.name) # gives me the new copies
        