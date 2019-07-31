Central Services Website Test Suite
===============

## About

This repository holds a Test Suite for our Central Services website.
It includes page-fragments, common actions, and test scripts to ensure the quality of the site.

## Installation

1. Install Python 3.5 or above (if you don't already have it)
2. Clone the repo
3. Download [chromedriver here](https://sites.google.com/a/chromium.org/chromedriver/downloads).
    1. Get the latest version
    2. Put the downloaded chromedriver.exe in this directory - `<repo root>/central_service_test_suite`
4. Create a virtual environment for the repo

```
Windows
cd <repo directory>
<your python exe> -m venv venv
venv\Scripts\activate.bat
pip install -U pip
pip install -U -r requirements.txt
deactivate
```

```
Linux
cd <repo directory>
<your python exe> -m venv venv
source venv/bin/activate
pip install -U pip
pip install -U -r requirements.txt
deactivate
```


## Getting Started

### PAGE OPTIONS

- **PAGE_ONE** - holds page fragments for commonly used widgets that are present on multiple pages - IE TopNav and LeftNav
    - USERNAME
    - PASSWORD
    - SUBMIT
- **PAGE_TWO** - holds page fragments. These would be unique pages. Any common actions that are contained within a single
page should be included as functions within the fragments (as opposed to creating an action.)
    - HEADER1
    - HEADER2
    - DESCRIPTION
    - FIELD1
    - FIELD2
- **PAGE_THREE** - holds commonly used actions that span multiple screens or fragments (If the action is common to a single page,
please put it in the page fragment directly.)
    - FIELD1
    - FIELD2
    - NAME
    - DESCRIPTION


###

- **widgets** - holds page fragments for commonly used widgets that are present on multiple pages - IE TopNav and LeftNav
- **fragments** - holds page fragments. These would be unique pages. Any common actions that are contained within a single
page should be included as functions within the fragments (as opposed to creating an action.)
- **actions** - holds commonly used actions that span multiple screens or fragments (If the action is common to a single page,
please put it in the page fragment directly.)
- **data** - holds commonly used strings and other data - IE users objects, sites objects
- **support** - holds generic helpful functionality - IE creation of test data
- **tests** - holds tests scripts. Should never be imported into any other file (or tests will run multiple times)
    - The [pytest framework](https://docs.pytest.org/en/latest/) is used for test running. This framework has a few rules
    so that tests are properly collected and ran.
        - Files that include tests must use this naming convention - *test_yourname.py*
        - Classes that include tests must use this naming convention - *TestYourClassName*
        - Functions that are a test must use this naming convention - *test_your_test_name*

### Structure

- **widgets** - holds page fragments for commonly used widgets that are present on multiple pages - IE TopNav and LeftNav
- **fragments** - holds page fragments. These would be unique pages. Any common actions that are contained within a single
page should be included as functions within the fragments (as opposed to creating an action.)
- **actions** - holds commonly used actions that span multiple screens or fragments (If the action is common to a single page,
please put it in the page fragment directly.)
- **data** - holds commonly used strings and other data - IE users objects, sites objects
- **support** - holds generic helpful functionality - IE creation of test data
- **tests** - holds tests scripts. Should never be imported into any other file (or tests will run multiple times)
    - The [pytest framework](https://docs.pytest.org/en/latest/) is used for test running. This framework has a few rules
    so that tests are properly collected and ran.
        - Files that include tests must use this naming convention - *test_yourname.py*
        - Classes that include tests must use this naming convention - *TestYourClassName*
        - Functions that are a test must use this naming convention - *test_your_test_name*

### Structure

- **widgets** - holds page fragments for commonly used widgets that are present on multiple pages - IE TopNav and LeftNav
- **fragments** - holds page fragments. These would be unique pages. Any common actions that are contained within a single
page should be included as functions within the fragments (as opposed to creating an action.)
- **actions** - holds commonly used actions that span multiple screens or fragments (If the action is common to a single page,
please put it in the page fragment directly.)
- **data** - holds commonly used strings and other data - IE users objects, sites objects
- **support** - holds generic helpful functionality - IE creation of test data
- **tests** - holds tests scripts. Should never be imported into any other file (or tests will run multiple times)
    - The [pytest framework](https://docs.pytest.org/en/latest/) is used for test running. This framework has a few rules
    so that tests are properly collected and ran.
        - Files that include tests must use this naming convention - *test_yourname.py*
        - Classes that include tests must use this naming convention - *TestYourClassName*
        - Functions that are a test must use this naming convention - *test_your_test_name*

### Structure

- **widgets** - holds page fragments for commonly used widgets that are present on multiple pages - IE TopNav and LeftNav
- **fragments** - holds page fragments. These would be unique pages. Any common actions that are contained within a single
page should be included as functions within the fragments (as opposed to creating an action.)
- **actions** - holds commonly used actions that span multiple screens or fragments (If the action is common to a single page,
please put it in the page fragment directly.)
- **data** - holds commonly used strings and other data - IE users objects, sites objects
- **support** - holds generic helpful functionality - IE creation of test data
- **tests** - holds tests scripts. Should never be imported into any other file (or tests will run multiple times)
    - The [pytest framework](https://docs.pytest.org/en/latest/) is used for test running. This framework has a few rules
    so that tests are properly collected and ran.
        - Files that include tests must use this naming convention - *test_yourname.py*
        - Classes that include tests must use this naming convention - *TestYourClassName*
        - Functions that are a test must use this naming convention - *test_your_test_name*
