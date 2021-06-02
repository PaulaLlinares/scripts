#!/home/paula/anaconda3/envs/my-rdkit-env/bin/python3.7
# ----------------------------------------------------------
# Outputs the actives distribution for each ranking
# Accepted input type: csv
#
# Example: actives_distribution.py -i1 ranking1 -i2 ranking2 -i3 ranking3 -i4 ranking4 -i5 ranking5
# ----------------------------------------------------------

import os
import numpy as np
import argparse
import pandas as pd
import csv

parser = argparse.ArgumentParser(description="Outputs name of active and their position")
parser.add_argument('-i1', required=True, help='ranking file')
#parser.add_argument('-i2', required=True, help='ranking file')
#parser.add_argument('-i3', required=True, help='ranking file')
#parser.add_argument('-i4', required=True, help='ranking file')
#parser.add_argument('-i5', required=True, help='ranking file')

args = parser.parse_args()

#filenames= [args.i1, args.i2, args.i3, args.i4, args.i5]
filenames=[args.i1]
dictionary = {} #se crea un diccionario
file_number = 0

for filename in filenames:
    #print (filename)
    count = 0
    with open(filename, 'r') as input_handle:
        for line in input_handle:
            count += 1
            if count > 3: #lectura a partir de la 4a línea
                name = line.split(';')[9] #se recoge los datos de Molecule Name
                if name.startswith("CHEMBL"):
                    position = int(line.split(';')[0]) #se recogen los datos de la posición
                    print(name, position)
                    #dictionary[name][file_number] = [position]
 #                   dictionary[name] = position
                #print ("name: " + name + " position: " + str(position) + " tanimoto: " + str(tanimoto))
    file_number+=1
