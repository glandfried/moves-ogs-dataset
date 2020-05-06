import csv
import os
import json
import pickle
import numpy as np

files_dir = 'files_GO_glicko/'
listdir_ = os.listdir(files_dir ) # Crea una lista de todos los archivos dentro de esa carpeta

""" 
There are private game before oct 2013 (id game less than 414291)?:
    Conclution: 
        there is no private after analyse 254770 games
 
Note: there is a file name "export.csv", when expected number.sgf 

ToDo: Description (frecuency) of corrupted files.
"""

games = []
count = 0
files_names_corrupted = []
for f in range(len(listdir_)):#f = 8993
    try:
        n = int(listdir_[f].split(".")[0])
        count = count + 1
        file_path = os.path.join(files_dir, listdir_[f]) # Genera el path completo de un archivo
        with open(file_path, 'r') as file:
            data = file.read()
        
        ###########################
        # ToDo
        # Add here the analysis of corrupted files
        ################
        
        # Before Oct 2013
        if n <= 414291 and 'Permission denied' in data:
            games.append(n)
        
    except:
        files_names_corrupted.append(f)
