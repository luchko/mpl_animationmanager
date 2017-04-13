#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Unittest of the Matplotlib animation manager basic functionality

Unittests is strongly binded with the example moudules and AnimationManager 
class itself which support TestCase running. 

Unittest should be run by passing the TestCase to manager instance (mng) 
via the nmg.runUnitTest(MyTestCase) method. 

TestCase gets access to the figure axes and the manager dialog during 
the TestCase instance creationg via __init__ method.
"""

__author__ = "Ivan Luchko (luchko.ivan@gmail.com)"
__version__ = "1.0a1"
__date__ = "Apr 4, 2017"
__copyright__ = "Copyright (c) 2017, Ivan Luchko and Project Contributors "

import os
import time
import unittest

from mpl_animationmanager.examples import oscillation_2D 
from mpl_animationmanager.examples import rot_graph_3D 
from mpl_animationmanager.examples import modif_wireframe_3D 
from mpl_animationmanager.examples import modif_randwalk_3D 
 
test_folder = "./mpl_animationmanager/test/"

DELAY = 0.2 # [sec] delay for signal processing in the main loop

def isRotated(ax, dlg):
    '''
    returns True if 3D axes is rotated
    
    this function should be executed in separate thread
    '''
    azim0 = ax.azim
    # wait some time until 3D axes are rotated in main thread 
    time.sleep(1.01/dlg.fps)
    
    return azim0 != ax.azim

class modif_oscillation_2D_Test(unittest.TestCase):
    '''Animation manager test based on the '2D oscillation' example'''

    def __init__(self, testname, ax, dlg):
        
        unittest.TestCase.__init__(self, testname)
        
        self.ax, self.dlg = ax, dlg
        self.fig = self.ax.get_figure()
            
    def test_initialization(self):
        '''
        test widgets comonent according to type of figure and animation
            - 2D/3D axes
            - object modification present
        '''
        # curent example has modification
        self.assertTrue(self.dlg.widget_modif.isVisible())
        self.assertTrue(self.dlg.checkBox_modif.isChecked())
        
        # curent example are axes 2D, thus object can be rotated 
        self.assertTrue(not self.dlg.widget_rot.isVisible())
        self.assertTrue(not self.dlg.checkBox_rot.isChecked())        
        
        self.assertAlmostEqual(self.dlg.period, self.dlg.period_modif)
        
    def test_quality_props(self):
                
        # change dpi
        dpi = 50
        self.dlg.spinBox_dpi.setValue(dpi)
        time.sleep(DELAY) # wait for signal handling in the main event loop
        self.assertEqual(self.dlg.dpi, dpi)
        self.assertEqual(self.fig.get_dpi(), dpi)
        
        # change fps
        fps = 10
        self.dlg.spinBox_fps.setValue(fps)
        time.sleep(DELAY) # wait for signal handling in the main event loop
        self.assertEqual(self.dlg.fps, fps)
        
        # restore defaults:
        self.dlg.spinBox_dpi.setValue(100)
        self.dlg.spinBox_fps.setValue(24)
        time.sleep(3*DELAY) # wait for signal handling in the main event loop

    def test_modif_props(self):

        # change rotation period
        t = 30
        self.dlg.spinBox_period_modif.setValue(t)
        time.sleep(DELAY) # wait for signal handling in the main event loop
        self.assertEqual(self.dlg.period_modif, t)     
        self.assertEqual(self.dlg.period, t)     

    def test_control_btns(self):
        
        # test pause button
        self.dlg.btnPause.click()
        time.sleep(2*DELAY) # wait for signal handling in the main event loop

        # test start button
        self.dlg.btnStart.click()
        time.sleep(2*DELAY) # wait for signal handling in the main event loop

        # test stop button
        self.dlg.btnStop.click()
        time.sleep(2*DELAY) # wait for signal handling in the main event loop
        
        # test start button
        self.dlg.btnStart.click()
        time.sleep(2*DELAY) # wait for signal handling in the main event loop

    def test_exportAnim(self):
        
        # make the animation small for faster export
        self.dlg.spinBox_dpi.setValue(30)
        self.dlg.spinBox_fps.setValue(10)
        self.dlg.spinBox_period_modif.setValue(2)
        time.sleep(3*DELAY) # wait for signal handling in the main event loop
        
        # export animation
        path = os.path.abspath(test_folder+"test")
        self.dlg.lineEdit_name.setText(path)
        self.dlg.EXPORT_RUNNING = True
        self.dlg.btnExport.click()
        # wait until exporting is finished
        while self.dlg.EXPORT_RUNNING: time.sleep(2*DELAY)
        self.assertTrue(os.path.exists(self.dlg.filepath))
        # remove testfile
        os.remove(self.dlg.filepath)

        # restore default settings
        self.dlg.btnStart.click()
        time.sleep(2*DELAY) # wait for signal handling in the main event loop
        # make the animation small for faster export
        self.dlg.spinBox_dpi.setValue(100)
        self.dlg.spinBox_fps.setValue(24)
        self.dlg.spinBox_period_modif.setValue(10)
        time.sleep(3*DELAY) # wait for signal handling in the main event loop


class rot_graph_3D_Test(unittest.TestCase):
    '''Animation manager test based on the '3D rotated graph' example'''

    def __init__(self, testname, ax, dlg):
        
        unittest.TestCase.__init__(self, testname)
        
        self.ax, self.dlg = ax, dlg
        self.fig = self.ax.get_figure()
            
    def test_initialization(self):
        '''
        test widgets comonent according to type of figure and animation
            - 2D/3D axes
            - object modification present
        '''
        # curent example has no modification
        self.assertTrue(not self.dlg.widget_modif.isVisible())
        self.assertTrue(not self.dlg.checkBox_modif.isChecked())
        
        # curent example are axes 3D, thus object can be rotated 
        self.assertTrue(self.dlg.widget_rot.isVisible())
        self.assertTrue(self.dlg.checkBox_rot.isChecked())        
        
        self.assertAlmostEqual(self.dlg.period, self.dlg.period_rot)
        
    def test_quality_props(self):
                
        # change dpi
        dpi = 50
        self.dlg.spinBox_dpi.setValue(dpi)
        time.sleep(DELAY) # wait for signal handling in the main event loop
        self.assertEqual(self.dlg.dpi, dpi)
        self.assertEqual(self.fig.get_dpi(), dpi)
        
        # change fps
        fps = 10
        self.dlg.spinBox_fps.setValue(fps)
        time.sleep(DELAY) # wait for signal handling in the main event loop
        self.assertEqual(self.dlg.fps, fps)
        
        # restore defaults:
        self.dlg.spinBox_dpi.setValue(100)
        self.dlg.spinBox_fps.setValue(24)
        time.sleep(3*DELAY) # wait for signal handling in the main event loop

    def test_3D_props(self):

        # change rotation period
        t = 30
        self.dlg.spinBox_period_rot.setValue(t)
        time.sleep(DELAY) # wait for signal handling in the main event loop
        self.assertEqual(self.dlg.period_rot, t)     
        self.assertEqual(self.dlg.period, t)     

        # change elevation
        elev = 10
        self.dlg.spinBox_elev.setValue(elev)
        time.sleep(DELAY) # wait for signal handling in the main event loop
        self.assertEqual(self.dlg.elevation, elev)
        self.assertEqual(self.ax.elev, elev)
        
        # enable/diable rotation
        self.dlg.checkBox_rot.setChecked(False)
        time.sleep(3*DELAY) # wait for signal handling in the main event loop
        self.assertTrue(not isRotated(self.ax, self.dlg))
        self.dlg.checkBox_rot.setChecked(True)
        time.sleep(3*DELAY) # wait for signal handling in the main event loop
        self.assertTrue(isRotated(self.ax, self.dlg))
        
        # change initial azimut
        azim = -50
        self.dlg.btnStop.click()
        time.sleep(DELAY) # wait for signal handling in the main event loop
        self.dlg.spinBox_azim.setValue(azim)
        time.sleep(DELAY) # wait for signal handling in the main event loop
        self.assertEqual(self.dlg.zero_azim, azim)
        self.assertEqual(self.ax.azim, azim)

    def test_control_btns(self):
        
        # test pause button
        self.dlg.btnPause.click()
        time.sleep(2*DELAY) # wait for signal handling in the main event loop
        self.assertTrue(not isRotated(self.ax, self.dlg))

        # test start button
        self.dlg.btnStart.click()
        time.sleep(2*DELAY) # wait for signal handling in the main event loop
        self.assertTrue(isRotated(self.ax, self.dlg))

        # test stop button
        self.assertNotEqual(self.ax.azim, self.dlg.spinBox_azim.value())
        self.dlg.btnStop.click()
        time.sleep(2*DELAY) # wait for signal handling in the main event loop
        self.assertTrue(not isRotated(self.ax, self.dlg))
        self.assertEqual(self.ax.azim, self.dlg.spinBox_azim.value())
        
        # test start button
        self.dlg.btnStart.click()
        time.sleep(2*DELAY) # wait for signal handling in the main event loop
        self.assertTrue(isRotated(self.ax, self.dlg))

    def test_exportAnim(self):
        
        # make the animation small for faster export
        self.dlg.spinBox_dpi.setValue(30)
        self.dlg.spinBox_fps.setValue(10)
        self.dlg.spinBox_period_rot.setValue(2)
        time.sleep(3*DELAY) # wait for signal handling in the main event loop
        
        # export animation
        path = os.path.abspath(test_folder+"test")
        self.dlg.lineEdit_name.setText(path)
        self.dlg.EXPORT_RUNNING = True
        self.dlg.btnExport.click()
        # wait until exporting is finished
        while self.dlg.EXPORT_RUNNING: time.sleep(2*DELAY)
        self.assertTrue(os.path.exists(self.dlg.filepath))
        # remove testfile
        os.remove(self.dlg.filepath)

        # restore default settings
        self.dlg.btnStart.click()
        time.sleep(2*DELAY) # wait for signal handling in the main event loop
        self.assertTrue(isRotated(self.ax, self.dlg))
        # make the animation small for faster export
        self.dlg.spinBox_dpi.setValue(100)
        self.dlg.spinBox_fps.setValue(24)
        self.dlg.spinBox_period_rot.setValue(10)
        time.sleep(3*DELAY) # wait for signal handling in the main event loop


    tests_require=['pytest'],
    test_suite='sandman.test.test_sandman',


def main():
    '''run test suits and return the error code'''
    
    TestExamples_list = [(oscillation_2D, modif_oscillation_2D_Test), 
                         (rot_graph_3D, rot_graph_3D_Test)]
    
    WAS_SUCCESSFUL = True
    
    for example, exampleTestCase in TestExamples_list:
        mng = example.get_animManager()
        result = mng.runUnitTest(MyTestCase=exampleTestCase) #TestResult instance
        
        WAS_SUCCESSFUL = WAS_SUCCESSFUL and result.wasSuccessful()
    
    return not WAS_SUCCESSFUL
    
    
if __name__ == "__main__":
    
    main()