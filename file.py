#-*-coding:utf-8-*-
'''This .py file is to combine files'''
'''Vinson 17 Aug 2018'''

import os

# root dictionary of files
root_dir = r"/home/vchim/PycharmProjects/suoju/primaryschool_textbook/primaryschool_textbook"
root_dir_1 = r"/home/vchim/PycharmProjects/suoju/primaryschool_writings"

# Read files, and write files
with open("primaryschool_textbook_total.txt", "w") as text_total:

    # Read each files in root dictionary one by one
    for file in os.listdir(root_dir):
        file_name = root_dir + "/" + file
        filein = open(file_name, "r")
        # Read file's content by lines
        for line in filein:
            text_total.write(line.rstrip("\n"))
            text_total.write("\n")
        filein.close()

with open("primaryschool_writings_total.text", "w") as writing_total:

    for file in os.listdir(root_dir_1):
        file_name = root_dir_1 + "/" + file
        filein = open(file_name, "r")
        for line in filein:
            writing_total.write(line.rstrip("\n"))
            writing_total.write("\n")
        filein.close()