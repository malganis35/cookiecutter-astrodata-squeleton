Sphinx Cheat Sheet
==================

:Authors:
    Cao Tri DO <caotri.do@astrodata.fr>
:Version: 2026-02

source: https://docs.typo3.org/m/typo3/docs-how-to-document/main/en-us/WritingReST/CheatSheet.html

Headlines
---------

Every reST (.rst) file should use these underlining styles. In reST, you can use different styles in any order you want. These are our conventions for TYPO3 documentation.

.. code::

    ========
    DocTitle
    ========

    Then use underlining only:

    ..  _header1:

    Header 1
    ========

    Header 1.1
    ----------

    Header 1.1.1
    ~~~~~~~~~~~~

    Header 1.1.1.1
    """"""""""""""

- line 1-3: This is the doc title. Every .rst file should have one.
- line 7: header label. This can be used for cross-referencing to this section:
   .. code::

        :ref:`header1`

- 9-10: Header level 1
- etc.

Links
-----

External links
^^^^^^^^^^^^^^

**method 1**:

.. code-block::

    `anchor text <URL>`__
    Check out more information on `t3o <https://typo3.org>`__.

(with one or two underscores at the end, if in doubt, use two)

**method 2** : "External Hyperlink Targets":

.. code-block::

    Check out more information on t3o_

    _t3o: https://typo3.org

This may be more convenient if you use a link several times.

Cross references
^^^^^^^^^^^^^^^^

When linking within docs.typo3.org, you should use this method of cross-referencing.

Use it to link to a section in this manual:

.. code-block::

    :ref:`intersphinx`

A section with the label intersphinx must exist! It is placed before the header:

.. code-block::

    ..  _intersphinx:

    Intersphinx
    ===========

Or, when cross-referencing to other manuals:

.. code-block::

    :ref:`shortcut:label`

When you are linking to another manual, make sure the shortcut (here: "h2document") is included in Settings: Documentation/Settings.cfg:

.. code-block::

    [intersphinx_mapping]

    h2document         = https://docs.typo3.org/m/typo3/docs-how-to-document/main/en-us/Index.html
    ...

We use the same conventions for naming the shortcuts in Settings.cfg, see Settings: Documentation/Settings.cfg. Not used manuals are commented out.

.. admonition::
   tips

   This is a cool feature, where reST & Sphinx shines: Even when a section is moved to another page (which effectively changes the URL), the link will still work!

Lists
-----


**How it looks:**

To create a bullet list:

- add a blank line before and after the list
- indent the list item text by 4 spaces - including the item sign
- to create a nested list:

  - indent the items by 4 spaces (left-align with parent item text)
  - apply rules of parent list (blank lines, item text indentation, ..)

Source:

.. code-block::

    To create a bullet list:

    * add a blank line before and after the list
    * indent the list item text by 4 spaces - including the item sign
    * to create a nested list:

        * indent the items by 4 spaces (left-align with parent item text)
        * apply rules of parent list (blank lines, item text indentation, ..)


Numbered lists
--------------

**How it looks:**

To create a numbered list:

#.  add a blank line before and after the list
#.  indent the list item text by 4 spaces - including the item sign
#.  to create a nested list:

    #. indent the items by 4 spaces (left-align with parent item text)
    #. apply rules of parent list (blank lines, item text indentation, ..)

More text.

.. code-block::

    To create a numbered list:

    #.  add a blank line before and after the list
    #.  indent the list item text by 4 spaces - including the item sign
    #.  to create a nested list:

        #. indent the items by 4 spaces (left-align with parent item text)
        #. apply rules of parent list (blank lines, item text indentation, ..)

    More text.


Code Blocks
-----------

Code block directive
^^^^^^^^^^^^^^^^^^^^


**How it looks:**

..  code-block:: php

    $a = 'hello';
    $b = 'something';

Source:

.. code-block::

    ..  code-block:: php

        $a = 'hello';
        $b = 'something';

This uses the directive "code-block" (line 1)

.. important::
   Make sure to indent correctly. The lines of the code-block (line 3+) must be indented (4 spaces).


Bold & italic
-------------

For inline code or for other semantic markup of special texts, use text roles.

**How it looks:**

Normal text, **bold text** and *italic text*.

.. code-block::

   Normal text, **bold text** and *italic text*.

Images
------


**How it looks:**

.. image:: sphinx_quickstart/a4.jpg
    :class: with-shadow

Source:

.. code-block::

    .. image:: sphinx_quickstart/a4.jpg
        :class: with-shadow

Another example

.. code-block::

    .. image:: sphinx_quickstart/a4.jpg
        :class: with-shadow
        :target: https://typo3.org
        :alt: alt text
        :width: 100px

YouTube videos
--------------

**How it looks:**

.. youtube:: wNxO-aXY5Yw
    :width: 640
    :height: 480
    :aspect: 4:3
    :align: center
    :url_parameters: ?start=43

Source:

.. code-block::

    .. youtube:: wNxO-aXY5Yw
        :width: 640
        :height: 480
        :aspect: 4:3
        :align: center
        :url_parameters: ?start=43

To be able to do it, you will have to install and setup the package:

.. code-block:: bash

   pip install sphinxcontrib-youtube

Add “sphinxcontrib.youtube” to the extensions list in conf.py. For example:

.. code-block:: python

    extensions = [
        'sphinx.ext.intersphinx',
        'sphinxcontrib.youtube'
    ]


Tips, hints, important (Admonitions)
------------------------------------

**How it looks:**

..  tip::

    To look at the reST source of this rendered page, scroll to the bottom
    and click on "View page source".

Source:

.. code-block::

    ..  tip::

        To look at the reST source of this rendered page, scroll to the bottom
        and click on "View page source".


Tab
-----


**How it looks:**

.. tab:: bash

    ..  code-block:: bash

        touch example-project-directory/public/FIRST_INSTALL

.. tab:: powershell

    ..  code-block:: powershell

        echo $null >> public/FIRST_INSTALL

Source:

.. code-block::

   .. tab:: bash

    ..  code-block:: bash

        touch example-project-directory/public/FIRST_INSTALL

    .. tab:: powershell

        ..  code-block:: powershell

            echo $null >> public/FIRST_INSTALL

HTML Embedding (iframe)
-----------------------

**How it looks:**

.. raw:: html

    <iframe title="Salaires Dev" width="800" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiMWZlZmYxNjItZWM5ZC00MWMxLTk4ZjctMjgxNTE0OWZlYTE5IiwidCI6IjkyNWViMjNjLTEwMGUtNGQ2MC1iYzg1LTg3MzY2MTRlYjdiMCJ9" frameborder="0" allowFullScreen="true"></iframe>

Source:

.. code-block::

    .. raw:: html

        <iframe title="Salaires Dev" width="800" height="600" src="https://app.powerbi.com/view?r=eyJrIjoiMWZlZmYxNjItZWM5ZC00MWMxLTk4ZjctMjgxNTE0OWZlYTE5IiwidCI6IjkyNWViMjNjLTEwMGUtNGQ2MC1iYzg1LTg3MzY2MTRlYjdiMCJ9" frameborder="0" allowFullScreen="true"></iframe>
