"""
Controller for reading .env content files
"""

from abc import ABC, abstractmethod, abstractproperty
import os


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

    def __init__(self, f_type):
        self.file_type = f_type
    
    @property
    def file_type(self) -> str:
        return self._file_type

    @file_type.setter
    def file_type(self, attr) -> None:
        self._file_type = attr
    
    def read_file(self) -> dict:
        lines = open(os.getcwd() + "/.env").readlines()
        return  {
            x[0]: x[1].strip('\n') for x in [v.split("=") for v in lines]
        }

        
class JsonFileReader(AbstractEnvironmentFileReader):
    """
    Still Not Implemented

    >--- TODO
    """
    pass
