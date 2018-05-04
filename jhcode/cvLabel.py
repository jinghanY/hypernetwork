import pickle
import re
def read_file(fileName):
	f = open(fileName, "r")
	lines = f.readlines()
	ct = 0
	eles = []
	for line in lines:
		ct = ct+1
		element = line.split(" ")
		element_ele = [int(x.strip('\n'))+1 for x in element]
		eles.append(element_ele)
		# every element plus one, for the convention of nverts and simplices. 
	return eles

def create_dict(element_list):
	d ={}
	for i in range(len(element_list)):
		element_ele = element_list[i]
		#g = input()
		d[element_ele[0]]=element_ele[1]
	return d
		
def main():
	data_path = "/project/tantra/jinghanY/hypernet/dataset/email-Eu-full"
	fileName = data_path+"/email-Eu-core-department-labels.txt"
	element_list = read_file(fileName)
	d = create_dict(element_list)
	fileName_dict = data_path+"/email-dict.pickle"
	with open(fileName_dict, 'wb') as handle:
		pickle.dump(d, handle, protocol=pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
	main()
