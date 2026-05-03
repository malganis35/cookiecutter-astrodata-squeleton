Adding Google Analytics to Sphinx
=================================

:Authors:
    Cao Tri DO <caotri.do@astrodata.fr>
:Version: 2026-02

source: https://dailystuff.nl/blog/2023/adding-google-analytics-in-sphinx

Creating and maintaining a website is a lot of work and it is nice to know which pages are being visited and how people are finding your site. Google Analytics is a great tool for this and it is easy to add to your Sphinx site. But adding it to your Sphinx Sphinx blog is not as easy as it could be. This post will show you how to add Google Analytics to your Sphinx site instead of modifiying the theme or template files.

Preparing your site
-------------------

The first step is to create a Google Analytics account and get your tracking ID. This is a long string that looks like ``G-XXXXXXXXX``. You can find it in the admin section of your Google Analytics account.

.. note::
    If you are using Google Analytics 4, you will need to use the ``G-XXXXXXXXX`` format. If you are using Universal Analytics, you will need to use the ``UA-XXXXXXXXX`` format.

The next step is to install the ``sphinxcontrib-googleanalytics`` package (https://github.com/sphinx-contrib/googleanalytics).
This is a Sphinx extension that will add the Google Analytics tracking code to your site. You can install it with ``pip`` or add it to your ``requirements.txt`` file.

Adding the sphinxcontrib-googleanalytics package to ``docs/requirements.txt``

.. code-block:: bash

    sphinxcontrib-googleanalytics==0.4

Enabling the extension
----------------------

Now that you have the extension installed, you need to enable it in your Sphinx configuration file. You can do this by adding ``sphinxcontrib.googleanalytics`` to the extensions list and setting the ``googleanalytics_id`` variable to your tracking ID.

Example configuration file ``docs/conf.py``

.. code-block:: bash

    extensions = [
                    'sphinxcontrib.googleanalytics',
                ]

    googleanalytics_id = 'G-XXXXXXXXX'

After you have added the extension and set the tracking ID, you can build your site and the tracking code will be added to the pages. You can verify this by looking at the source of your pages and searching for the tracking ID.


Enabling the extension only when building on GitHub Actions
-----------------------------------------------------------

The extension will add the tracking code to your pages when you build your site locally. But you probably don’t want to track your local builds. You can use the ``os.getenv`` function to only enable the extension when you are building on GitHub Actions.

Example configuration file ``docs/conf.py``

.. code-block:: bash

    import os

    if os.getenv("GITHUB_ACTIONS"):
        extensions.append("sphinxcontrib.googleanalytics")
        googleanalytics_id = "G-XXXXXXXXX"

Now the extension will only be enabled when you build your site on GitHub Actions. You can verify this by looking at the source of your pages and searching for the tracking ID.

The example below shows how to enable the extension when building on GitHub Actions, Travis CI, CircleCI, or GitLab CI.

Example configuration file ``docs/conf.py``

.. code-block:: bash

    import os

    if os.getenv("GITHUB_ACTIONS") or os.getenv("TRAVIS") or os.getenv("CIRCLECI") or os.getenv("GITLAB_CI"):
        extensions.append("sphinxcontrib.googleanalytics")
        googleanalytics_id = "G-XXXXXXXXX"
