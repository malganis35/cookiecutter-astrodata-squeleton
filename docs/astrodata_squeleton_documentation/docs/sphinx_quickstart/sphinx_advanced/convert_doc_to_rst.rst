Convert a Word File to reStructuredText with Pandoc
==========================================================

:Authors:
    Cao Tri DO <caotri.do@astrodata.fr>
:Version: 2026-02

To convert a Word file (.docx) to a reStructuredText (.rst) file with Pandoc, follow these steps:

1. **Install Pandoc**: If you don't have it already, you need to install Pandoc. You can download it from the `official Pandoc site <https://pandoc.org/installing.html>`_ and follow the instructions for your operating system (Windows, macOS, Linux).

2. **Use the Command Line**: Once Pandoc is installed, you can use the command line to convert your file. Open a terminal (or command prompt on Windows) and use the following command:

   .. code-block:: sh

      pandoc -o output_file.rst input_file.docx

   Replace ``input_file.docx`` with the path to your Word file and ``output_file.rst`` with the desired name for your output reStructuredText file.

Example
-------

Suppose you have a Word file named ``document.docx`` and you want to convert it to ``document.rst``. Here is the command you would use:

.. code-block:: sh

   pandoc -o document.rst document.docx

Additional Options
------------------

Pandoc offers many options to customize the conversion. For example, you can specify metadata, adjust formatting, and more. Here are some useful options:

- ``--standalone`` (or ``-s``): Create a complete document (including necessary headers).
- ``--toc``: Add a table of contents.
- ``--extract-media``: Extract embedded images from the Word document into a specified directory.

Example with Options
--------------------

If you want to extract images into a directory named ``media`` and add a table of contents, you would use:

.. code-block:: sh

   pandoc -s --toc --extract-media=media -o document.rst document.docx

Verify Pandoc Installation
--------------------------

To check that Pandoc is correctly installed, you can run the following command in your terminal:

.. code-block:: sh

   pandoc --version

This should display the installed version of Pandoc along with other information.

By following these steps, you should be able to easily convert a Word file to a reStructuredText file using Pandoc.
