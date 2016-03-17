EotE Dice
=========

.. image:: https://travis-ci.org/johnthagen/eote-dice.svg
    :target: https://travis-ci.org/johnthagen/eote-dice

.. image:: https://codeclimate.com/github/johnthagen/eote-dice/badges/gpa.svg
   :target: https://codeclimate.com/github/johnthagen/eote-dice

.. image:: https://codeclimate.com/github/johnthagen/eote-dice/badges/issue_count.svg
   :target: https://codeclimate.com/github/johnthagen/eote-dice

.. image:: https://codecov.io/github/johnthagen/eote-dice/coverage.svg
    :target: https://codecov.io/github/johnthagen/eote-dice

.. image:: https://img.shields.io/pypi/v/eote-dice.svg
    :target: https://pypi.python.org/pypi/eote-dice

.. image:: https://img.shields.io/pypi/status/eote-dice.svg
    :target: https://pypi.python.org/pypi/eote-dice

.. image:: https://img.shields.io/pypi/pyversions/eote-dice.svg
    :target: https://pypi.python.org/pypi/eote-dice/

.. image:: https://img.shields.io/pypi/dm/eote-dice.svg
    :target: https://pypi.python.org/pypi/eote-dice/

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
use ``k``).  Use ``--roll`` to perform a roll or ``analyze`` to statistically analyze.

.. code:: shell-session

    $ eote_dice --pool yygbrppk analyze --success-cutoff=1 --advantage-cutoff=2
    $ eote_dice --pool yygbrppk --roll


Releases
--------

1.0.0 - 2016-03-05
^^^^^^^^^^^^^^^^^^

Added four dimensional distribution to analyze dependant probabilities (e.g.
What is the probability of at least 1 success and 2 advantage?). Contributions by
@drhagen.

0.3.2 - 2015-12-31
^^^^^^^^^^^^^^^^^^

Fix bright black ANSI color difficult to read.

0.3.1 - 2015-12-31
^^^^^^^^^^^^^^^^^^

For rolls, use bright ANSI colors.

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