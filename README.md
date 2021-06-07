MARKETDATA CLI
==============

Getting started
---------------
Checkout this project and use [Poetry](https://python-poetry.org).

Install dependencies

    poetry install

Execute

    poetry shell
    cd marketdata
    ./cli.py --help

Install a new module

    poetry add <module>




Config VSCodium
---------------

In this folder run 
    
    poetry shell
    which python

or

    poetry env info

to get the full path to the Pipenv's virtualenv. This is something like 

    /Users/me/Library/Caches/pypoetry/virtualenvs/marketdata-cli-MiIDVtXc-py3.7

Press Cmd+Shift+P and search for "Select Interpreter". Press enter, and select any of the suggested interpreters and a .vscode directory will be created inside your project root. It contains a settings.json. Edit this file and set python.pythonPath to the virtualenv path and add /bin/python at the end.

    {
        "python.pythonPath": "/Users/me/Library/Caches/pypoetry/virtualenvs/marketdata-cli-MiIDVtXc-py3.7/bin/python"
    }

Troubleshooting
---------------

Check if LANG and LC_ALL envirnonment variable is set:

    locale
    LANG="de_DE.UTF-8"
    LC_ALL="de_DE.UTF-8"
