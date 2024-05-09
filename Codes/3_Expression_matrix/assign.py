#!/usr/bin/python

import pickle
import pandas as pd

with open('sc1479topep.pkl','rb') as f :
	sc2pep = pickle.load(f)

with open('go2peps.pkl','rb') as f1 :
	go2peps = pickle.load(f1)

with open('og2peps.pkl','rb') as f2 :
	og2peps = pickle.load(f2)

data1  = pd.read_csv('1479.sc.TPM10K.csv')
data2  = pd.read_csv('OGLevel.expression.matrix.TPM10K.csv')
data3  = pd.read_csv('GOLevel.expression.matrix.TPM10K.csv')


'''
VGpeps = []
for line in open('19VG.list','r') :
	line = line.strip()
	VGpeps.append(line)


associateOGs1 = []
for k,v in sc2pep.items() :
	if len(list(set(v).intersection(set(VGpeps)))) > 0 :
		associateOGs1.append(k)
df1 = data1[data1['OG'].isin(associateOGs1)]
df1.to_csv( str(len(df1)) + '.19VG.sc.TPM10K.csv',index=False)




associateOGs2 = []
for k,v in og2peps.items() :
	if len(list(set(v).intersection(set(VGpeps)))) > 0 :
		associateOGs2.append(k)
df2 = data2[data2['OG'].isin(associateOGs2)]
df2.to_csv( str(len(df2)) + '.19VG.OG.TPM10K.csv',index=False)


associateGOs3 = []
for k,v in go2peps.items() :
	if len(list(set(v).intersection(set(VGpeps)))) > 0 :
		associateGOs3.append(k)
df3 = data3[data3['GO'].isin(associateGOs3)]
df3.to_csv( str(len(df3)) + '.19VG.GO.TPM10K.csv',index=False)
'''

#Five Drosophila
VGpeps = []
for line in open('19.HE.list','r') :
#for line in open('19VG.list','r') :
	line = line.strip()
	if line[:4] in ['Lbou','Lhet','Asoj','Tdro','Pvin'] :
		VGpeps.append(line)


associateOGs1 = []
for k,v in sc2pep.items() :
	if len(list(set(v).intersection(set(VGpeps)))) > 0 :
		associateOGs1.append(k)
df1 = data1[data1['OG'].isin(associateOGs1)]
df1.to_csv( str(len(df1)) + '.5DrosHE.sc.TPM10K.csv',index=False)


associateOGs2 = []
for k,v in og2peps.items() :
	if len(list(set(v).intersection(set(VGpeps)))) > 0 :
		associateOGs2.append(k)
df2 = data2[data2['OG'].isin(associateOGs2)]
df2.to_csv( str(len(df2)) + '.5DrosHE.OG.TPM10K.csv',index=False)


associateGOs3 = []
for k,v in go2peps.items() :
	if len(list(set(v).intersection(set(VGpeps)))) > 0 :
		associateGOs3.append(k)
df3 = data3[data3['GO'].isin(associateGOs3)]
df3.to_csv( str(len(df3)) + '.5DrosHE.GO.TPM10K.csv',index=False)