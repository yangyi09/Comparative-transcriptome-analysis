##Pipeline for Orthology inference of the 19 species

#Step 1, run OrthoFinder to identify the orthologues sequence of the 19 species.
orthofinder -f ./pep -T iqtree -t 112 -M msa &

#Step 2, identify single-copy genes across the 18 species except Tdro.
python pich.sc.in18species.py

#Step 3, pick the best hit of Tdro in the identified single-copy genes. 
python pick.bestHit.inTdro.py

#Step 4, run Orthosnap to recover single-copy orthologs nested within large gene families with multiple homologs in one or more species
python rename.gene.trees.py #Rename leaf name in each of the gene trees as Orthofinder added '_' to the leaf name
python run_orthosnap.py
