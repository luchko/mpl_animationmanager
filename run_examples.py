#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""script runs examples of animation manager usage"""

from mpl_animationmanager.examples import oscillation_2D 
from mpl_animationmanager.examples import rot_graph_3D 
from mpl_animationmanager.examples import modif_wireframe_3D 
from mpl_animationmanager.examples import modif_randwalk_3D 


def run_examples():
    """Main entry point for the script."""
    
#    oscillation_2D.run()
#    rot_graph_3D.run()
    modif_wireframe_3D.run()
#    modif_randwalk_3D.run()


if __name__ == '__main__':
    run_examples()
