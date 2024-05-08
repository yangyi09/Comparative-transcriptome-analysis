#!/usr/bin/python

import os

species = []
for file in os.listdir('./featureCounts') :
	species.append(file.split('.')[0])
species = list(set(species))

for s in species :
	os.system('mkdir ./featureCounts/%s' %s)
	os.system('STAR --runMode genomeGenerate --runThreadN 112 --genomeDir ./featureCounts/%s --genomeFastaFiles ./featureCounts/%s.genome.fa --sjdbGTFfile ./featureCounts/%s.gtf' %(s,s,s))