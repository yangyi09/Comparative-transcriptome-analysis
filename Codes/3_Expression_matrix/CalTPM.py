#!/usr/bin/python

import numpy as np
import pandas as pd
import os

def cal(df) :
	df.rename(columns={df.columns.tolist()[-1]:'Counts'},inplace=True)
	df.drop(['Chr','Start','End','Strand'],axis=1,inplace=True)
	df_kb=df['Length']*0.001
	df['length_kb']=df_kb
	rpk= df['Counts']/df['length_kb']
	df['rpk_values']=rpk
	total_rpk=df['rpk_values'].sum()
	per_million_scalling_factor=total_rpk/1000000
	tpm=df['rpk_values']/per_million_scalling_factor
	df['tpm']=tpm
	return (df)

#data = pd.read_csv('Acal.vg1.fc',sep="\t",header=1)
for file in os.listdir('./') :
	if file.endswith('.fc') :
		data =  pd.read_csv(file,sep="\t",header=1)
		df_tpm = cal(data)
		df_tpm.to_csv(file+'.tpm.tsv',sep='\t',index=False)