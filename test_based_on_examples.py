#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Unittest of the Matplotlib animation manager basic functionality"""

from __future__ import division

__author__ = "Ivan Luchko (luchko.ivan@gmail.com)"
__version__ = "1.0a1"
__date__ = "Apr 4, 2017"
__copyright__ = "Copyright (c) 2017, Ivan Luchko and Project Contributors "

import os
import unittest
import time

from mpl_animationmanager.examples import oscillation_2D 
from mpl_animationmanager.examples import rot_graph_3D 
from mpl_animationmanager.examples import modif_wireframe_3D 
from mpl_animationmanager.examples import modif_randwalk_3D 

from PyQt5.QtCore import QTimer
 
test_folder = "./mpl_animationmanager/test/"


def isRotated(ax, dlg):
    '''returns True is 3D axes is rotated'''
        
    azim0 = ax.azim
    time.sleep(1.01/dlg.fps)
    return azim0 != ax.azim


class rot_graph_3D_Test(unittest.TestCase):
    '''Animation manager test based on the '3D rotated graph' example'''

    def __init__(self, testname, ax, dlg):
        
        unittest.TestCase.__init__(self, testname)
        
        self.ax, self.dlg = ax, dlg
    
#    def setUp(self):
#        '''Run example and get the control over axes and manager dialog'''
#        
#        self.ax, self.dlg = rot_graph_3D.run()
        
#    def tearDown(self):
#        '''close the manager dialog and stop running the example'''
#        
#        self.dlg.btnClose.click()
        

    def test_control_btns(self):
        
#        self.setUp()

        # object is rotated after opening the manager
        time.sleep(0.1) # sleep 0.1s for slots handling
        self.assertTrue(isRotated(self.ax, self.dlg))

        # test pause button
        self.dlg.btnPause.click()
        time.sleep(0.1) # sleep 0.1s for slots handling
        self.assertTrue(not isRotated(self.ax, self.dlg))

        # test start button
        self.dlg.btnStart.click()
        time.sleep(0.1) # sleep 0.1s for slots handling
        self.assertTrue(isRotated(self.ax, self.dlg))

        # test stop button
        self.assertNotEqual(self.ax.azim, self.dlg.spinBox_azim.value())
        self.dlg.btnStop.click()
        time.sleep(0.1) # sleep 0.1s for slots handling
        self.assertTrue(not isRotated(self.ax, self.dlg))
        self.assertEqual(self.ax.azim, self.dlg.spinBox_azim.value())

        
#    def test_AnimManager(self):
#        
##        self.setUp()
#        
#        # change dpi
#        self.dlg.spinBox_dpi.setValue(50)
#        self.assertEqual(self.dlg.dpi, 50)
#        # change fps
#        self.dlg.spinBox_fps.setValue(10)
#        self.assertEqual(self.dlg.fps, 10)
#
#        # change elevation
#        self.dlg.spinBox_elev.setValue(10)
#        self.assertEqual(self.dlg.elevation, 10)
#        # change rotation period
#        self.dlg.spinBox_period_rot.setValue(30)
#        self.assertEqual(self.dlg.period_rot, 30)        
#        self.dlg.spinBox_period_rot.setValue(3)
#        self.assertEqual(self.dlg.period_rot, 3)                
#        
#        # stop
#        self.dlg.btnStop.click()
#        # change initial azimut
#        self.dlg.spinBox_azim.setValue(-50)
#        self.assertEqual(self.dlg.zero_azim, -50)
#
#        # export animation
#        path = os.path.abspath(test_folder+"test")
#        self.dlg.lineEdit_name.setText(path)
#        self.dlg.btnExport.click()
#        self.assertTrue(os.path.exists(test_folder+"test.gif")
#                        or os.path.exists(test_folder+"test.mp4"))


if __name__ == "__main__":
    
    mng = rot_graph_3D.get_animManager()
    mng.runUnitTest(MyTestCase=rot_graph_3D_Test)

#    unittest.main()