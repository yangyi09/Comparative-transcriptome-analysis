#!/usr/bin/python
import os

for file in os.listdir('/data/yangyi/project/17_dros_para/01_data/pep/OrthoFinder/Results_Aug25/Orthogroup_Sequences/') :
	if file.endswith('.fa') :
		os.system('orthosnap -f /data/yangyi/project/17_dros_para/01_data/pep/OrthoFinder/Results_Aug25/Orthogroup_Sequences/%s -t /data/yangyi/project/17_dros_para/01_data/pep/OrthoFinder/Results_Aug25/Gene_Trees_rename/%s -op ./' %(file,file.split('.')[0] + '_tree.txt'))