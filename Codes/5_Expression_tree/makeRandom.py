#!/usr/bin/python
import os

for i in range(10000) :
	os.system('Rscript random.r')
	os.system('mv tmp.tre random.%s.tre' %str(i))