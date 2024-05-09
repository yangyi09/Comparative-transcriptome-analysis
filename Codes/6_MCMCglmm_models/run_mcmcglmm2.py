#!/usr/bin/python


import os
import threading
from collections import defaultdict
import pickle
import numpy as np
import pandas as pd

def run_mcmcglmm(ogs) :
	for og in ogs :
		os.system('Rscript ./%s/mcmcglmm.R  ./%s/data.csv ./%s/Species.r8s.tre ./%s/model.rda ./%s/d.csv ./%s/r.csv  '  %(og,og,og,og,og,og))


def generate_data(og,data) :
	a = data[[og,'Host']]
	a['Species'] = a.index
	a.columns = ['Exp','Host','Species']
	a = a[['Species','Exp','Host']]
	a.to_csv('data.csv',index=False)
def tpm10k(a,n) :
	return ([(i*n)/10000 for i in a])
def host(a,b) :
	if a in b :
		return ('Y')
	else :
		return ('N')



def main() :
	og2peps = defaultdict(list)
	for line in open('Orthogroups.txt','r') :
		line = line.strip()
		a = line.split(': ')
		og2peps[a[0]] = a[1].lstrip().rstrip().split()

	with open('pep2gene.pkl','rb') as f2 :
		pep2gene = pickle.load(f2)

	with open('gene2tpms.pkl','rb') as f3 :
		gene2tpms = pickle.load(f3)

	with open('speciesn.pkl','rb') as f4 :
		adict = pickle.load(f4)

	sharedOGs = []
	for key,value in og2peps.items():
		value = list(set([i[:4] for i in value]))
		if len(value) == 19 :
			sharedOGs.append(key)

	for og in sharedOGs :
		o = []
		os.system('mkdir %s' %og)
		os.chdir('./%s' %og)
		for pep in og2peps.get(og) :
			gene = pep2gene.get(pep)
			tpms = gene2tpms.get(gene)
			tpm10kmedian = np.median(tpm10k(tpms,adict[gene[:4]]))
			#log2 = np.log2(tpm10kmedian+1)
			hosttype = host(gene[:4],['Asoj','Lhet','Lbou','Tdro','Pvin'])
			o.append([gene[:4],gene,tpm10kmedian,hosttype])
		df = pd.DataFrame(o,columns=['Species','Gene','Exp','Host'])
		df.to_csv('data.csv',index=False)
		os.system('cp ../mcmcglmm.R ./')
		os.system('cp ../Species.r8s.tre ./')
		os.chdir('../')

	threads =[]
	threads_num=112
	per_thread=len(sharedOGs)//threads_num
	for i in range(threads_num):
		if threads_num-i==1:
			ogs = sharedOGs[i*per_thread:]
			t=threading.Thread(target=run_mcmcglmm,args=(ogs,))
		else:
			ogs = sharedOGs[i*per_thread:i*per_thread+per_thread]
			t=threading.Thread(target=run_mcmcglmm,args=(ogs,))
		threads.append(t)
	for thr in threads:
		thr.start()
	for thr in threads:
		thr.join()
if __name__ == '__main__':
	main()
