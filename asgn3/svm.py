import sys
datafile = sys.argv[1]
file = open(datafile)
data = []
raw1 = file.readlines()
for i in range(len(raw1)):
	temp1 = raw1[i].split()
	temp2 = []
	for j in range(0,len(temp1)):
		temp2.append(float(temp1[j]))
	temp2.append(1)
	data.append(temp2)
rows = len(data)
cols = len(data[0])
file.close()


labelfile = sys.argv[2]
file = open(labelfile)
trainlabels = {}
raw2 = file.readlines()
for i in range(len(raw2)):
	temp3 = raw2[i].split()
	trainlabels[int(temp3[1])] = int(temp3[0])
	if(trainlabels[int(temp3[1])] == 0):
		trainlabels[int(temp3[1])] = -1
file.close()


import random
w = []
for j in range(0,cols):
	w.append(0.02*random.random()-0.01)


eta=0.001
error0 = 1
error1 = 0
while(abs(error0-error1) > 0.000000001):
	dellf = []
	for j in range(0,cols):
		dellf.append(0)
	for i in range(0,rows):
		if(trainlabels.get(i) != None):
			dp = 0
			for j in range(0,cols):
				dp += w[j]*data[i][j]
			if(trainlabels.get(i)*dp < 1):
				for j in range(0,cols):
					dellf[j] += ((trainlabels[i]-dp)*data[i][j])
                
	for j in range(0,cols):
		w[j] = w[j]+(eta*dellf[j])
        
	error0 = error1  
	error1 = 0
	for i in range(0,rows):
		if(trainlabels.get(i) != None):
			dp = 0
			for j in range(0,cols):
				dp += w[j]*data[i][j]	
			gradient = 1 - trainlabels.get(i)*dp
			if(gradient > 0):
				error1 += gradient
	#print(error1)


print("w =")
normw = 0
for j in range(0,cols-1):
    normw += w[j]**2
    print (w[j])
print("\t")
normw = normw**0.5
print ("||w||=",normw)
print("\t")
d_origin = w[len(w)-1]/normw
print ("d_origin=",abs(d_origin))
print("\t")


for i in range(0,rows):
	if(trainlabels.get(i) == None):
		dp = 0
		for j in range(0,cols):
			dp += w[j]*data[i][j]
		if(dp>0):
			print ("1 ",i)
		else:
			print ("0 ",i)  
print("\t")   

