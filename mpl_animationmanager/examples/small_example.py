"""script runs small example of the animation manager usage"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_animationmanager import AnimationManager

def fAnim(j, ax, lineColl):
    '''define the modification animation function'''
    ax.collections = [] # clean axes
    ax.add_collection3d(lineColl[j]) # add new artist

# create figure        
fig = plt.figure('3D wireframe example')
ax = fig.gca(projection='3d')
ax.set_axis_off()

# generate modification frames (passed as fargs)
numFrames = 300     
X, Y, Z = axes3d.get_test_data(0.05)
for j in range(numFrames):
    ax.plot_wireframe(X, Y, Z*np.cos(2*np.pi/numFrames*j), rstride=5, cstride=5)
fargs = ax.collections
ax.collections = []
                    
# pass figure to animation manager
mng = AnimationManager(ax, fAnim, fargs, numFrames) 
mng.run()
