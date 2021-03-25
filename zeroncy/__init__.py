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
from .controllers import DotEnvFileReader, JsonFileReader


FILE_TYPES_AVALIABLE = {None: DotEnvFileReader, dict: JsonFileReader}x

ENV = dict()

def config(file_type: str=None):
    if not file_type in FILE_TYPES_AVALIABLE.keys():
        raise FileExtensionDoesNotCovered()
    single_controller = FILE_TYPES_AVALIABLE.get(file_type)()
    global ENV
    ENV = single_controller.read_file()


def get(var_name: str, cast=None) -> any:
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
