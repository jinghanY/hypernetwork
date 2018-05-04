import math
import argparse
import copy
import hynode2vec 
import numpy as np
import scipy.sparse as sps
import hypergraph_sparse as hy
import pickle
from gensim.models import Word2Vec

def parse_args():
	'''
	Parses the hynode2vec arguments.
	'''
	parser = argparse.ArgumentParser(description="Run hynode2vec.")
	# input 
	# output
	parser.add_argument('--dimensions', type=int, default=128, help='Number of dimensions. Default is 128')
	parser.add_argument('--walk-length', type=int, default=80, help='length of walk per source, Default is 80')
	parser.add_argument('--num-walks', type=int, default=10, help='Number of walks per source, Default is 10')
	parser.add_argument('--window-size', type=int, default=10, help='Context size for optimization. Default is 10')
	parser.add_argument('--iter', default=1, type=int, help='Number of epochs in SGD')
	parser.add_argument('--workers', type=int, default=8, help='Number of parallel workers, Default is 8.')
	parser.add_argument('--output', nargs='?', default='karate_small.emb', help='Embeddings path')
	return parser.parse_args()


def learn_embedding(walks):
	'''
	Learn embeddings by optimizing the Skipgram objective using SGD
	'''
	walks = [list(map(str,walk)) for walk in walks]
	model = Word2Vec(walks, size=args.dimensions, window=args.window_size, min_count=0, sg=1, workers=args.workers, iter=args.iter)
	model.wv.save_word2vec_format(args.output)
	return

def main(args):
	data_path = "/project/tantra/jinghanY/hypernet/dataset/email-Eu-full"
	fileName_simplices_tuple = data_path + "/simplices_tuple.pickle"
	
	
	fileName_nverts = data_path + "/nverts_small.pickle"
	with open(fileName_nverts,'rb') as f:
		nverts = pickle.load(f)
	
	fileName_simplices = data_path + "/simplices_small.pickle"
	with open(fileName_simplices,'rb') as f:
		simplices= pickle.load(f)
	
	num_nverts = max(simplices)
	num_simplices = len(nverts)
	a = hy.Hypernetwork(nverts, simplices)
	[hypMat,row,col] = a.adjacencyMatrix()
	# how to get walks
	G = hynode2vec.Graph(row,col,hypMat)
	walks = G.simulate_walks(args.num_walks, args.walk_length)
	learn_embedding(walks)	

if __name__ == "__main__":
	args = parse_args()
	main(args)
