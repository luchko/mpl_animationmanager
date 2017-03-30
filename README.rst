Matplotlib animation manager (GUI) 1.0a1
*********************************************

- Git-hub repo: https://github.com/Luchko/mpl_animation-manager
- Documentation: [Links to the project's ReadTheDocs page]
- Free software: MIT license

Build status
============

[A TravisCI button showing the state of the build]

[pyup.io button to deal with requirements]

Overview
========

It is a small convenient tool which allows to setup and save matplotlib animation using PyQt based GUI. Program can deal with both 2D and 3D animation. For 3D axes manager can add additional rotation of the view point resulting in both object modification and rotation animation. Also animation manager can be easily integrated in your larger PyQt project as a dialog. For more details see the Quitckstart section.

Program is compatible with Python 2.7 or Python 3.3+ and PyQt4 4.6+ or PyQt5 5.2+.

-------------------------

.. figure::  ./img_src/demo.gif
   :align:   center
   :figwidth: 100 %
   
-------------------------

Main features:
==============

- ``mpl_animationmanager`` library contains two classes ``AnimationManager`` and ``QDialogAnimManager`` with the same input arguments (see API LINK).
- ``QDialogAnimManager`` is inherited from the PyQt ``QDialog``. Using this class you can easily integrate animation manager as a QDialog into your larger PyQt application.
- ``AnimationManager`` is a small class build on top of the ``QDialogAnimManager`` and uses the input arguments to initialize the ``QDialogAnimManager`` object and run a PyQt application using ``run()`` function.
- After passing the required arguments to the manager, user can setup animation properties such as: dpi, fps (frames per second), modification period.
- For 3D animation user can also setup the rotation period, elevation and initilal azimut angles. The resulting duration of the animation equals the least common multiple of modification and rotaion periods if both are provided. 
- Animation can be saved in gif or mp4 format by picking one of the preinstalled movie writers used by matplotlib (imagemagick, ffmpeg etc.).
- Check a short demo video on YouTube. [LINK SHOULD BE HERE]

Quickstart
==========

Installation (cross-platform way from source)
---------------------------------------------

1. Download a source of the last stable package version [LINK]
2. Open the terminal.
3. Move to the package root directory.
4. In your command prompt type:

   .. code::

      python setup.py install

5. Thats it. Further, your can import the module into your python script by

   .. code:: python
   
      import mpl_animationmanager

Running from source
-------------------

It is possible to use animation manager without installing it.

1. Make sure that PyQt4 or PyQt5 package is installed.
2. Put the ``mpl_animationmanager`` source code folder into the root directiory of your script.
3. Now you can import ``mpl_animationmanager`` to your sript the same way as it would be installed.

You may want to do this for fixing bugs, adding new features, learning how the tool works or just getting a taste of it.

API
---

.. automodule:: mpl_animationmanager.mpl_animationmanager.QDialogAnimManager
    :members:
    :undoc-members:
    :show-inheritance:

Small example
--------------

Code below produces the same animation as one shown at the main demo above. 

.. literalinclude:: ./examples/small_example.py
    :linenos:
    :language: python
    :lines: 1, 3-5
    :start-after: 3
    :end-before: 5

More examples are included in ``./examples/`` folder.

Contacts:
=========

About the feature extension or bugs report you can create issue or feature request at [LINK] or feel free to contact me directly by e-mail:

	**Ivan Luchko** - luchko.ivan@gmail.com
