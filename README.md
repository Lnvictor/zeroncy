# Zeroncy

A simple python tool to make your projet more decoupled.

Just put your project variables on a config file instead store in encironment variable. You can use a .env for json file...

## Installing

```console
pip install zeroncy
```

## How to Use
1. Using .env file
- create a .env file in project root and set variables...

    ```yml
  
    HOST=localhost
    PORT=5000
  
    ```

- Then you could use your variables on your settings module...

    ```python

    >>> import zeroncy
    
    >>> zeroncy.config()
    
    >>> zeroncy.get("HOST")
    >>> "localhost"

    # If you want a diferent type you can pass the cast parameter

    >>> zeroncy.get("PORT", cast=int)
    >>> 5000

    ```

2. Using .env.json file
- Create a .env.json file on project root:

    ```json

    {
        "HOST": "localhost",
        "PORT": 5000
    }

    ```

- Then you could use on a similar way as the previous
    
    ```python

    >>> import zeroncy
    
    >>> zeroncy.config(dict) # passes dict as parameter
    
    >>> zeroncy.get("HOST")
    >>> "localhost"

    >>> zeroncy.get("PORT")
    >>> 5000

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
    