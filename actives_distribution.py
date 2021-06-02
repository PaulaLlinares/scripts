#!/home/paula/anaconda3/envs/my-rdkit-env/bin/python3.7
# ----------------------------------------------------------
# Ranking position calculation using Pareto fusion rule
# Accepted input type: csv
#
# Example: pareto_fusion.py -i1 ranking1 -i2 ranking2 -i3 ranking3 -i4 ranking4 -i5 ranking5
# ----------------------------------------------------------

import os
import numpy as np
import argparse
import pandas as pd
import csv

parser = argparse.ArgumentParser(description="Ranking position calculation using Pareto fusion rule")
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

'''
key = Molecule_Name
Value = list(5)
dict[CHEMBL1095096-act] = {pos en fitxer ranking1, pos en fitxer ranking2, pos en fitxer ranking3, pos en fitxer ranking4, pos en fitxer ranking5}

file_number = 0;
llegir fitxers
llegir fitxer 1
dict[Molecule_Name][file_number] = pos
++file_number
'''

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

#crea matriz con los datos
#df = pd.DataFrame(dictionary.values(), columns = ['Ref1','Ref2', 'Ref3', 'Ref4', 'Ref5', 'Molecule Name'])
#df = df[['Molecule Name', 'Ref1','Ref2', 'Ref3', 'Ref4', 'Ref5']]
#df.index=np.arange(1,len(df)+1)
#df.drop('Molecule Name', axis=1)
#df.to_csv('ranking_actives.csv', sep=';')
