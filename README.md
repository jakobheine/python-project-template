# +++ DELETE THIS AREA +++
# python-project-template

This is a python project template to get you up and running in under one minute.
This template contains the following best practices:
- [**pytest**](https://docs.pytest.org/en/7.3.x/) for [testing](https://github.com/veilair/test-driven-development)
- [**flake8**](https://flake8.pycqa.org/en/latest/) for [linting](https://www.makeuseof.com/what-is-linting/)
- **venv** + **requirements.txt** for [dependency/package handling](https://docs.python.org/3/library/venv.html#:~:text=New%20in%20version%203.3.,installed%20in%20their%20site%20directories.)
- **README** instruction of usage + ToC


# --- DELETE THIS AREA ---
# Project Name
Introduce the project / repository in one-two sentences.

Table of Contents:
1. [Virtual Environment](#virtual-environment)<br/>
2. [Build](#build)<br/>
3. [Test](#test)<br/>
4. [Linting](#linting)<br/>

# Python version **3.11**

# Virtual Environment
To work locally with an virtual environment (venv) do the following steps:
1. Create a venv locally by running:
```
python -m venv venv
```
2. Activate the venv:
```
source venv/bin/activate
```
3. Install dependencies locally:
```
pip install -r requirements.txt
```

# Run
Use the following command to run the code:
```
python src/index.py
```

# Test
For testing, run:
```
pytest test
```

# Linting
For linting, run:
```
flake8 --config=flake8.ini
```
