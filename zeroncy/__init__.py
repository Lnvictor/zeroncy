"""
______   _____   _____   _____  _      _  _____ __     __
    /   |       |     | |     | |\     | |       \     /
   /    |_____  |_____| |     | | \__  | |        \___/
  /     |       |    |  |     | |    \ | |          | 
 /_____ |_____  |     | |_____| |     \| |_____     |


 Welcome to zeroncy!!!

 A simple zero-dependency python library...
"""

from .exceptions import FileExtensionDoesNotCovered, VariableDoesNotExists
from .controller import DotEnvFileReader


FILE_TYPES_AVALIABLE = [None, ]
FILE_USED_IN_PROJECT = None

# If new configuration file type was added,
# Remember to update this code to make
# these types avaliable

single_controller = DotEnvFileReader(None)
ENV = dict()

def config(file_type: str=None):
    if not file_type in FILE_TYPES_AVALIABLE:
        raise FileExtensionDoesNotCovered()
    global ENV 
    ENV = single_controller.read_file()


def get(var_name: str, cast=None) -> any:
    # global ENV
    try:
        if cast is not None:
            var = cast(ENV[var_name]) 
            if cast == bool:
                var = not var
        else:
            var = ENV[var_name]
        return var
    except KeyError:
        raise VariableDoesNotExists()