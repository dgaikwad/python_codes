#!/usr/bin/python3

import os

def printFiles1(main_dir):
    """Code without using os.walk"""
    for file in os.listdir(main_dir):
        file_path = main_dir + "/" + file
        if os.path.isdir(file_path):
            print("DirName: " + file_path)
            printFiles1(file_path)
        elif os.path.isfile(file_path):
            print("FileName: " + file_path)

def printFiles2(main_dir):
    """Code with using os.walk"""
    # traverse root directory, and list directories as dirs and files as files
    for root, dirs, files in os.walk(main_dir):
        print("DirName: " + root)
        for file in files:
            print("FileName: " + root + os.sep +  file)

if __name__ == "__main__":
    parent_dir = os.getcwd()
    printFiles1(parent_dir)
    print("#"*50)
    printFiles2(parent_dir)
