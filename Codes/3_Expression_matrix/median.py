#!/usr/bin/python

import pandas as pd
import numpy as np
import math
from collections import defaultdict
import statistics

for s in ['Asoj','Lbou','Lhet','Pvin','Tdro','Pven','Acal','Aful','Ajap','Pqin','Tele','Gfla','Vvel','Ppup','Btre','Cchi','Csol','Hheb','Nvit'] :
	data = pd.read_excel('%s.TPM10K.xlsx' %s, header=0)
	adict = defaultdict(list)
	for i in df.columns :
		adict[i[:4]].append(i)
	dfm = pd.DataFrame()
	for key,value in adict.items() :
		dfm[key] = df[value].apply(lambda x :statistics.median(x),axis=1)
	dfm.to_csv('%s.TPM10K.median.csv' %s,index=False,sep=',')