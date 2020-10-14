# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 14:04:53 2020

@author: HeJiXiao
"""
import os
from os.path import splitext,join

#作業解壓縮後的資料夾
UNZIPED_DIR = r' '

def getSourceFiles(path):
    sources = []
    
    for root, dirs, files, in os.walk(path):
        for file in files:
            name, extension = splitext(file)
            if extension == '.c' or extension == '.cpp':
                sources.append({'path':root, 'filename':file})
    
    return sources

def ensureGCC():
    if(os.system('gcc --version') == 1):
        print('Please install GCC or check be installed correctly.')
        exit(1)
    
def compileSourceFiles(files_tuple):
    ensureGCC()
    
    for entry in files_tuple:
        name, extension = splitext(entry['filename'])
        result = os.system('gcc -o "' + join(entry['path'], name) + '" "' + join(entry['path'], entry['filename']) + '"')
        if result != 0 :
            print(result)
        else:
            print(join(entry['path'], entry['filename']) + " has been compiled")
        
    print('done')
    
if __name__ == '__main__' :
    files = getSourceFiles(UNZIPED_DIR)
    compileSourceFiles(files)