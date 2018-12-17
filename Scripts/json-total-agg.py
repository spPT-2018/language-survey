import json
import ast
import os


dirr = '5krepos/'
filelist = os.listdir(dirr)
result_dict = {'C++' : 0}

def addSingleJson(filedest):
	print("Processing file: " + filedest)
	with open(dirr + filedest, "r") as read_file:
		data = json.load(read_file)
		#print(data)
		for k in data.keys():
			if k in result_dict:
				#print("MATCH for " + k+ "\nAdding " + str(data[k]))

				result_dict[k] += int(data[k])
			else:
				#print("No match for " + k)
				result_dict[k] = int(data[k])


for f in filelist:
	addSingleJson(f)



with open('total-sum-for-all-lang.json', 'w') as fp:
	json.dump(result_dict, fp)
