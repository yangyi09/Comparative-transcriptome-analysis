#!/usr/bin/python

import os
import pandas as pd

data = pd.read_csv($exp.matrix,header=0)

def tree(a) :
	og = a['OG']
	df = a.to_frame()
	df = pd.DataFrame(df.values.T,columns=df.index)
	df.to_csv('tmp.csv',index=False)
	os.system('Rscript phylip.dis.R')
	os.system('fastme -i tmp.dis.phylip -m N  -o %s.tre' %og)
	os.system('rm tmp.csv')
	os.system('rm tmp.dis.phylip')
	os.system('rm tmp.dis.phylip_fastme_stat.txt')

data.apply(lambda x : tree(x), axis = 1)