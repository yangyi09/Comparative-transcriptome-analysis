##Pipeline for reconstructing the species phylogenetic tree

#Step1, generate a supergene sequence from 1,792 single-copy orthologues.
python concat.py

#Step 2, run IQ-TREE v2.0 for maximum likelihood phylogenetic tree construction.
iqtree2 -s ./all_concated.fasta -m MFP -B 1000

#Step 3, run r8s to estimate the divergent times between the species
r8s -b -f r8s_input.txt >r8s.out