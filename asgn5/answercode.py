import math
import sys
import random as ran
from operator import mul

# Get The Data and Labels
dataf = sys.argv[1];
labelf = sys.argv[2];
f = open(dataf);
l = f.readline();
i = 0;
data = [];

while(l != ''):
    a = l.split();
    l2 = [];
    for j in range(0, len(a), 1):
        l2.append(float(a[j]));
    data.append(l2);
    l = f.readline();
    data[i].append(1);
    i += 1;

rows = len(data);
cols = len(data[0]);

f = open(labelf);
traininglabels = {};
n = [];
n.append(0);
n.append(0);
l = f.readline();
while (l != ''):
    a = l.split();
    traininglabels[int(a[1])] = int(a[0]);
    l = f.readline();
    n[int(a[0])] += 1;
    if (traininglabels[int(a[1])] == 0):
        traininglabels[int(a[1])] = -1;

# Initilization

w = [];

for j in range(0, cols, 1):
    w.append(((0.02 * ran.random()) - 0.01));
    
# Gradient Descent Iteration
eta_list = [.0001, .00001, .000001, .0000001, .00000001, .000000001, .0000000001, .00000000001]
stop = 0.001;
previous = 1000000000;
objective = previous - 10;
dp = 0;
best_eta = 1;

dellfunction = [];
for i in range(0, cols, 1):
    dellfunction.append(0);

while (previous - objective > stop):

    previous = objective;
    # Reset dellfunction to 0
    for j in range(0, cols, 1):
        dellfunction[j] = 0

    # Compute dellfunction
    for i in range(0, rows, 1):
        if (traininglabels.get(i) != None):
            dp = sum(map(mul, w, data[i]));
            for j in range(0, cols, 1):
                dellfunction[j] += (traininglabels[i] - dp)*(data[i][j]);
                #print('delf = ',dellfunction)
                #break
    best = 1000000000000;
    for k in range(0, len(eta_list), 1):
        e = eta_list[k]
        # Update w (locally)
        for j in range(0, cols, 1):
            w[j] = w[j] + e * dellfunction[j];
        #print(w)
        # Compute Error
        error = 0;
        for i in range(0, rows, 1):
            if (traininglabels.get(i) != None):
                error += (traininglabels[i] - (sum(map(mul, w, data[i]))))**2;
        objective = error;

        # Set best objective/eta
        if(objective < best):
            best_eta = e;
            best = objective;

        # Remove w
        for j in range(0, cols, 1):
            w[j] = w[j] - e * dellfunction[j];
        #print(e, objective, previous);

    e = best_eta;
    # Update w
    for j in range(0, cols, 1):
            w[j] = w[j] + e * dellfunction[j];

    # Compute Error
    error = 0;
    for i in range(0, rows, 1):
        if (traininglabels.get(i) != None):
            error += (traininglabels[i] - (sum(map(mul, w, data[i]))))**2;
    objective = error;
    print("best_eta=", best_eta, " Objective=", error);
    #break 
#print("w = ");
n1 = 0;
for j in range(0, cols - 1, 1):
    n1 += w[j]**2;
    #print(w[j]);
#print("\n");
n1 = math.sqrt(n1);
distance = abs(w[len(w) - 1]/n1);
#print("Distance to the Origin = ", distance);
'''
# Prediction
for i in range(0, rows, 1):
    if (traininglabels.get(i) == None):
        dp = (sum(map(mul, w, data[i])));
        if (dp > 0):
            print("1", i);
        else:
            print("0", i);
'''
