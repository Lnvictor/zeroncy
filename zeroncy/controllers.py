"""
Controller classes to read the content
of configuration file.

The type file can be choosed between .env or .env.json file
"""

from abc import ABC, abstractmethod, abstractproperty
import os
import json


class AbstractEnvironmentFileReader(ABC):
    """
    Config files reader template.

    Contains abstract methods, that should be
    implemented by your childs. The aim of this class
    is define an interface of methods that allows read and
    providing env variables allocated on a determined configuration
    file. The type of config file may vary...

    If file type is None, its intended that file is .env
    """

    @property
    @abstractmethod
    def file_type():
        pass

    @abstractmethod
    def read_file() -> dict:
        pass


class DotEnvFileReader(AbstractEnvironmentFileReader):
    """
    Reads a .env file
    """

    @property
    def file_type(self) -> str:
        return self._file_type

    @file_type.setter
    def file_type(self, attr: str) -> None:
        self._file_type = attr

    def read_file(self) -> dict:
        lines = open(os.getcwd() + "/.env", encoding="utf-8").readlines()
        dotenv_vars = {x[0]: x[1].strip("\n") for x in [v.split("=") for v in lines]}
        dotenv_vars.update(os.environ)
        return dotenv_vars


class JsonFileReader(AbstractEnvironmentFileReader):
    """
    reads a .env.json file
    """

    @property
    def file_type(self) -> str:
        return self.file_type

    @file_type.setter
    def file_type(self, attr: str) -> None:
        self._file_type = attr

    def read_file(self) -> dict:
        dotenv_vars = json.loads(open(os.getcwd() + "/.env.json", encoding="utf-8").read())
        dotenv_vars.update(os.environ)
        return dotenv_vars
