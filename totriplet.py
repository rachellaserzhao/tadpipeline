import numpy as np
from scipy.sparse import coo_matrix
import sys

data = np.loadtxt("/home/rachelz/pipeline/tadpipeline/cluster_test/outputMatrixFile.txt", skiprows=1, usecols=range(2,325))
triplet = coo_matrix(data)

newrow = [x+1 for x in triplet.row]
newcol = [x+1 for x in triplet.col]

with open ('trip.txt' , 'w') as output:
	sys.stdout = output
	for r, v, c in zip(newrow, triplet.data, newcol):
		print("{0}\t{1}\t{2}".format(r, v, c))
