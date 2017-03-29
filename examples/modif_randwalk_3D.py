#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:05:42 2017

@author: Ivan Luchko (luchko.ivan@gmail.com)

Random walk: matplotlib animation manager usage example        
"""    
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d    
from mpl_animationmanager import AnimationManager


def Gen_RandLine(length, step_max, dims=2):
    """Create a line using a random walk algorithm """
    
    lineData = np.empty((dims, length))
    lineData[:, 0] = np.random.rand(dims)
    for index in range(1, length):
        step = ((np.random.rand(dims) - 0.5)*step_max)
        lineData[:, index] = lineData[:, index - 1] + step
    return lineData        


def update_lines(num, ax, fargs):
    """define modification animation function"""
    
    dataLines, lines = fargs
    for line, data in zip(lines, dataLines):
        # NOTE: there is no .set_data() for 3 dim data...
        line.set_data(data[0:2, :num])
        line.set_3d_properties(data[2, :num])
    return lines


def run():
    """
    return animation manager dialog
    
    example idea borrowed from: 
        http://matplotlib.org/examples/animation/simple_3danim.html
    """         
    NUM_LINES = 50
    NUM_STEPS = 1000
    STEP_MAX = 0.1

    fig = plt.figure('Random walk example')
    ax = fig.gca(projection='3d')
    ax.set_axis_off()
    # Setting the axes properties
    d = 1
    ax.set_xlim3d([0.0 - d, 1.0 + d])
    ax.set_ylim3d([0.0 - d, 1.0 + d])
    ax.set_zlim3d([0.0 - d, 1.0 + d])
    
    # generating random data and 3-D lines
    data = [Gen_RandLine(NUM_STEPS, STEP_MAX, dims=3) for index in range(NUM_LINES)]    
    lines = [ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in data]
    
    # pass figure to animation manager
    mng = AnimationManager(ax, fAnim=update_lines, fargs=(data, lines), 
                           numFramesModif=NUM_STEPS)
    # set some initial parameters
    mng.dlg.spinBox_period_modif.setValue(30)
    
    return mng.run()
    

if __name__ == '__main__':
    sys.exit(run())