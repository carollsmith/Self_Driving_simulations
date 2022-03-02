# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 19:22:23 2022

@author: 91996
"""
#%% importing necessary libraries
import numpy as np
import matplotlib.pyplot as plt


class Bicycle():
    def __init__(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0
        self.lr = 1.2
        self.L = 2
        self.W_max = 1.22
        self.sample_time = 0.01
        
    def reset(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta =0 
        self.beta = 0
        
class Bicycle(Bicycle):
    def step(self,v,w):
        if w > 0:
            w = min(w,self.W_max)
        else :
            w = max(w,-self.W_max)
        self.xc = self.xc + self.sample_time*v*np.cos(self.theta+self.beta)
        self.yc = self.yc + self.sample_time*v*np.sin(self.theta+self.beta)
        self.theta =  self.theta + self.sample_time*(v*np.cos(self.beta)*np.tan(self.delta)/self.L)
        self.delta =  self.delta + w*self.sample_time
        self.beta = np.arctan((self.lr*np.tan(self.delta))/self.L)
        pass
    
sample_time = 0.01
time_end = 30
model = Bicycle()

radius = 8

t_data = np.arange(0,time_end,sample_time)
x_data = np.zeros_like(t_data)
y_data = np.zeros_like(t_data)
v_data = np.zeros_like(t_data)
w_data = np.zeros_like(t_data)

n = t_data.shape[0]
v_data[:] = ((2*np.pi*radius)*2)/time_end
delta_req = 0.993*np.arctan(model.L/radius)


for i in range(n):
    x_data[i] = model.xc
    y_data[i] = model.yc
    
    if i < n/8:
        if model.delta < delta_req:
            w_data[i] = model.W_max
            model.step(v_data[i], w_data[i])
            
        else :
            w_data[i] = 0
            model.step(v_data[i], w_data[i])
            
    elif i < 5.1*n/8:
          if model.delta > -delta_req:
              w_data[i] = -model.W_max
              model.step(v_data[i], w_data[i])
             
          else :
              w_data[i] = 0
              model.step(v_data[i], w_data[i])        
        
        
    elif i < n:
          if model.delta < delta_req:
                  w_data[i] = model.W_max
                  model.step(v_data[i], w_data[i])
                 
          else :
                  w_data[i] = 0
                  model.step(v_data[i], w_data[i])      
                 
plt.axis('equal')
plt.plot(x_data, y_data,label='Learner Model')
plt.legend()
plt.show()





        
        
        
        