#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 02:24:06 2017

@author: Ivan Luchko (luchko.ivan@gmail.com)

setup latticegraph_designer package in your environment
    
"""
import os
import sys
import pip
from setuptools import setup

#with open(os.path.abspath('README.rst'), encoding='utf-8') as f:
#    long_description = f.read()


long_description = '''
Matplotlib animation manager (GUI)
**********************************************

.. image:: https://img.shields.io/pypi/status/mpl-animationmanager.svg
        :target: https://pypi.python.org/pypi/mpl-animationmanager
        :alt: status

.. image:: https://img.shields.io/pypi/l/mpl-animationmanager.svg
        :target: https://github.com/luchko/mpl-animationmanager/blob/master/LICENSE.txt
        :alt: License

.. image:: https://readthedocs.org/projects/mpl-animationmanager/badge/?version=latest
        :target: http://mpl-animationmanager.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

It is a small convenient tool which allows to setup and save the gif/mp4-animations using the `PyQt <https://riverbankcomputing.com/software/pyqt/intro>`_ based GUI built on top of the `matplotlib animation module <http://matplotlib.org/api/animation_api.html>`_. Program can deal with both 2D and 3D animation. For 3D axes manager can add additional rotation of the view point resulting in both object modification and rotation animation. Also animation manager can be easily integrated in your larger PyQt project as a dialog. For more details see the Quitckstart section.

- Git-hub repo: https://github.com/luchko/mpl_animationmanager
- Documentation: https://mpl-animationmanager.readthedocs.io

Tool is compatible with Python 2.7 or Python 3.3+ and PyQt4 4.6+ or PyQt5 5.2+.

-------------------------

.. figure::  https://github.com/luchko/mpl_animationmanager/blob/master/img_src/demo.gif?raw=true
   :align:   center
   :figwidth: 100 %
   
-------------------------

Features
=========

- ``mpl_animationmanager`` library contains two classes ``AnimationManager`` and ``QDialogAnimManager`` with the same input arguments.
- ``QDialogAnimManager`` is inherited from the PyQt ``QDialog``. Using this class you can easily integrate animation manager as a QDialog into your larger PyQt application.
- ``AnimationManager`` is a small class build on top of the ``QDialogAnimManager`` and uses the input arguments to initialize the ``QDialogAnimManager`` object and run a PyQt application using ``run()`` function.
- After passing the required arguments to the manager, user can setup animation properties such as: dpi, fps (frames per second), modification period.
- For 3D animation user can also setup the rotation period, elevation and initilal azimut angles. The resulting duration of the animation equals the least common multiple of modification and rotaion periods if both are provided. 
- Animation can be saved in gif or mp4 format by picking one of the preinstalled movie writers used by matplotlib (imagemagick, ffmpeg etc.).
'''

# get list of dependencies from requirements.txt file
with open(os.path.abspath('requirements.txt')) as f:
    install_requires = [p for p in f.read().splitlines() if p != '']

pip.main(['install', 'matplotlib'])
## trick required to install numpy
#for package in install_requires:
#    pip.main(['install', package])

# define custom test runner 
from setuptools.command.test import test as TestCommand

class MyUnitTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
        
    def run_tests(self):
        from mpl_animationmanager.test import test_based_on_examples
        errcode = test_based_on_examples.main()
        sys.exit(errcode)

import mpl_animationmanager # need to be imported after matplotlib have been installed

setup(
    name='mpl_animationmanager',
    version=mpl_animationmanager.__version__,
    description='Matplotlib animation manager (GUI).',
    long_description=long_description,
    url='https://github.com/luchko/mpl_animationmanager',
    author='Ivan Luchko',
    author_email='luchko.ivan@gmail.com',
    documentation='https://mpl-animationmanager.readthedocs.io',
    license='MIT',
    packages=['mpl_animationmanager', 
              'mpl_animationmanager.examples',
              'mpl_animationmanager.test'],
    install_requires=install_requires,
    platforms='any',
    include_package_data=True,
    zip_safe=False,
    cmdclass = {'test': MyUnitTest},
    keywords='matplotlib animation animation-3d visualization gui gif pdf',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: Other Audience',
        'Topic :: Desktop Environment',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Widget Sets',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Presentation',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English'
        ]
)
