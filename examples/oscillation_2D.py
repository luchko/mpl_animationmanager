#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:05:42 2017

@author: Ivan Luchko (luchko.ivan@gmail.com)

2D oscillation: matplotlib animation manager usage example        
"""    
import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_animationmanager import AnimationManager


def fAnim(i, ax, fargs):
    '''define modification animation function'''
    line, tdata, ydata = fargs
    line.set_data(tdata[:i], ydata[:i])


def run():
    """return animation manager dialog"""
                    
    NUM_STEPS = 400
    STEP = 0.05

    fig = plt.figure('2D oscillation example') 
    ax = fig.gca()
    ax.set_ylim(-1.1, 1.1)
    ax.set_xlim(0, STEP*NUM_STEPS)
    ax.grid()
    
    line, = ax.plot([], [], lw=2)
    tdata = [STEP*i for i in range(NUM_STEPS)]
    ydata = [np.sin(2*np.pi*t) * np.exp(-t/5.) for t in tdata]
        
    # pass figure to animation manager
    mng = AnimationManager(ax, fAnim=fAnim, fargs=(line, tdata, ydata), 
                           numFramesModif=NUM_STEPS)
    # set some initial parameters
    mng.dlg.spinBox_period_modif.setValue(10)

    return mng.run()
    

if __name__ == '__main__':
    sys.exit(run())