#!/bin/bash
/home/rachelz/.linuxbrew/bin/bwa mem -t 8 -M -U 0 -L "0,0" -R "@RG\tID:BWA\tSM:test" /home/rachelz/pipeline/genomes/hg38.fa /home/rachelz/pipeline/test_data/dixon_2M/SRR400264_00_R1.fastq | /home/rachelz/.linuxbrew/bin/samtools sort -n -O BAM -o cluster_test/alignment.R1.bam
/home/rachelz/.linuxbrew/bin/bwa mem -t 8 -M -U 0 -L "0,0" -R "@RG\tID:BWA\tSM:test" /home/rachelz/pipeline/genomes/hg38.fa /home/rachelz/pipeline/test_data/dixon_2M/SRR400264_00_R2.fastq | /home/rachelz/.linuxbrew/bin/samtools sort -n -O BAM -o cluster_test/alignment.R2.bam
/home/rachelz/.linuxbrew/bin/python /home/rachelz/HiC-Pro/scripts/mergeSAM.py -f cluster_test/alignment.R1.bam -r cluster_test/alignment.R2.bam -o cluster_test/paired.bam
/home/rachelz/.linuxbrew/bin/python /home/rachelz/HiC-Pro/scripts/mapped_2hic_dnase.py -a -v -r cluster_test/paired.bam -o cluster_test/
