#!/usr/bin/python

import os
from collections import defaultdict


outdict = defaultdict(list)
for file in os.listdir('./og111') :
	if file.endswith('.fa') :
		og = file.split('.')[0]
		os.system('mafft --thread 56 --anysymbol --maxiterate 1000 --localpair ./og111/%s >./og111/%s.mafft' %(og + '.fa',og))
		os.system('trimal -in ./og111/%s -out ./og111/%s.trimal -automated1' %(og + '.mafft',og))
	for line in open('./og111/%s.trimal' %og,'r') :
		line = line.strip()
		if line.startswith('>') :
			id = line[1:]
		else :
			outdict[id].append(line.replace('\n',''))

out = open('all_concated.fasta','a+')
for key in list(outdict.keys()) :
	out.write('>' + key)
	out.write('\n')
	out.write(''.join(outdict[key]))
	out.write('\n')
out.close()