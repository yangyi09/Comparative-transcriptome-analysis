#!/usr/bin/python

import pickle
from collections import defaultdict,Counter
import os
import pandas as pd
import numpy as np

with open('go2peps.pkl','rb') as f :
	go2peps = pickle.load(f)
with open('pep2gene.pkl','rb') as f1 :
	pep2gene = pickle.load(f1)
with open('gene2exp.pkl','rb') as f2 :
	gene2exp = pickle.load(f2)

sharedGOs = []
for key,value in go2peps.items():
	value = list(set([i[:4] for i in value]))
	if len(value) == 19 :
		sharedGOs.append(key)

df =pd.DataFrame()
for go in sharedGOs :
	print (go)
	cdict = {}
	peps = go2peps[go]
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
	dft = pd.DataFrame(cdict,index=[go])
	df = pd.concat([df, dft])
df.to_csv('GOLevel.expression.matrix.csv',index=True)
print (df)
