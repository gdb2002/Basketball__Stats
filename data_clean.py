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

def combine(path: str, new_path:str, skip = 2, empty_line = False):
    """
    Combines a folder into a csv file
    Path -> a folder
    new_path -> FILE
    """
    new_file = open(new_path, 'w')
    counter = 0
    folder = os.scandir(path)
    
    for file in folder:
        f = open(path+'/'+file.name, "r") #modifed
        f.readline()
        if counter != 0:
            f.readlines(skip)
        
        if not empty_line:
            new_file.write(f.read())
        else:
            hold =f.read() + '\n'
            new_file.write(hold)
        f.close()
        counter += 1
        
    new_file.close()
    
        
        
if __name__ == "__main__":
    
    path_player = "./Stats/Combined_Stats"
    path_game = "./Stats/Game_stats"
    folder_player = os.scandir("./Stats/Combined_Stats")
    folder_game = os.scandir("./Stats/Game_stats")
    
    combine(path_player, "./player_combined.csv")
    combine(path_game, "./game_combined.csv", empty_line=True)
        

        