#!/usr/bin/python

import pandas as pd
import numpy as np
from Bio import SeqIO
from sklearn.preprocessing import OneHotEncoder

seqindex = SeqIO.index('concat.fa','fasta')
adict = {}
for k,v in seqindex.items() :
	adict[k] = list(str(v.seq))
data = pd.DataFrame(adict)

'''
for index,row in data.iterrows():
	if 'X' in row.tolist():
		data.drop(index = index,inplace=True)
'''



def one_hot(my_array) :
	encoder = OneHotEncoder(handle_unknown='ignore',sparse_output=False,categories=[['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L','M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']])
	ans = encoder.fit_transform(my_array.reshape(len(my_array),1))
	return (ans)


df = pd.DataFrame()

for  c in data.columns.tolist():
	df[c] = one_hot(np.array(data[c].tolist())).ravel()

df.to_csv('genome.oneHot.csv',index=False)

print (df)