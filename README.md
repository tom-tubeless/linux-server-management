# Linux Server Management

Teaching Linux-Server-Management

To build this Book yourself to need to do the following:

## Installation

### Dependencies
* virtualenv
* python-pip

### Create the Environment & enter

From the top directory of the Repo do:

```
$ python -m venv linux-server-management

$ cd linux-server-management

$ source linux-server-management/bin/activate

$ source linux-server-management/bin/activate.fish # if you are using fish
```

### Install Python-Packages in the Environment

```
$ python -m pip install --upgrade pip

$ pip install -r requirements.txt
```

### Exit the Environment

```
$ deactivate
```

## Building

Enter the Environment and do the following:

```
$ jupyter-book build --all book

$ ghp-import -n -p -f book/_build/html
```
