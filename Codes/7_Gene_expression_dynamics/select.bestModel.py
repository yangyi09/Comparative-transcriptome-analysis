#!/usr/bin/python

import pandas as pd
from collections import Counter

data = pd.read_excel('Fit.result.xlsx',header=0)


def best(a) :
	minAICc = min(a[1:].tolist())
	i = a[1:].tolist().index(minAICc)
	if i == 0 :
		return ('BM')
	elif i == 1 :
		return ('OU')
	else :
		return ('OUM')

data['Best'] = data.apply(lambda x : best(x),axis = 1)
data.to_excel('Fit.OUwie.result.best.xlsx',index=False)
print (Counter(data['Best'].tolist()))