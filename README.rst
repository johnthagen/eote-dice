EotE Dice
=========

.. image:: https://badge.fury.io/py/eote-dice.png
    :target: http://badge.fury.io/py/eote-dice

Analyze or roll SW EotE role-playing game dice pools.

Installation
------------

*Note: Linux and Mac OSX users should use* ``pip3`` *rather than* ``pip``.

You can install, upgrade, and uninstall ``eote-dice`` with these commands:

.. code:: shell-session

    $ pip install eote-dice
    $ pip install --upgrade eote-dice
    $ pip uninstall eote-dice

Usage
-----

Input the dice pool using the first letter of the color of the die (except black Setback die which
use ``k``).  Use ``--roll`` to perform a roll or ``--analyze`` to statistically analyze.

.. code:: shell-session

    $ eote_dice --pool yygbrppk --analyze
    $ eote_dice --pool yygbrppk --roll


Releases
--------

0.3.0 - 2015-12-31
^^^^^^^^^^^^^^^^^^

Added rolling capability.


0.2.0 - 2015-12-31
^^^^^^^^^^^^^^^^^^

Dice statistics are now calculated using discrete distribution.  Contribution by @drhagen.

0.1.3 - 2015-12-25
^^^^^^^^^^^^^^^^^^

Fix pip install dependency issues.

0.1.2 - 2015-12-23
^^^^^^^^^^^^^^^^^^

Improve feedback when user enters an incorrect dice color.

0.1.1 - 2015-12-23
^^^^^^^^^^^^^^^^^^

Fixed setup.py.

0.1.0 - 2015-12-23
^^^^^^^^^^^^^^^^^^

First release.