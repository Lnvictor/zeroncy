# Zeroncy

A simple python tool to make your projet more decoupled.

Just put your project variables on a config file instead store in encironment variable. You can use a .env for json file...

[![PyPI version](https://badge.fury.io/py/zeroncy.svg)](https://badge.fury.io/py/zeroncy)
![Coverage](./cov-badge.svg)
[![Tests](https://github.com/Lnvictor/zeroncy/actions/workflows/python-app.yml/badge.svg)](https://github.com/Lnvictor/zeroncy/actions/workflows/python-app.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html)

## Installing

```console
pip install zeroncy
```

## How to Use
1. Using .env file
- create a .env file in project root and set variables...

    ```yml
    
    DATABASE_URL=postgres://user:pwd@localhost:5432/psql
    ALLOWED_HOSTS=localhost, 127.0.0.0.1
    PORT=5000
  
    ```

- Then you could use your variables on your settings module...

    ```python

    >>> import zeroncy
    
    >>> zeroncy.config()
    
    >>> zeroncy.get("DATABASE_URL")
    'postgres://user:pwd@localhost:5432/psql'

    # If you want a diferent type you can pass the cast parameter

    >>> zeroncy.get("PORT", cast=int)
    5000

    # If your var has more than one value, you must set the many parameter to true...

    >>> zeroncy.get("ALLOWED_HOSTS", many=True)
    ['localhost', '127.0.0.0.1']

    ```

2. Using .env.json file
- Create a .env.json file on project root:

    ```json

    {
        "DATABASE_URL": "postgres://user:pwd@localhost:5432/psql",
        "ALLOWED_HOSTS": "localhost, 127.0.0.0.1",
        "PORT": 5000
    }

    ```

- Then you could use on a similar way as the previous
    
    ```python

    >>> import zeroncy
    
    >>> zeroncy.config(dict) # passes dict as parameter
    
    >>> zeroncy.get("DATABASE_URL")
    'postgres://user:pwd@localhost:5432/psql'

    >>> zeroncy.get("PORT")
    5000

    >>> zeroncy.get("ALLOWED_HOSTS", many=True)
    ['localhost', '127.0.0.0.1']

    # Note that on Json config you don't need to passes cast parameter for other types (Integer in this example)

    ```

# References

- This project was inpired by [python-decouple](https://github.com/henriquebastos/python-decouple) lib, it's a simpler adaption

- [Python Docs]()

---

# LICENSE

                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.  
    
