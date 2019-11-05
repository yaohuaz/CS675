import sys
import random
import numpy as np
import math
from operator import mul 

datafile = sys.argv[1]
f = open(datafile)
data = []
i = 0
l = f.readline()

#read data
while(l != ''):
	a = l.split()
	l2 = []
	for j in range(0, len(a), 1):
		l2.append(float(a[j]))
	l2.append(float(1))
	data.append(l2)
	l = f.readline()
rows = len(data)
cols = len(data[0])

#read labels
labelfile = sys.argv[2]
f = open(labelfile)
trainlabels = {}
l = f.readline()
while(l != ''):
	a = l.split()
	trainlabels[int(a[1])] = int(a[0])
	if trainlabels[int(a[1])] == 0:
		trainlabels[int(a[1])] = -1
	l = f.readline()

f.close()
#initialize w

w = []
for j in range(0, cols, 1):
	w.append(0)
for j in range(0, cols, 1):
	w[j] = (0.02 * random.random()) - 0.01

eta_list = [.0001, .00001, .000001, .0000001, .00000001, .000000001,
.0000000001, .00000000001]
best_eta = 0
best_error = 1000000000000

#gradient descent interation
#eta = 0.0001

#for k in range(0, len(eta_list), 1):
#	eta = eta_list[k]
obj = 0
preobj = 20 
error = 0
count = 0
while(abs(preobj-obj)>0.001):
	preobj = obj
	count +=1
	delf = []
	for j in range(0, cols, 1):
		delf.append(0)
	#if(count%100 == 0):
	#	print('iteration ',count)
	#compute dellf
	for i in range(0, rows, 1):
		if trainlabels.get(i) != None:
			dp = np.dot(w, data[i])
			#print(dp)
			for j in range(0, cols, 1):
				delf[j] += (trainlabels[i] - dp) * (data[i][j])
				#print('delf = ',delf)
	#eta_list
	for k in range(0, len(eta_list), 1):
		eta = eta_list[k]
		#update gradient
		for j in range(0, cols, 1):
			w[j] = w[j] + eta * delf[j]
		#print(w)	
		#compute error
		#preobj = error
		error = 0
		for i in range(0, rows, 1):
			if trainlabels.get(i) != None:
				error += (trainlabels[i] - sum(map(mul, w, data[i])))**2
		#print('diff =', abs(preobj - error))		
		if(error < best_error):
			best_error = error
			best_eta = eta
		#remove gradient
		for i in range(0, cols, 1):
			w[j] = w[j] - eta * delf[j]
		print(eta, error)
	beta = best_eta
	for i in range(0, cols, 1):
		w[j] += beta * delf[j]
	
	err = 0
	for i in range(0, rows, 1):
		if trainlabels.get(i) != None:
			err += (trainlabels[i] - sum(map(mul, w, data[i]))) ** 2
	obj = error
	print(count,'obj:', obj)
	print(count,'preobj:', preobj)
#normw = 0
#for j in range(0, (cols-1), 1):
#	normw += w[j] ** 2
#	print('w =', w)
#
#normw = math.sqrt(normw)
#print('||w||=', normw)
#dorigin =abs(w[len(w)-1]/normw)
#print('distance to origin:', dorigin) 

'''
###prediction###
for i in range(0, rows, 1):
	if(trainlabels.get(i) == None):
		dp = np.dot(w, data[i])
		if (dp > 0):
			print("1 ", i)
		else:
			print("0 ", i)
'''
