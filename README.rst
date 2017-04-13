Matplotlib animation manager (GUI) 1.0a1
****************************************

.. image:: https://img.shields.io/pypi/v/mpl-animationmanager.svg
        :target: https://pypi.python.org/pypi/mpl-animationmanager
        :alt: PyPi

.. image:: https://img.shields.io/pypi/status/mpl-animationmanager.svg
        :target: https://pypi.python.org/pypi/mpl-animationmanager
        :alt: status

.. image:: https://img.shields.io/pypi/l/mpl-animationmanager.svg
        :target: https://github.com/luchko/mpl-animationmanager/blob/master/LICENSE.txt
        :alt: License

.. image:: https://readthedocs.org/projects/mpl-animationmanager/badge/?version=latest
        :target: http://mpl-animationmanager.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://travis-ci.org/luchko/mpl_animationmanager.svg?branch=master
        :target: https://travis-ci.org/luchko/mpl_animationmanager
        :alt: travis-ci

.. image:: https://coveralls.io/repos/github/luchko/mpl_animationmanager/badge.svg?branch=master
	:target: https://coveralls.io/github/luchko/mpl_animationmanager?branch=master
        :alt: coveralls

- Git-hub repo: https://github.com/luchko/mpl_animationmanager
- Free software: MIT license

Overview
========

It is a small convenient tool which allows to setup and save `matplotlib animation <http://matplotlib.org/api/animation_api.html>`_ using the `PyQt <https://riverbankcomputing.com/software/pyqt/intro>`_ based GUI. Program can deal with both 2D and 3D animation. For 3D axes manager can add additional rotation of the view point resulting in both object modification and rotation animation. Also animation manager can be easily integrated in your larger PyQt project as a dialog. For more details see the Quitckstart section.

- Git-hub repo: https://github.com/luchko/mpl_animationmanager
- Documentation: https://mpl-animationmanager.readthedocs.io
- Free software: MIT license

Tool is based on PyQt and is compatible with Python 2.7 or Python 3.3+ and PyQt4 4.6+ or PyQt5 5.2+.

-------------------------

.. figure::  https://raw.githubusercontent.com/luchko/mpl_animationmanager/master/img_src/demo.gif
   :align:   center
   :figwidth: 100 %
   
-------------------------

Main features:
==============

- ``mpl_animationmanager`` library contains two classes ``AnimationManager`` and ``QDialogAnimManager`` with the same input arguments (`see API`_).
- ``QDialogAnimManager`` is inherited from the PyQt ``QDialog``. Using this class you can easily integrate animation manager as a QDialog into your larger PyQt application.
- ``AnimationManager`` is a small class build on top of the ``QDialogAnimManager`` and uses the input arguments to initialize the ``QDialogAnimManager`` object and run a PyQt application using ``run()`` function.
- After passing the required arguments to the manager, user can setup animation properties such as: dpi, fps (frames per second), modification period.
- For 3D animation user can also setup the rotation period, elevation and initilal azimut angles. The resulting duration of the animation equals the least common multiple of modification and rotaion periods if both are provided. 
- Animation can be saved in gif or mp4 format by picking one of the preinstalled movie writers used by matplotlib (imagemagick, ffmpeg etc.).

Quickstart
==========

Installation (cross-platform way from source)
---------------------------------------------

NOT IMPLEMENTED YET

Running from source
-------------------

It is possible to use animation manager without installing it.

1. Make sure that PyQt4 or PyQt5 package is installed.
2. `Download a source <https://github.com/luchko/mpl_animationmanager/archive/master.zip>`_ of the last stable package version.
3. Copy the ``./mpl_animationmanager/`` package folder into the root directiory of your script.
4. Now you can import ``mpl_animationmanager`` module to your sript the same way as it would have been installed.

You may want to do this for fixing bugs, adding new features, learning how the tool works or just getting a taste of it.

.. _`see API`:

API
---

Both ``AnimationManager`` and ``QDialogAnimManager`` classes take the same input arguments

.. code-block:: python

    class AnimationManager(object):    

        def __init__(self, ax, fAnim=None, fargs=None, numFramesModif=None, *args, **kwargs):
            '''
            Parameters
            ----------
            ax : 2D or 3D matplotlib axes object binded to the figure
                provides control over animated figure
            fAnim : function
                fAnim(i, ax, fargs) - modifies the "ax" at each "i" step
            fargs : any
                arguments used by the "fAnim" function during the "ax" modification
            numFramesModif : int
                number of modification frames
    
            '''          
        
Small example
--------------

Code below produces the same animation as one shown at the main demo above.

.. code-block:: python

    """script runs a small example of the animation manager usage"""
    
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
                        
    # pass figure to the animation manager
    mng = AnimationManager(ax, fAnim, fargs, numFrames) 
    mng.run()
    
More examples are included in ``./mpl_animationmanager/examples/`` folder.

Contacts:
=========

About the feature extension or bugs report you can create `the issue or feature request <https://github.com/luchko/mpl_animationmanager/issues>`_ or feel free to contact me directly by e-mail:

	**Ivan Luchko** - luchko.ivan@gmail.com
