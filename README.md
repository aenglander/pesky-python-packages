# Pesky Python  Packages

This project correlates to a presentation on Python Packaging. It has an
example for the common ways you can install dependencies.

## Setup Tools

The [setup.py](setup.py) file uses
[Setuptools](https://setuptools.readthedocs.io/en/latest/) to install
dependencies.

```bash
python setup.py install
```

## PIP

The [requirements.txt](requirements.txt) file can be used by
[PIP](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install -r requirements.txt
```

## Pipenv

The [Pipfile](Pipfile) and [Pipfile.lock](Pipfile.lock) files can be used by
[Pipenv](https://pipenv.kennethreitz.org/en/latest/) to install
dependencies.

```bash
pipenv install
```

## Anaconda

The [environment.yml](environment.yml) file can be used by
[Anaconda](https://docs.anaconda.com/anaconda/user-guide/) to install
dependencies.

```bash
conda env create
```
