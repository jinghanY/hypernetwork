import copy
import numpy as np
from scipy.sparse import coo_matrix

class Hypernetwork:
	def __init__(self, nverts, simplices):
		self.nverts = nverts
		self.simplices = simplices 
		
	def adjacencyMatrix(self):
		nverts = self.nverts
		simplices = self.simplices
		num_app = len(simplices)
		row = np.array(copy.copy(simplices))-1
		col = np.zeros(num_app)
		ct = 0
		# Constructing a matrix with duplicate indices
		# row is just the simplices
		for i in range(len(nverts)):
			# i th simplice (i is actually the simplice-th number - 1. But it is more convinient to starts from zeros. However, we should convert aka + 1 for the label conversion.)
			nvert = nverts[i]
			col[ct:(ct+nvert)] = i
			ct = ct + nvert
		data = np.ones(num_app)
		coo = coo_matrix((data, (row, col)), shape=(num_app,num_app))
		return coo, row, col
