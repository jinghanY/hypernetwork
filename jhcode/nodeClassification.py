import pickle
import numpy as np
#from sklearn import learn_model
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# import data feature and label
def read_file(fileName, dictName):
	f = open(fileName, "r")
	lines = f.readlines()
	feature = []
	label = []
	nodes = []
	ct = 0
	with open(dictName, 'rb') as f:
		d = pickle.load(f)
	for line in lines:
		ct = ct +1
		if ct ==1: continue
		ele = line.split(" ")
		ele = ele[:-1]
		ele = [x.strip("\n") for x in ele]
		ele = [float(x.strip("\n")) for x in ele]
		#print(d[int(ele[0])])
		#print(d[int(ele[0])+1])
		#g = input()
		label.append(d[int(ele[0])+1])
		feature.append(ele[1:])
	return np.array(feature), label, nodes


def del_new_label(Y_train, Y_test, X_test):
	new_label = set(Y_test) - set(Y_train)
	indices = [] 
	for lab in new_label:
		indice = [i for i, x in enumerate(Y_test) if x==lab]
		indices += indice
	# remove new labels
	labels = [x for i,x in enumerate(Y_test) if i not in indices]
	features = np.array([x for i,x in enumerate(X_test) if i not in indices])
	return features, labels
	# remove corresponding features

def main():
	datapath = "/project/tantra/jinghanY/hypernet/dataset/email-Eu-full"
	fileName = datapath+"/finalH.emb"
	#fileName = datapath+"/finalN.emb" 
	dictName = datapath+"/email-dict.pickle"
	feature, label, nodes = read_file(fileName, dictName)
	X_train, X_test, Y_train, Y_test = train_test_split(feature, label, test_size=0.33, random_state = 42)
	X_test, Y_test = del_new_label(Y_train, Y_test, X_test)
	model_log = LogisticRegression(solver = "lbfgs",multi_class="multinomial", max_iter= 100)
	model_log.fit(X_train,Y_train)
	Y_pred = model_log.predict(X_test)
	diff_labels_train = len(set(Y_train))
	diff_labels_test = len(set(Y_test))
	print('********summary**********')
	print(X_train.shape, "training data")
	print("There are ", diff_labels_train,"training labels")
	print(X_test.shape, "test data")
	print("There are ", diff_labels_test,"testing labels")
	
	print("*************************")
	# error rate
	ct = 0
	for i in range(len(Y_test)):
		if Y_test[i] == Y_pred[i]:
			ct = ct +1
	error_rate = ct/float(len(Y_test))
	print("accuracy")
	print(error_rate)
if __name__=="__main__":
	main()
