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
    for table in root.xpath("//table[@class='roundy eplist s-关都']"):
        # Initialize
        temp_str = ""
        for row in table.xpath("//tbody/tr/td"):
            if not row.text:
                for item in row.xpath("/a"):
                    temp_str = "{0} {1}".format(temp_str, item.text)
            else:
                temp_str = "{0} {1}".format(temp_str, row.text)
        # Print the answer
        print(temp_str)
    # We need the infomations
    # National Pokedex, Pokemon name, 1st Type, 2nd Type(if exists)
    #-----------------------------------
    # Measure time
    elapsed_time = time.time() - start_time
    print("Exiting Main Program, spending ", elapsed_time, "seconds.")
