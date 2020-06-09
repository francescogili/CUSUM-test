# CUSUM-test

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import *

def find_min_array(index, array):
    i=0
    minimum = array[0]
    while i <= index:
        if minimum <= array[i]:
            i += 1
        else:
            minimum = array[i]
            i += 1
    return minimum


print("Behaviour of the LLR function and of the observations of X")

s = np.random.normal(0, 1, 120)
change_point = randint(1,100)

sigma = 1
x = np.zeros(101)
    #print(x)
sum_up = np.zeros(101)

theta_z = input("Enter the mean before the changepoint: ") 
theta_o = input("Enter the mean after the changepoint: ") 
theta_1 = float(theta_o)
theta_0 = float(theta_z)

p_0 = 1
p_1 = 1


j=change_point
i=1

while i<change_point:
    x[i] = s[i]
    #print(x[i])
    p_0 = np.exp((-1/(2*((sigma)**2)))*((x[i] - theta_0)**2))
    p_1 = np.exp((-1/(2*((sigma)**2)))*((x[i] - theta_1)**2))
    
    sum_up[i] = sum_up[i-1] + np.log(p_1 / p_0)

    i += 1

s = np.random.normal(2, 1, 120)

while j<101:
    x[j] = s[j]
    p_0 = np.exp((-1/(2*((sigma)**2)))*((x[j] - theta_0)**2))
    p_1 = np.exp((-1/(2*((sigma)**2)))*((x[j] - theta_1)**2))
    
    sum_up[j] = sum_up[j-1] + np.log(p_1 / p_0)

    j += 1 
    
k=1
change_point_detected = 0

while k < 101:
    g_n = sum_up[k] - find_min_array(k,sum_up)
    h = 3
    if g_n < h:
        k += 1
    else:
        change_point_detected = k
        k = 101
        
            
print("This is the real changepoint: " + str(change_point))
print("This is the changepoint detected: " + str(change_point_detected))

    
plt.plot(sum_up)
plt.xlabel(r'$Time$')
plt.ylabel(r'$\sum_i^n \log{f_{\theta_1} \left( X_i \right)} / {f_{\theta_0} \left( X_i \right)}$')
plt.title('Plot of the behaviour of S_n')
plt.show()



w=0
v = np.zeros(101)
while w < 101: 
    v[w] = theta_0
    w += 1


r=0
t = np.zeros(101)
while r < 101: 
    t[r] = theta_1
    r += 1


plt.plot(x)
plt.plot(v, 'r--', label = r'$\theta_0$', color = 'r')
plt.plot(t, 'b--', label = r'$\theta_1$', color = 'b')
plt.xlabel(r'$Time$')
plt.ylabel(r'$X$')
plt.title('Plot of the behaviour of X')
plt.legend(loc = 'best')
plt.show()
