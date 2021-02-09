#!/usr/bin/env python
# coding: utf-8

# In[14]:





# In[28]:


import numpy as np

nos = 4  # no of states
A = ['l', 'r']  # actions
noa = 2 #number of actions

# R [from state][action]
#: [0 to left, 0 to right], [1 to left, 1 to right], [2 to left, 2 to rght]]
# : [0 : left, right,
#    1: left, right,
#    2: left, right]
R = [[-1, -1], [-1, -1], [-1, -1]]

# P [from state] [to state] [action]
# : [[0->0 (for left prob table), 0->0 ( for right prob table)], [0->1,0->1], [ 0->2, 0->2], [ 0->3, 0->3]]
# similarly for 1,2,3
P = [
    #state 0
    [[0.8, 0.2], [0.2, 0.8], [0, 0], [0, 0]],
    #state 1
    [[0.8, 0.2], [0, 0], [0.2, 0.8], [0, 0]],
    #state 2
    [[0, 0], [0.8, 0.2], [0, 0], [0.2, 0.8]],
]

delta = 0.01
gamma = 0.25
max_diff = 0

V = [0, 0, 0, 10]  # utilities of each state




convg = 0
V = np.array(V).reshape(4,1)
itera = 0

while convg == 0:
    states = []
    
    v_old = V
    #print("old value = ", v_old)
    for i in range(3):
        #print("iteration ==========   ", i)
        #print("p[i] = ", P[i])
        v_new  = np.multiply(P[i],v_old)
        #print("new values for state s = ", i, " in iteration ", itera, " are", v_new)
        v_new  = np.sum(v_new, axis = 0)
        net = v_new*0.25
        #print("net values == ", net)
        final_val = np.max((-1 + net))
        #print("final val = ", final_val)
        states.append(final_val)
    states.append(10)
    
    #V[i] = final_val
    #print("sates = ", states)
    V  = np.array(states).reshape(4,1)
    #print("after iteration = ", itera, " updates state values = ", V)
    print("V updated after iteration", itera, "is = ", V)
    itera = itera+1
    max_diff = np.max(np.subtract(v_old, V))
    print("max_diff = ", max_diff)
    if max_diff < delta:
        convg = 1
    #convg = convg + 1
    


# In[ ]:




