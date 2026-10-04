# Status Checker

[![Documentation Status](https://readthedocs.org/projects/status-checker/badge/?version=latest)](https://status-checker.readthedocs.io/en/latest/)
[![Python](https://img.shields.io/badge/Python-3.14%2B-blue.svg)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

A simple Python and Streamlit application for checking the status of a website.

Status Checker sends an HTTP request to a user-provided URL and determines whether the website is reachable based on its HTTP response status.

---

## 🚀 Live Demo

Try the application online:

**https://status-checker-tool.streamlit.app/**

---

## 📚 Documentation

Full project documentation is available on Read the Docs:

**https://status-checker.readthedocs.io/en/latest/**

The documentation includes:

- Project overview
- Installation instructions
- Usage instructions
- Python API reference
- Development information

---

## ✨ Features

- 🌐 Check the status of a website using its URL
- 🖥️ Simple Streamlit web interface
- 🐍 Reusable Python API
- 🧪 Automated tests with pytest
- 📖 Sphinx documentation
- 📚 Read the Docs integration
- 📦 Modern Python packaging
- ⚡ Dependency management with `uv`

---

## 🛠️ Technologies

This project is built using:

| Technology    | Purpose                                  |
| ------------- | ---------------------------------------- |
| Python        | Main programming language                |
| Requests      | HTTP requests                            |
| Streamlit     | Web interface                            |
| pytest        | Automated testing                        |
| Sphinx        | Documentation                            |
| Read the Docs | Documentation hosting                    |
| uv            | Python package and dependency management |

---

## 📁 Project Structure

```text
Status-Checker/
│
├── app/
│   └── app.py
│
├── src/
│   └── status_checker/
│       ├── __init__.py
│       └── check_status.py
│
├── tests/
│   ├── __init__.py
│   └── test_check_status.py
│
├── docs/
│   ├── source/
│   │   ├── _static/
│   │   ├── api.rst
│   │   ├── conf.py
│   │   ├── index.rst
│   │   └── usage.rst
│   │
│   └── requirements.txt
│
├── .readthedocs.yaml
├── README.md
├── pyproject.toml
└── uv.lock
```

### Directory Overview

#### `app/`

Contains the Streamlit application.

```text
app/app.py
```

This provides the user interface where a URL can be entered and checked.

#### `src/status_checker/`

Contains the main Python package and status-checking logic.

```text
src/status_checker/check_status.py
```

This module performs the HTTP request and evaluates the response.

#### `tests/`

Contains automated tests for the project.

```text
tests/test_check_status.py
```

The tests verify the behavior of the status-checking function without making real requests to external websites.

#### `docs/`

Contains the Sphinx documentation source files.

---

# 📦 Installation

## Requirements

Before installing the project, make sure you have:

- Python 3.14 or newer
- Git
- `uv`

You can check your Python version with:

```bash
python3 --version
```

Check `uv` with:

```bash
uv --version
```

---

## Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/devwithNoumanButt/Status-Checker.git
```

Move into the project directory:

```bash
cd Status-Checker
```

---

## Install Dependencies

This project uses `uv` for dependency management.

Run:

```bash
uv sync
```

This creates/updates the project's virtual environment and installs the required dependencies.

---

# ▶️ Running the Application

Start the Streamlit application with:

```bash
uv run streamlit run app/app.py
```

Streamlit will display a local URL in the terminal.

Open the URL in your browser.

You will see the Status Checker interface where you can enter a website URL.

For example:

```text
https://example.com
```

The application will check the website and display the result.

---

# 🔍 How It Works

The application follows a simple workflow:

```text
                    User
                     │
                     ▼
             Enter website URL
                     │
                     ▼
             Streamlit interface
                     │
                     ▼
              check_status()
                     │
                     ▼
              HTTP GET request
                     │
                     ▼
             Check HTTP status
                 ┌───┴───┐
                 │       │
                200    Other
                 │       │
                 ▼       ▼
               UP      DOWN
```

The status-checking function sends an HTTP GET request to the supplied URL.

The current implementation considers:

```text
HTTP 200 → Website is UP
Other     → Website is DOWN
```

---

# 🐍 Python API

The status checker can also be used directly from Python.

Import the function:

```python
from status_checker.check_status import check_status
```

Then provide a URL:

```python
status = check_status("https://example.com")

print(status)
```

Example result:

```text
200
```

---

## Return Values

The current implementation returns:

| HTTP Response | Function Result | Meaning                 |
| ------------- | --------------: | ----------------------- |
| `200`         |           `200` | Website is up           |
| `404`         |           `400` | Website considered down |
| `500`         |           `400` | Website considered down |
| Other         |           `400` | Website considered down |

> **Note:** The current implementation maps every non-200 response to `400`. It does not return the original HTTP status code.

---

# 🧪 Testing

The project uses **pytest** for automated testing.

Tests are located in:

```text
tests/
└── test_check_status.py
```

The tests verify important behavior such as:

- Successful HTTP responses
- Non-200 responses
- Server errors
- Correct URL handling

The HTTP requests are mocked during testing, so the test suite does not depend on an external website being online.

---

## Run Tests

Run all tests:

```bash
uv run pytest
```

For more detailed output:

```bash
uv run pytest -v
```

Example:

```text
============================= test session starts =============================

collected 4 items

tests/test_check_status.py ....                              [100%]

============================== 4 passed ==============================
```

---

# 📖 Documentation

The project uses **Sphinx** to generate documentation.

Documentation source files are located in:

```text
docs/source/
```

The main documentation files are:

```text
docs/source/
├── conf.py
├── index.rst
├── usage.rst
└── api.rst
```

---

## Install Sphinx

Sphinx is included in the development dependencies.

Install dependencies:

```bash
uv sync
```

Verify Sphinx:

```bash
uv run sphinx-build --version
```

---

## Build Documentation Locally

From the project root:

```bash
uv run sphinx-build -b html docs/source docs/build/html
```

After the build completes, the generated documentation will be located at:

```text
docs/build/html/
```

On macOS, you can open the documentation with:

```bash
open docs/build/html/index.html
```

---

## Live Documentation Development

For automatic rebuilding while editing documentation, you can install:

```bash
uv add --dev sphinx-autobuild
```

Then run:

```bash
uv run sphinx-autobuild docs/source docs/build/html
```

This automatically rebuilds the documentation when source files change.

---

# 🌐 Read the Docs

The project is configured to use **Read the Docs** for documentation hosting.

The configuration is stored in:

```text
.readthedocs.yaml
```

Read the Docs uses the Sphinx configuration:

```text
docs/source/conf.py
```

and documentation dependencies:

```text
docs/requirements.txt
```

After the GitHub repository is connected to Read the Docs, documentation builds can be triggered automatically whenever changes are pushed to the repository.

### Online Documentation

**https://status-checker.readthedocs.io/en/latest/**

---

# 🧰 Development

Install the development environment:

```bash
uv sync
```

Run the application:

```bash
uv run streamlit run app/app.py
```

Run tests:

```bash
uv run pytest
```

Build documentation:

```bash
uv run sphinx-build -b html docs/source docs/build/html
```

Build the Python package:

```bash
uv build
```

---

# 📦 Package Structure

The project follows the `src` layout:

```text
src/
└── status_checker/
    ├── __init__.py
    └── check_status.py
```

Using a `src` layout helps separate package source code from project configuration, tests, documentation, and other development files.

---

# ⚠️ Current Limitations

This project is intentionally simple and currently has several limitations.

### 1. No timeout

The HTTP request does not currently specify a timeout.

A future implementation should use something like:

```python
requests.get(url, timeout=10)
```

### 2. Limited error handling

Connection errors and other request exceptions are not currently handled.

For example:

- DNS failures
- Connection refused
- Network unavailable
- Timeout
- Invalid URL

could be handled more gracefully.

### 3. Non-200 responses

All non-200 responses currently become:

```text
400
```

This means the application does not distinguish between:

```text
301
302
400
401
403
404
500
502
503
```

### 4. No response-time information

The application currently does not show how long the request took.

### 5. Single URL

The current application checks one URL at a time.

---

# 🔮 Future Improvements

Possible improvements for future versions include:

- [ ] Add request timeout
- [ ] Handle connection exceptions
- [ ] Return the actual HTTP status code
- [ ] Display response time
- [ ] Validate URLs
- [ ] Support multiple URLs
- [ ] Add website monitoring history
- [ ] Add periodic monitoring
- [ ] Add availability statistics
- [ ] Add charts for uptime
- [ ] Add email notifications
- [ ] Add automated CI testing
- [ ] Improve Streamlit UI
- [ ] Add more comprehensive test coverage

---

# 🧪 Example Test Strategy

The project uses mocking to avoid depending on external websites.

For example, a successful response can be simulated:

```python
class MockResponse:
    status_code = 200
```

The test can then verify:

```python
assert check_status("https://example.com") == 200
```

A failed response can similarly be simulated:

```python
class MockResponse:
    status_code = 404
```

and verified with:

```python
assert check_status("https://example.com") == 400
```

This makes the test suite predictable and fast.

---

# 🤝 Contributing

Contributions and improvements are welcome.

A typical development workflow is:

```bash
git clone https://github.com/devwithNoumanButt/Status-Checker.git

cd Status-Checker

uv sync

uv run pytest

uv run streamlit run app/app.py
```

After making changes:

```bash
git status
```

Stage the changes:

```bash
git add .
```

Create a commit:

```bash
git commit -m "Describe your changes"
```

Push the changes:

```bash
git push origin main
```

---

# 📄 License

A license has not yet been specified for this project.

If you plan to make the project open source, consider adding a license such as:

- MIT
- Apache 2.0
- GPL-3.0

Once selected, add the license file to the repository.

---

# 👨‍💻 Author

**Nouman Shahid**

GitHub:

https://github.com/devwithNoumanButt

---

# 🔗 Links

| Resource          | Link                                                |
| ----------------- | --------------------------------------------------- |
| GitHub Repository | https://github.com/devwithNoumanButt/Status-Checker |
| Live Application  | https://status-checker-tool.streamlit.app/          |
| Documentation     | https://status-checker.readthedocs.io/en/latest/    |

---

## ⭐ Project Goal

The goal of Status Checker is to provide a simple introduction to building a Python project with:

```text
Python
   │
   ├── Package structure
   ├── HTTP requests
   ├── Automated testing
   ├── Streamlit
   ├── Sphinx
   ├── Read the Docs
   └── Modern dependency management
```

It is intentionally kept simple so that the project can serve as a foundation for adding more advanced website monitoring functionality in the future.
