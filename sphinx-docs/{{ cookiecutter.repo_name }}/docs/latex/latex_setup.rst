===================
LaTeX Setup
===================

:Authors:
    Cao Tri DO <caotri.do@astraviz.fr>
:Version: 2026-02

LaTeX is a powerful typesetting system that is widely used for creating scientific and technical documents. It is particularly well-suited for documents that contain complex mathematical equations, tables, and figures. In this section, we will provide an introduction to LaTeX and how to set it up for your documentation projects.

Installing LaTeX
================
To install LaTeX, you can use a distribution such as TeX Live (for Windows, macOS, and Linux) or MiKTeX (for Windows). These distributions include all the necessary tools and packages to create LaTeX documents.

- For TeX Live, you can download it from https://www.tug.org/texlive/
- For MiKTeX, you can download it from https://miktex.org/download
- For macOS users, you can also use MacTeX, which is a TeX Live distribution specifically for macOS: https://tug.org/mactex/
- For Linux users, you can typically install TeX Live using your package manager. For example, on Debian-based systems, you can use the following command:

.. code-block:: bash
    
    sudo apt update
    sudo apt-get install texlive-full

Once you have installed LaTeX, you can verify the installation by running the following command in your terminal:

.. code-block:: bash
    
    latex --version

This should display the version of LaTeX that you have installed.

Setup LaTeX for VSCode
========================

LaTeX Workshop
--------------

To set up LaTeX for VSCode, you can install the "LaTeX Workshop" extension. This extension provides a rich set of features for working with LaTeX documents, including

- Syntax highlighting
- Code snippets
- PDF preview
- Build tools
- And much more!

To install the "LaTeX Workshop" extension, follow these steps:

1. Open VSCode and go to the Extensions view by clicking on the Extensions icon in the Activity Bar on the side of the window or by pressing `Ctrl+Shift+X`.
2. In the search bar, type "LaTeX Workshop" and press Enter.
3. Click on
4. the "Install" button to install the extension.
5. Once the extension is installed, you can create a new LaTeX document by creating a new file with the `.tex` extension. The extension will automatically provide you with features such as syntax highlighting and code snippets to help you write your LaTeX document more efficiently.

To build your LaTeX document and generate a PDF, you can use the "Build LaTeX project" command provided by the extension. You can access this command by pressing `Ctrl+Shift+B` or by clicking on the "Build LaTeX project" button in the status bar at the bottom of the VSCode window.

After building your document, you can preview the generated PDF by clicking on the "View LaTeX PDF" button in the status bar or by using the "View LaTeX PDF" command.

The "LaTeX Workshop" extension also provides many other features, such as support for bibliographies, code folding, and more. You can explore the extension's documentation for more information on how to use these features effectively.

With LaTeX set up in VSCode, you can now create and manage your LaTeX documents with ease, making it a great choice for writing scientific and technical documentation.

LaTeX language support
----------------------

Install LaTex language support for VSCode to get syntax highlighting, code snippets, and other features that will make writing LaTeX documents easier. You can find the "LaTeX Workshop" extension in the VSCode marketplace, which provides comprehensive support for LaTeX development.

Overleaf Workshop
-----------------

Overleaf is an online LaTeX editor that allows you to write, edit, and collaborate on LaTeX documents in your web browser. It provides a rich set of features for working with LaTeX, including real-time collaboration, version control, and a wide range of templates.
To get started with Overleaf, you can create a free account at https://www.overleaf.com/. Once you have an account, you can create a new project and start writing your LaTeX document. Overleaf provides a user-friendly interface that allows you to easily manage your LaTeX files and compile your document to see the output in real-time.
Overleaf also supports collaboration, allowing you to invite others to work on your LaTeX document with you. You can share your project with collaborators and work together in real-time, making it a great choice for team projects or when you need to collaborate with others on a LaTeX document.
With Overleaf, you can also take advantage of a wide range of templates for different types of documents, such as academic papers, presentations, and more. This can help you get started quickly and ensure that your document is formatted correctly.
Overall, Overleaf is a powerful online LaTeX editor that provides a convenient and collaborative environment for writing LaTeX documents, making it a great choice for both beginners and experienced LaTeX users.

To install Overleaf in VSCode, you can use the "Overleaf Workshop" extension. This extension allows you to connect your Overleaf account to VSCode and work on your LaTeX documents directly from the editor. You can find the "Overleaf Workshop" extension in the VSCode marketplace and follow the installation instructions provided by the extension to set it up. Once installed, you can easily sync your Overleaf projects with VSCode and take advantage of the features provided by both platforms for a seamless LaTeX writing experience.
