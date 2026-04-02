Get rid of "duplicate label" warning in Sphinx
==============================================

:Authors:
    Cao Tri DO <caotri.do@astraviz.fr>
:Version: 2026-02

source: https://stackoverflow.com/questions/62631362/get-rid-of-duplicate-label-warning-in-sphinx

sphinx.ext.autosectionlabel is producing these warnings. I had the same issue and managed to reduce the number of warnings by adding

.. code-block:: python

    suppress_warnings = ['autosectionlabel.*']
