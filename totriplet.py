import numpy as np

data = np.loadtxt("outputMatrixFile.txt", skiprows=1, usecols=range(2,325))
from scipy.sparse import coo_matrix
triplet = coo_matrix(data)

newrow = [x+1 for x in triplet.row]
newcol = [x+1 for x in triplet.col]

with open ('trip.txt' , 'a') as output:
	for r, v, c in zip(newrow, triplet.data, newcol):
		output.write("{0}\t{1}".format(r, v, c))