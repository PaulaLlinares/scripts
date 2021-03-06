#!/home/paula/anaconda3/envs/my-rdkit-env/bin/python3.7
# ----------------------------------------------------------
# AUC summary generation
# ----------------------------------------------------------
# ----------------------------------------------------------
import sys
import os
import argparse

#----------------------------------- Main function --------------------------------------
sys.path.insert(0, './support')
parser = argparse.ArgumentParser(description='Molecular 3D structure generator from 2D')
parser.add_argument('-i', required=True, help='ranking file')
parser.add_argument('-i1', required=True, help='ranking file')
parser.add_argument('-i2', required=True, help='ranking file')
parser.add_argument('-i3', required=True, help='ranking file')
parser.add_argument('-i4', required=True, help='ranking file')
parser.add_argument('-i5', required=True, help='ranking file')
parser.add_argument('-i6', required=True, help='ranking file')
parser.add_argument('-i7', required=True, help='ranking file')
parser.add_argument('-o', required=True, help='output name')
parser.add_argument('-set', required=True, help='set name')
parser.add_argument('-n', required=True, help='roc num')
parser.add_argument('-p', required=True, help='roc num')

args = parser.parse_args()
lg = RDLogger.logger()
lg.setLevel(RDLogger.CRITICAL)

inp = args.i
inp1 = args.i1
inp2 = args.i2
inp3 = args.i3
inp4 = args.i4
inp5 = args.i5
inp6 = args.i6
inp7 = args.i7
out = args.o 

input_file=open(inp,"r")
input_file1=open(inp1,"r")
input_file2=open(inp2,"r")
input_file3=open(inp3,"r")
input_file4=open(inp4,"r")
input_file5=open(inp5,"r")
input_file6=open(inp6,"r")
input_file7=open(inp7,"r")
o=open(out,"w")
ref_cons="a"
ref1="b"
ref2="c"
ref3="d"
ref4="e"
ref5="f"
ref_pareto="g"
ref_parallel="h"

count=0
for line in input_file:
    count+=1
    if count==12:
        ref_cons = line.split()[0]
        
count=0
for line in input_file1:
    count+=1
    if count==12:
        ref1 = line.split()[0]

count=0
for line in input_file2:
    count+=1
    if count==12:
        ref2 = line.split()[0]

count=0
for line in input_file3:
    count+=1
    if count==12:
        ref3 = line.split()[0]

count=0
for line in input_file4:
    count+=1
    if count==12:
        ref4=line.split()[0]
count=0
for line in input_file5:
    count+=1
    if count==12:
        ref5=line.split()[0]

count=0
for line in input_file6:
    count+=1
    if count==12:
        ref_pareto=line.split()[0]
count=0
for line in input_file7:
    count+=1
    if count==12:
        ref_parallel=line.split()[0]

auc=str(args.set) + "," +str(ref1) + "," +  str(ref2) + "," + str(ref3) + "," + str(ref4) + "," + str(ref5) + "," + str(ref_cons)+ "," + str(ref_pareto) +","+ str(ref_parallel) +"\n"

if args.set == "aa2ar": 
    o.write("\n")
    o.write(str(args.n)+"\n")
    o.write("set_name" +","+ "Ref1" +","+ "Ref2" +","+ "Ref3" +","+ "Ref4" +","+ "Ref5" +","+ "max" + "," + "pareto" + "," + "parallel" +"\n")
o.write(auc)
o.close()
