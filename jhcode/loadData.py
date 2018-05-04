import pickle
# This file is used to load 

# load the nverts file 
# nverts: the number of vertices within each simplex. nth line corresponds to the nth simplex.  

# laod the simplices file 
# simplices: a contiguous list of the nodes comprising the simplices

# read file
def read_file(fileName):
	f = open(fileName, "r")
	lines = f.readlines()
	ele = [int(x.strip('\n')) for x in lines]
	return ele

# create tuple
def simplices_to_nverts(nverts, simplices):
	ct = 0
	t = ()
	i = 0
	for index in nverts:
		i = i+1
		t = t + ((i,simplices[ct:ct+index]),)
		ct = ct + index
	print(t)
	return t

def compress_hypernets(nverts, simplices, num):
	'''
	num = how many nverts that we want to use for training and testing. 
	'''
	nverts = nverts[:num]
	num_simplices = sum(nverts)
	simplices = simplices[:num_simplices]
	return nverts, simplices

# write down tuple using pickle

if __name__ == "__main__":
	#hm_path = "/project/tantra/jinghanY/hypernet/dataset/drugSub_25/NDC-substances/test"
	hm_path = "/project/tantra/jinghanY/hypernet/dataset/email-Eu-full"
	fileName_nverts = hm_path +"/email-Eu-full-nverts.txt"
	fileName_simplices = hm_path+"/email-Eu-full-simplices.txt"
	nverts = read_file(fileName_nverts)
	simplices = read_file(fileName_simplices)
	#simplices_tuple = simplices_to_nverts(nverts, simplices)

	[nverts, simplices]=compress_hypernets(nverts, simplices,2000)
	fileName_nverts = hm_path + "/nverts_small.pickle"
	with open(fileName_nverts,'wb') as f:
		pickle.dump(nverts, f)
	
	fileName_simplices = hm_path + "/simplices_small.pickle"
	with open(fileName_simplices, 'wb') as f:
		pickle.dump(simplices, f)

	#fileName_simplices_tuple = hm_path + "/simplices_tuple.pickle"
	#with open(fileName_simplices_tuple, 'wb') as f:
	#	pickle.dump(simplices_tuple, f)



