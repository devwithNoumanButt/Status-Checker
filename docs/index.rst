Status Checker Documentation
============================

Welcome to the Status Checker documentation!

Status Checker is a simple Python and Streamlit application
for checking the status of a website.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   src/check_status
   src/usage


Overview
--------

The application sends an HTTP GET request to a provided URL
and checks the HTTP response status.

Currently:

* HTTP 200 is considered **UP**.
* Other HTTP responses are considered **DOWN**.


Project Links
-------------

* GitHub: https://github.com/devwithNoumanButt/Status-Checker
* Live Demo: https://status-checker-tool.streamlit.app/