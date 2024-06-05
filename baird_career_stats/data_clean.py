import pandas as pd
import os
import numpy as np
from datetime import date
"""
A collection of functions that make data cleaning 
easier and more reapeatable for future projects
"""

def get_percent(lst: np.array, divider = '-'):
    """Meant to seperate a column that has a divider"""
    lst = [char.split(sep = divider) for char in lst]
    percent_arr = []
    for  made, attempted in lst:
        if(int(made) == 0 and int(attempted) == 0):
            percent_arr.append(0)
        else:
            percent_arr.append(int(made)/int(attempted))
            
    return  list(map(lambda x: x*100, percent_arr))

def label(table: pd.DataFrame, x_row, y_row, label, amount = 1, rotate = 90, font_size = 12):

    for i, _ in enumerate(x_row):
        table.text(x_row[i], y_row[i] + amount, label[i], rotation = rotate, size = font_size)
    
    return

def str_to_date(string:list):
    """takes a list of strings in the month/day/year format and converts it to date"""
    new_list = []
    
    for day in string:
        bank = day.split(sep = '/')
        bank = [int(i)for i in bank]
        bank[2]= bank[2] + 2000
        new_day = date(bank[2],bank[0],bank[1])
        new_list.append(new_day)
        
    return new_list
    
def add_value(file: str, value: str, title: str, sep: str = '-', copy = False, New_file = ""):
    """
    Assumes A title on csv and adds a value to a file

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
    
def seperate(table, col: str, data_type, divider = '-', name1 = "New_col1", name2 = "New_col2", delete_original = False ):
    """takes a table and an col name then splits them and adds them back to the orginal table

    Args:
        table (_type_): _description_
        col (str): _description_
        divider (str, optional): _description_. Defaults to '-'.
        name1 (str, optional): _description_. Defaults to "New_col1".
        name2 (str, optional): _description_. Defaults to "New_col2".
    """
    column = table[col].to_numpy()
    data1 = []
    data2 = []
    
    for item in column:
        item1, item2 = item.split(sep = divider)
        data1.append(data_type(item1))
        data2.append(data_type(item2))
    
    table[name1] = data1
    table[name2] = data2
    
    if delete_original:
        table.drop(columns =[col])
    
    return 

def percent(table, col1:str, col2: str, new_col_name):
    """can do the percent of col1 and col2 and 
    add a new col to the table based off of this"""
    
    new_col = (table[col1] / table[col2]) * 100
    table[new_col_name] = new_col 
        
if __name__ == "__main__":
    x = date(2000, 1, 20)
    print(len(x.month))
    # path_player = "./Stats/Combined_Stats"
    # path_game = "./Stats/Game_stats"
    # folder_player = os.scandir("./Stats/Combined_Stats")
    # folder_game = os.scandir("./Stats/Game_stats")
    
    # combine(path_player, "./player_combined.csv")
    # combine(path_game, "./game_combined.csv", empty_line=True)
        

        