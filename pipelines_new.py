#!/usr/bin/env python2.7
import os, sys, re, io
import ConfigParser
import shutil
import socket
import argparse
from subprocess import call
sys.path.append('/home/rachelz/HiC-Pro/scripts')
import mergeSAM

# read configuration file
config = ConfigParser.ConfigParser()
config_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), "config.ini")
config.read(config_file)

def parse_options():

	parser = argparse.ArgumentParser(description='pipeline for bwa mem alignmnet and hi-c pro contact map')

	parser.add_argument('-r1', action='store', dest='r1', help="Replicate 1 (fastq file)", required=True, metavar='<R1.fastq>')
	parser.add_argument('-r2', action='store', dest='r2', help="Replicate 1 (fastq file)", required=True, metavar='<R2.fastq>')
	parser.add_argument('-e', action='store', default='', dest='experiment', help='experiment type', metavar='<experiment>')
	parser.add_argument('-g', default='hg38', action='store', dest='genome', help="Genome assembly (hg19 or hg38; default = hg38)", metavar='<genome>')
	parser.add_argument("-o", "--output-dir", default="./", action="store", dest="output_dir", help="Output directory will be pwd/output (default = ./)", metavar="<output_dir>")
	parser.add_argument("-p", action="store", dest="prefix", required=True, help="Prefix (identifies output dir/files)", metavar="<prefix>")
	parser.add_argument("-q", "--qsub", default=False, action="store_true", dest="submit", help="Submit PBS script to queue (default = False)")
   	parser.add_argument("-w", "--walltime", default=168, action="store", type=int, dest="walltime", help="Walltime (in hours; default = 168; i.e. one week)", metavar="<walltime>")


	options = parser.parse_args()
	return options

def ConfigSectionMap(section):
    dict1 = {}
    options = config.options(section)
    for option in options:
        try:
            dict1[option] = config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

def alignment(r1, r2, genome, prefix, outdir):

	header = r'@RG\tID:BWA\tSM:'

	cmd_r1 = bwa + ' mem ' + '-t ' +  processors + ' -M -U 0 -L "0,0" -R "' + header + prefix + '"'+ \
	' ' + westgrid_config[genome] + ' ' + r1 + ' | ' + samtools + ' sort -n -O BAM -o ' + outdir+ '/' + 'alignment.R1.bam'

	cmd_r2 = bwa + ' mem ' + '-t ' +  processors + ' -M -U 0 -L "0,0" -R "' + header + prefix + '"' + \
	' ' + westgrid_config[genome] + ' ' + r2 + ' | ' + samtools + ' sort -n -O BAM -o ' + outdir+ '/' + 'alignment.R2.bam'

	with io.open('test.sh', 'w') as file:
    file.write(u'#!/bin/bash')
    file.write(u'echo $1')
	
	if not closed:
		file.close()

def merge()

python ~/HiC-Pro/scripts/mergeSAM.py -f alignment.R1.bam -r alignment.R2.bam -o ./test.bwt2pairs.bam

	

if __name__ == '__main__':
	
	options = parse_options()
	westgrid_config = ConfigSectionMap(config.sections()[0])
	samtools = westgrid_config['samtools']
	processors = westgrid_config['processors']
	fastqc = westgrid_config['fastqc']
	picard = westgrid_config['picard']
	memory = westgrid_config['memory']
	trimmomatic = westgrid_config['trimmomatic']
	queue = westgrid_config['queue']
	bwa = westgrid_config['bwa']
	hg38 = westgrid_config['hg38']
	hg19 = westgrid_config['hg19']
	email = westgrid_config['email']
	
	if not os.path.exists(os.path.abspath(options.output_dir)):
		os.makedirs(os.path.abspath(options.output_dir))

	if options.genome != "hg19" and options.genome != "hg38":
		parser.error('invalid genome')
	else:
		alignment(options.r1, options.r2, options.genome, options.prefix, options.output_dir)
		merge()
	
