#!/usr/bin/python

import os


run_list = []
tmp = {}

for file in os.listdir('../../01_data/transcrpitome/all_data/') :
	run_list.append(file[:8])
	tmp[file[:8]] = file
run_list = list(set(run_list))


for i in run_list :
	s = i[:4]
	#os.system('mkdir %s' %s)
	if tmp[i].endswith('.gz') :
		os.system('STAR --runThreadN 112 --runMode alignReads --readFilesCommand zcat  --quantMode TranscriptomeSAM GeneCounts --outSAMtype BAM Unsorted --outSAMunmapped None --genomeDir ../01_reference/featureCounts/%s --readFilesIn ../../01_data/transcrpitome/all_data/%s.R1.fq.gz ../../01_data/transcrpitome/all_data/%s.R2.fq.gz --outFileNamePrefix %s' %(s,i,i,i))
	elif tmp[i].endswith('.fq') :
		os.system('STAR --runThreadN 112 --runMode alignReads --quantMode TranscriptomeSAM GeneCounts --outSAMtype BAM Unsorted --outSAMunmapped None --genomeDir ../01_reference/featureCounts/%s --readFilesIn ../../01_data/transcrpitome/all_data/%s.R1.fq ../../01_data/transcrpitome/all_data/%s.R2.fq --outFileNamePrefix %s' %(s,i,i,i))