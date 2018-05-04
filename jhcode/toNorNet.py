import numpy as np
import pickle
import itertools

def toNorm(nverts, simplices):
	res = []
	st = 0
	ct = 0
	#print(simplices[:50])
	for index in nverts:
		st +=1
		hypernet = simplices[ct:ct+index]
		nm= list(itertools.combinations(hypernet,2))
		res += nm
		#print(res)
		ct += index
	return np.array(res)

def writefile(fileName,lst):
	f = open(fileName, "w")
	for i in range(np.shape(lst)[0]):
		firstEle = lst[i][0]
		secondEle = lst[i][1]
		f.write(str(firstEle)+" "+str(secondEle))
		f.write("\n")
	f.close()

def main():
	data_path = "/project/tantra/jinghanY/hypernet/dataset/email-Eu-full"
	fileName_simplices_tuple = data_path + "/simplices_tuple.pickle"

	fileName_nverts = data_path + "/nverts_small.pickle"
	with open(fileName_nverts,'rb') as f:
		nverts = pickle.load(f)
	
	fileName_simplices = data_path + "/simplices_small.pickle"
	with open(fileName_simplices, 'rb') as f:
		simplices = pickle.load(f)
	lst = toNorm(nverts,simplices)
	fileName_out = data_path + "/normalNodes.edgelist"
	writefile(fileName_out,lst)

if __name__ == "__main__":
	main()
