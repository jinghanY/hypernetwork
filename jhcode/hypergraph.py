import numpy as np

class Hypernetwork:
	def __init__(self, n,m):
		# n: the number of hypernets
		# m: the number of vertices
		self.adjacency_matrix_trans = np.zeros((n,m))
	# the input hypernets is a tuple ((1, [1, 2, 3]), (2, [1, 2, 3]))	
	# the input hypernet is a tuple (1, [1,2,3]), 1th hypernet consists of nodes 1, 2, 3
	def adjacencyMatrix(self, hypernets):
		for i in range(len(hypernets)): # ith hypernet
			hypernet = hypernets[i]
			hypernet_index = hypernet[0] # a scalar
			hypernet_nodes = hypernet[1] # a list 
			for j in range(len(hypernet_nodes)):
				self.adjacency_matrix_trans[hypernet_index-1, hypernet_nodes[j]-1] = 1
		self.adjcency_matrix =  np.transpose(self.adjacency_matrix_trans)
		
	def getHypernet(self, node):
		'''
		For a given node, we can get the hypernet for this given node. 
		'''
		adjMat = self.adjcency_matrix
		index = node -1
		hypernet = np.nonzero(adjMat[index])[0] + 1
		return hypernet



#a = Hypernetwork(3,4)
#b = ((1, [1,3]), (2, [ 2, 3,4]), (3,[1,2,3,4]))
#print(a.adjacencyMatrix_trans(b))


