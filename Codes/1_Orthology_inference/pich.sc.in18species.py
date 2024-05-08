#!/usr/bin/python

import pandas as pd

data = pd.read_csv('Orthogroups.GeneCount.tsv',sep='\t',index_col=0)

data.drop(['Total'],axis=1,inplace=True)

for s in data.columns.tolist():
	if not s == 'Tdro' :
		data = data[data[s]==1]
data = data[data['Tdro']>0]
data.to_csv('sc.in18Species.csv')