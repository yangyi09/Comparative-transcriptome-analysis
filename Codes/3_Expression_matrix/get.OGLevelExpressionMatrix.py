#!/usr/bin/python

import pickle
from collections import defaultdict,Counter
import os
import pandas as pd
import numpy as np


with open('pep2gene.pkl','rb') as f1 :
	pep2gene = pickle.load(f1)
with open('gene2exp.pkl','rb') as f2 :
	gene2exp = pickle.load(f2)

og2peps = defaultdict(list)
for line in open('Orthogroups.txt','r') :
	line = line.strip()
	a = line.split(': ')
	og2peps[a[0]] = a[1].lstrip().rstrip().split()


sharedOGs = []
for key,value in og2peps.items():
	value = list(set([i[:4] for i in value]))
	if len(value) == 19 :
		sharedOGs.append(key)

df =pd.DataFrame()
for og in sharedOGs :
	print (og)
	cdict = {}
	peps = og2peps[og]
	adict = Counter([i[:4] for i in peps])
	for s in list(adict.keys()):
		a = []
		for pep in peps :
			if pep[:4] == s :
				gene = pep2gene[pep]
				a.append(gene2exp[gene])
		b = np.sum(np.array(a),axis=0)
		for i in range(len(b)) :
			cdict[s+ '.vg' + str(i)] = b[i]
	dft = pd.DataFrame(cdict,index=[og])
	df = pd.concat([df, dft])
df.to_csv('OGLevel.expression.matrix.csv',index=True)
print (df)