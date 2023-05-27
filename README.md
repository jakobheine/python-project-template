# +++ DELETE THIS AREA +++
# python-project-template

This is a python project template to get you up and running in under one minute.
This template contains the following best practices:
- **pytest** for [testing](https://github.com/veilair/test-driven-development)
- **flake8** for [linting](https://www.makeuseof.com/what-is-linting/)
- **venv** + **requirements.txt** for [dependency/package handling](https://docs.python.org/3/library/venv.html#:~:text=New%20in%20version%203.3.,installed%20in%20their%20site%20directories.)
- **README** instruction of usage + ToC


# --- DELETE THIS AREA ---
# Project Name
Introduce the project / repository in one-two sentences.

Table of Contents:
3. [Virtual Environment ](#virtual-environment)
4. [Build](#build)
5. [Test](#test)
6. [Linting](#linting)

# Python version **3.11**

# Virtual Environment
To work locally with an virtual environment (venv) do the following steps:
1. Create a venv locally by running:<br/>
```python -m venv venv```
2. Activate the venv:<br/>
```source venv/bin/activate```
3. Install dependencies locally:<br/>
```pip install -r requirements.txt```

# Run
Use the following command to run the code:<br/>
```python src/index.py```

# Test
For testing, run:<br/>
`pytest test`

# Linting
For linting, run:<br/>
```flake8 --config=flake8.ini```