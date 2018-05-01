import copy
import random
import numpy as np

class Graph():
	def __init__(self, row,col,coo):
		self.row = row
		self.col = col 
		self.coo = coo 
	
	def hypernet_walk(self, walk_length, start_node): 
		'''
		Simulate a random walk in the hypergraph. There are two ordinal steps, first choose which hypernet it will go to with uniform distribution. Second, if there is it can only walk within a hyper-net,then it will walk to other nodes within the current distribution. 
		'''
		row = self.row
		col = self.col
		coo = self.coo
		walk = [start_node]
		while len(walk) < walk_length:
			cur = walk[-1]
			# first choose which hypernet it will go to. 
			node_hypernets = col[row == start_node]    # hypernet that this node belongs to.
			hypernet_this = random.choice(node_hypernets)
			# second choose which node it will go to within this hypernet. 
			hypernet_nodes = row[col == hypernet_this] # nodes in this hypernet
			node_next = random.choice(hypernet_nodes)
			walk.append(node_next)
		return walk

	def simulate_walks(self, num_walks, walk_length):
		'''
		Repeatedly simulate random walks from each node. 
		'''
		row = self.row
		col = self.col
		nodes = copy.copy(row)		
		hypernets = copy.copy(col)	 
		walks = []
		coo = self.coo		# adjacency matrix
		for walk_iter in range(num_walks):	
			random.shuffle(nodes)
			for node in nodes:
				walks.append(self.hypernet_walk(walk_length=walk_length, start_node=node))
		return walks
			






