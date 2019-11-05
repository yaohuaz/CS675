import sys
import decimal as dc

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
eta_list = ( .0001, .00001, .000001, .0000001, .00000001, .000000001,
.0000000001, .00000000001)
best_eta = 0
best_error = 1000000000000

error0 = 1
error1 = 0
while(abs(error0-error1) > 0.001):
	#rest dellf
	dellf = []
	for j in range(0,cols):
		dellf.append(0)
	
	#calculate dellf
	for i in range(0,rows):
		if(trainlabels.get(i) != None):
			dp = 0
			for j in range(0,cols):
				dp +=w[j]*data[i][j]
			for j in range(0,cols):
				dellf[j] += (trainlabels[i]-dp)*data[i][j]
        

	best_error = 1000000000000
	best_eta = 0
	#set eta_list
	for k in range(0, len(eta_list),1):
		eta = eta_list[k]

		#update gradient descent
		for j in range(0,cols):
			w[j] = w[j]+(eta*dellf[j])
	
		#compute error	
		error0 = error1  
		error1 = 0
		for i in range(0,rows):
			if(trainlabels.get(i) != None):
				dp = 0
				for j in range(0,cols):
					dp +=w[j]*data[i][j]
				error1 += (trainlabels[i]-dp)**2
		if(error1 < best_error):
			best_error = error1
			best_eta = eta
		else:
			break
#print(best_eta)


for i in range(0,rows):
    if(trainlabels.get(i) == None):
        dp = 0
        for j in range(0,cols):
            dp += w[j]*data[i][j]
        if(dp>0):
            print ("1 ",i)
        else:
            print ("0 ",i)   
