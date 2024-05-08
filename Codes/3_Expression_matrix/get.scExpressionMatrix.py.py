#!/usr/bin/python

import os
from collections import defaultdict
from Bio import SeqIO
import pickle

ogs = []
og2genes = {}
for file in os.listdir('111og') :
	if file.endswith('.fa') :
		ogs.append(file[:-3])
		seqindex = SeqIO.index('./111og/' + file ,'fasta')
		og2genes[file[:-3]] = list(seqindex.keys())

with open('gene2exp.pkl','rb') as f :
	gene2exp = pickle.load(f)


result = defaultdict(dict)
for og in ogs :
	genes = og2genes[og]
	for gene in genes :
		t = gene2exp[gene]
		for k,v in t.items():
			result[og][k] = v
import pandas as pd
df = pd.DataFrame(result)
df = df.T

df = df.sort_index(axis=1)
df.to_csv('1479sc.expression.matrix.csv')