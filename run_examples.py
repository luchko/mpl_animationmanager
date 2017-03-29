#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""script runs examples of animation manager usage"""

import examples.oscillation_2D 
import examples.rot_graph_3D
import examples.modif_wireframe_3D
import examples.modif_randwalk_3D


def run_examples():
    """Main entry point for the script."""
    
#    examples.oscillation_2D.run()
    examples.rot_graph_3D.run()
#    examples.modif_wireframe_3D.run()
#    examples.modif_randwalk_3D.run()


if __name__ == '__main__':
    run_examples()