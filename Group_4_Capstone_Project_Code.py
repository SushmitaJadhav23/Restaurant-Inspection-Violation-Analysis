"""
Group_4 Capstone Project
Copyright (c) 2019
Licensed Northeatern unniversity
"""
import numpy as np
# Create a function to make column values(string) to consistent
def flag_brands(col_name, file_name, dest_col, Dict):
    """

    :param col_name: Column Name to perform changes
    :param file_name: Data frame Name
    :param dest_col: Column where changes to apply
    :param Dict: contains values searching values and replacing values
    :return:
    """
    for k, v in Dict.items():
        file_name[dest_col] = np.where(col_name.str.contains(k), v, file_name[dest_col])
    return

# Create function to replce values in column by using dictionary values
def Change_values(col_name,Dict):
    """

    :param col_name: Column Name to perform changes
    :param Dict:contains values searching values and replacing values
    :return: Returns column with replacing values
    """
    return col_name.replace(Dict, inplace=True)