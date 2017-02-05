"""
Jhonatan da Silva
Last Updated version :
Sun Feb  5 11:02:55 2017
Number of code lines: 
61
"""
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import bokeh.plotting as bp
from matplotlib import style
import numpy as np
import random

#style.use('fivethirtyeight')
class gradientDescent():

    def __init__(self):
        self.x = np.linspace(-10,10,300)
        self.y = self.x**2 
        self.xdot = random.choice(self.x) 
        self.ydot = 0
        self.j = 0
        self.mins = []
        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1,1,1)

    def derivative(self,x):
        #test function = x^2
        return 2*x
    
    def GD(self):
        print('Initializing Gradient Descent')
        oldMin = 0
        currentMin = -7
        #precision
        epsilon = 0.001
        step = 0.01
        while abs(currentMin - oldMin) > epsilon:
            oldMin = currentMin
            gradient = self.derivative(oldMin)
            move = gradient * step
            currentMin = oldMin - move
            self.mins.append(currentMin)
        print('Local min : {:.2f}'.format(currentMin))

    def livePlot(self,i):
        style.use('fivethirtyeight')
        maxValue = len(self.mins) -1
        self.ax1.clear()
        self.ax1.set_ylim([-5,120])
        self.ax1.set_xlim([-20,20])
        #plt.axis('equal')
        self.ax1.plot(self.x,self.y,'c',self.mins[self.j],self.mins[self.j]**2,'ro')
        self.j+=1 
        if self.j == maxValue:
            self.j = 0


    def makeAnimation(self):
        a = animation.FuncAnimation(self.fig,self.livePlot,interval=10)
        plt.show()

            
gradient = gradientDescent() 
gradient.GD()
gradient.makeAnimation()
