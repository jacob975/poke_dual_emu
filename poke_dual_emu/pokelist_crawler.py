#!/usr/bin/python3
'''
Abstract:
    This is a function to obtain a list of pokemon. 
Usage:
    pokelist_crawler.py
Output:
    The image of dustmap on a given location.
Editor:
    Jacob975
##################################
#   Python3                      #
#   This code is made in python3 #
##################################
20200806
####################################
update log
20200806 version alpha 1:
    1. The code works.
'''
import time
import numpy as np
import requests
from lxml import html

def obtain_poke(root, table_class_name):
    # Initialization
    xpath_str = "//table[@class='{0}']".format(table_class_name)
    poke_list = []
    #-----------------------------------------------------------
    # We need the infomations
    # National Pokedex, Pokemon name, 1st Type, 2nd Type(if exists)
    for table in root.xpath(xpath_str):
        for row in table.xpath('./tbody/tr'):
            # String for a pokemon
            temp_str = ""
            result = ""
            for item in row.xpath('./td/a'):
                result = item.text
                temp_str = "{0} {1}".format(temp_str, result)
            for item in row.xpath('./td'):
                if item.text is None:
                    continue
                elif item.get('class') == "textwhite bg- hide":
                    continue
                else:
                    result = item.text
                temp_str = "{0} {1}".format(temp_str, result[:-1])
            print(temp_str)
            poke_list.append(temp_str)
    return poke_list

#--------------------------------------------
# Main code
if __name__ == "__main__":
    # Measure time
    start_time = time.time()
    #-----------------------------------
    # Open the list of pokemon: https://wiki.52poke.com/zh-hant/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89
    pokelist_wiki52page = 'https://wiki.52poke.com/zh-hant/%E5%AE%9D%E5%8F%AF%E6%A2%A6%E5%88%97%E8%A1%A8%EF%BC%88%E6%8C%89%E5%85%A8%E5%9B%BD%E5%9B%BE%E9%89%B4%E7%BC%96%E5%8F%B7%EF%BC%89'
    page = requests.get(pokelist_wiki52page)
    root = html.fromstring(page.content.decode('UTF-8'))
    # List the table class name
    table_class_name_list = []
    for table in root.xpath("//table"):
        table_class_name = table.get('class')
        table_class_name_list.append(table_class_name)
    print(table_class_name_list)
    # List the pokemon info in a line for each.
    for tbname in table_class_name_list:
        obtain_poke(root, tbname)
    #-----------------------------------
    # Measure time
    elapsed_time = time.time() - start_time
    print("Exiting Main Program, spending ", elapsed_time, "seconds.")
