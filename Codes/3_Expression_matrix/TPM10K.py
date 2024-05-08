#!/usr/bin/python

import pandas as pd
import numpy as np


for s in ['Asoj','Lbou','Lhet','Pvin','Tdro','Pven','Acal','Aful','Ajap','Pqin','Tele','Gfla','Vvel','Ppup','Btre','Cchi','Csol','Hheb','Nvit'] :
	data = pd.read_excel('%s.TPM.xlsx' %s, sheet_name='TPM',header=0)
	data1 = pd.read_excel('%s.TPM.xlsx' %s, sheet_name='n',header=0)
	df = pd.DataFrame()
	df['Gene'] = data['Gene']
	trans = data.columns.tolist()[1:]
	for t in trans :
		s = t[:4]
		n = data1[data1['S']==s]['N'].values[0]
		df[t] = data[t].map(lambda x : (x* n)/10000 )
	df.to_excel('%s.TPM10K.xlsx' %s, index=False)