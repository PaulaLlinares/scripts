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
parser.add_argument('-i2', required=True, help='ranking file')
parser.add_argument('-i3', required=True, help='ranking file')
parser.add_argument('-i4', required=True, help='ranking file')
parser.add_argument('-i5', required=True, help='ranking file')

args = parser.parse_args()

filenames= [args.i1, args.i2, args.i3, args.i4, args.i5]
dictionary = {} #se crea un diccionario

for filename in filenames:
    #print (filename)
    count = 0
    with open(filename, 'r') as input_handle:
        for line in input_handle:
            count += 1
            if count > 3: #lectura a partir de la 4a línea
                name = line.split(';')[9] #se recoge los datos de Molecule Name
                position = int(line.split(';')[0]) - 1 #se recogen los datos de la posición -1 para Pareto
                tanimoto = float(line.split(';')[5]) #se recogen los datos de coeficiente de Tanimoto
                #print(tanimoto))
                if not name in dictionary:
                #abre el primer archivo y anota la posición y tanimoto en lista
                    dictionary[name] = [position,tanimoto,name]
                    #print(tanimoto)
                #si el nombre ya existe suma la nueva posición a la anterior
                else:
                    dictionary[name][0] += position
                    if tanimoto>dictionary[name][1]:
                        dictionary[name][1]=tanimoto
                #print ("name: " + name + " position: " + str(position) + " tanimoto: " + str(tanimoto))


#crea matriz con los datos
df = pd.DataFrame(dictionary.values(), columns = ['Pareto score','Similarity Score','Molecule Name'])
df[['A','B','C','D','E','F','G']]=pd.DataFrame([['Similarity Score','Pareto', 'script','for','rank','scoring','#####']], index=df.index)
df = df[['Pareto score','Similarity Score','B','C','D','E','F','G','Molecule Name']]
df=df.sort_values(by=['Pareto score', 'Similarity Score'], ascending=[True, False]) 
# Pareto score asc, Similarity Score desc
df.index=np.arange(1,len(df)+1)
df.drop('Pareto score', axis=1)
#df.reset_index(inplace = True, drop = True)
df.to_csv('ranking_pareto.csv', sep=';')

output=open('ranking_pareto.csv', 'w')
output.write('\n'*2) #deja 2 líneas en blanco al inicio
df.to_csv(output, sep=';')
output.close()
