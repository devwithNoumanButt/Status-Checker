Usage
=====

Installation
------------

Clone the repository:

.. code-block:: bash

   git clone https://github.com/devwithNoumanButt/Status-Checker.git

Enter the project directory:

.. code-block:: bash

   cd Status-Checker

Install dependencies:

.. code-block:: bash

   uv sync


Running the Application
-----------------------

Start the Streamlit application:

.. code-block:: bash

   uv run streamlit run app/app.py


Running Tests
-------------

Run the test suite with:

.. code-block:: bash

   uv run pytest

For verbose output:

.. code-block:: bash

   uv run pytest -v


Using the Python API
--------------------

The status checker can also be used directly from Python:

.. code-block:: python

   from status_checker.check_status import check_status

   status = check_status("https://example.com")

   print(status)


Return Values
-------------

The current implementation returns:

* ``200`` when the HTTP response status is ``200``.
* ``400`` for other HTTP responses.


How It Works
------------

The application follows these steps:

1. The user enters a URL.
2. Streamlit passes the URL to ``check_status``.
3. ``check_status`` sends an HTTP GET request.
4. The response status is checked.
5. HTTP ``200`` is considered successful.
6. Other responses are currently considered unsuccessful.