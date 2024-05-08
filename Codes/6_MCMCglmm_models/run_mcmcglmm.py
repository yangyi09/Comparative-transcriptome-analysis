#!/usr/bin/python

import pandas as pd
import os
import threading
import numpy as np




def generate_data(og,data) :
	a = data[[og,'Host']]
	a['Species'] = a.index
	a.columns = ['Exp','Host','Species']
	a = a[['Species','Exp','Host']]
	#print (a)
	#a['Exp'] = a['Exp'].astype(float,copy=True).apply(lambda x : np.log2(x +1))
	a.to_csv('data.csv',index=False)



def run_mcmcglmm(ogs,data) :
	#print ('%dhanding\t%s\n'%(loops+1,list))
	for og in ogs :
#		os.system('mkdir %s' %og)
#		os.chdir('./%s' %og)
#		generate_data(og,data)
#		os.system('cp ../mcmcglmm.R ./')
#		os.system('cp ../Species.r8s.tre ./')
		os.system('Rscript ./%s/mcmcglmm.R  ./%s/data.csv ./%s/Species.r8s.tre ./%s/model.rda ./%s/d.csv ./%s/r.csv  '  %(og,og,og,og,og,og))
#		os.chdir('../')
#		print ('done %s' %og)


def main() :
	data = pd.read_csv(exp.data,header=0,index_col=0)
	data = data.T
	all_ogs = data.columns[1:].tolist()
	for og in all_ogs :
		os.system('mkdir %s' %og)
		os.chdir('./%s' %og)
		generate_data(og,data)
		os.system('cp ../mcmcglmm.R ./')
		os.system('cp ../Species.r8s.tre ./')
		os.chdir('../')
	threads =[]
	threads_num=112
	per_thread=len(all_ogs)//threads_num
	for i in range(threads_num):
		if threads_num-i==1:
			ogs = all_ogs[i*per_thread:]
			t=threading.Thread(target=run_mcmcglmm,args=(ogs,data))
		else:
			ogs = all_ogs[i*per_thread:i*per_thread+per_thread]
			t=threading.Thread(target=run_mcmcglmm,args=(ogs,data))
		threads.append(t)
	for thr in threads:
		thr.start()
	for thr in threads:
		thr.join()
if __name__ == '__main__':
	main()
