import numpy as np
from scipy.sparse import coo_matrix
import sys

data = np.loadtxt("simulatedmatrix.txt", skiprows=1, usecols=range(1,4602))
triplet = coo_matrix(data)

newrow = [int(x+1) for x in triplet.row]
newcol = [int(x+1) for x in triplet.col]
newdata = [int(x) for x in triplet.data]

with open ('simulatedtriple.txt' , 'w') as output:
	sys.stdout = output
	for r, c, v in zip(newrow, newcol, newdata):
		print("{0}\t{1}\t{2}".format(r, c, v))
