#!/usr/bin/python

import os

for file in os.listdir('../') :
	if file.endswith('Aligned.out.bam') :
		os.system('featureCounts -T 32  -p -B -C -F SAF -a %s.genes.saf -o %s.fc ../%s' %(file[:4],file[:9],file))