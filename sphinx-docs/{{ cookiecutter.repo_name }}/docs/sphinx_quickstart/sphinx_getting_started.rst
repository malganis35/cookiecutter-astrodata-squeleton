Sphinx Introduction
===========================

:Authors:
    Cao Tri DO <caotri.do@astraviz.fr>
:Version: 2026-02

Introduction to Sphinx
----------------------

Sphinx is a popular documentation generator for Python projects. It was originally created for documenting the Python software ecosystem, but it is now widely used for documenting other types of projects as well. Sphinx uses reStructuredText (RST) as its markup language, making it easy to write and maintain documentation.

One of the main advantages of Sphinx is its ability to automatically generate documentation from your source code. This means that you can keep your documentation and your code in sync, and any changes you make to your code will automatically be reflected in your documentation.

.. tip::
   To write easier in .rst format, we advice that you make your installation on VSCode. Within the team, we integrate an extension that facilitates the writing of.rst files for you with suggestion and autocompletion.

Examples of documentation
-------------------------

Many Python open sources project are based on Sphinx documentation. For example :

- Jupyter Notebook : https://docs.jupyter.org/en/latest/
- Flask : https://flask.palletsprojects.com/en/3.0.x/


Advantages of Sphinx
--------------------

- RST format allows to extend the Mardown syntax and to develop further advanced option
- Sphinx allows to easily convert RST format to HMTL format
- Sphinx compilated HTML can be easily deployed on Gitlab Pages, Github Pages for free as static website
- Using our Makefile command: ``make generate_docs``, Sphinx can automatically take all the docstrings of your function and add it automatically to your documentation
- You can easily compile the documentation into a PDF file

Installing Sphinx
------------------

To install Sphinx, you can use `pip`, the Python package manager. Simply run the following command in your terminal:

.. code-block::

    pip install sphinx

This will install Sphinx and all of its dependencies.

Creating a new project
------------------------

1. Using the sphinx-quickstart command
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create a new Sphinx project, you can use the `sphinx-quickstart` command. This command will guide you through the process of creating a new project, including setting up your project's basic structure and generating your project's configuration file.

Here's an example of how you can use `sphinx-quickstart` to create a new project:

.. code-block::

    sphinx-quickstart myproject

This will create a new project called `myproject` in the current directory. Once the project has been created, you can navigate into the project directory and run the `make html` command to generate your project's HTML documentation.

2. Using a squeleton: ``kdoc-make``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Follow the setup available on the Gitlab project page: (available soon)

Using our command ``kdoc-make``, This command will guide you through the process of creating a new project, including setting up your project's basic structure and generating your project's configuration file.

The difference here is that our Sphinx squeleton will have more advanced option and configuration that are automatically loaded when you start your project.

.. code-block::

    kdoc-make

Conclusion
----------

Sphinx is a powerful tool for creating and maintaining documentation. It is easy to learn, and its support for automatic documentation generation makes it an ideal choice for Python projects.
