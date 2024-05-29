import pandas as pd
import os
"""
A collection of small scripts that help with organizing and structuring the data sets
"""

def combine(path: str):
    """
    Combines a folder into a csv file
    """
    new_file = open("../Stats/Full_stats.csv", 'w')
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
    
    #combine("../Stats/")    #use if more data is added
        
    pass
    