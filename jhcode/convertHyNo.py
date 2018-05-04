import numpy as np

# import nodes and features 
def read_file(fileName):
	f = open(fileName, "r")
	lines = f.readlines()
	feature = []
	nodes = []
	ct = 0
	for line in lines:
		ct = ct+1
		if ct==1: continue
		ele = line.split(" ")
		ele = [float(x.strip("\n")) for x in ele]
		nodes.append(int(ele[0]))
		feature.append(ele[1:])
	return np.array(feature), nodes

def del_different_label(standa, nodes, feature):
	new_nodes = set(nodes) - set(standa)
	print("new_nodes")
	print(new_nodes)
	indices = []
	for node in new_nodes:
		indice = [i for i, x in enumerate(nodes) if x == node]
		indices += indice
	nodes = [x for i,x in enumerate(nodes) if i not in indices]
	features = np.array([x for i, x in enumerate(feature) if i not in indices])
	return features,nodes

def convertNode2H(featureH, nodesH, featureN, nodesN):
	# here nodesH and nodesN has same nodes, just different in sequence.
	nodesN_enumerate = list(enumerate(nodesN))
	nodesN_enumerate.sort(key=lambda x:nodesH.index(x[1]))
	ind = [x for x,_ in nodesN_enumerate]
	print(ind)
	nodesN = [nodesN[i] for i in ind]
	featureN = np.array([featureN[i] for i in ind])
	return featureN, nodesN

def writefile(fileName, feature, node):
	f = open(fileName, "w")
	f.write(str(len(node))+" "+ str(128))
	f.write("\n")
	print("check here")
	n,m = np.shape(feature)
	ct = 0
	for i in range(n):
		ct += 1
		f.write(str(node[i])+ " ")
		for j in range(m):
			f.write(str(feature[i,j])+" ")
	f.close()

def main():
	data_path = "/project/tantra/jinghanY/hypernet/dataset/email-Eu-full"
	fileName_hypernet = data_path+"/my.emb"
	fileName_node2vec = data_path+"/email.emb"
	feature_hypernet, nodes_hypernet = read_file(fileName_hypernet)
	feature_node2vec, nodes_node2vec = read_file(fileName_node2vec)
	print("size of feature_hypernet") 
	print(np.shape(feature_hypernet))
	print("len ")
	print(len(nodes_hypernet))
	print("size of feature_node2vec") 
	print(np.shape(feature_node2vec))
	print("len")
	print(len(nodes_node2vec))
	feature_hypernet, nodes_hypernet = del_different_label(nodes_node2vec, nodes_hypernet, feature_hypernet)
	#fileout_node2vec = data_path + "/finalN.emb"
	#writefile(fileout_node2vec, feature_node2vec, nodes_node2vec)
	feature_node2vec, nodes_node2vec = del_different_label(nodes_hypernet, nodes_node2vec, feature_node2vec)
	print("size")
	print(np.shape(feature_hypernet))
	print(len(nodes_hypernet))
	print(np.shape(feature_node2vec))
	#fileout_node2vec = data_path + "/finalN.emb"
	#writefile(fileout_node2vec, feature_node2vec, nodes_node2vec)
	feature_node2vec, nodes_node2vec = convertNode2H(feature_hypernet, nodes_hypernet, feature_node2vec, nodes_node2vec)
	fileout_hypernet = data_path + "/finalH.emb"
	fileout_node2vec = data_path + "/finalN.emb"
	writefile(fileout_hypernet, feature_hypernet, nodes_hypernet)
	writefile(fileout_node2vec, feature_node2vec, nodes_node2vec)

main()
