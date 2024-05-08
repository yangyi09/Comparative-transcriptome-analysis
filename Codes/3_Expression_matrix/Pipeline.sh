##Pipeline for processing the RNA-seq file and generate expression matrix for downxxx analyses.

#Step1, run fastp for quality control and filtering on raw RNA-seq data of each sample
fastp --thread 112 -i $R1 -I $R2 -o $clean_R1 -O clean_R2

#Step 2, run STAT to align the clean RNA-seq data to each species' reference genome
python buildIndex.STAR.py ##Build index for gene species
python run_STAR.py

#Step 3, run featureCounts to count for expresseion levels of each gene in each sample
python run.featureCounts.py

#Step 4, calculate TPM values and normalized to TPM10K
python CalTPM.py
python TPM10K.py
python median.py

#Step 5, generate expression matrics of the 1,479 single copy gene, 3,xxx shared orthogroups, and xxxx shared GO terms.
python get.scExpressionMatrix.py
python get.OGLevelExpressionMatrix.py
python get.GOLevelExpressionMatrix.py