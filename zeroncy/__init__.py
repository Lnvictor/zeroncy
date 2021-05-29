"""
______   _____   _____   _____  _      _  _____ __     __
    /   |       |     | |     | |\     | |       \     /
   /    |_____  |_____| |     | | \__  | |        \___/
  /     |       |    |  |     | |    \ | |          | 
 /_____ |_____  |     | |_____| |     \| |_____     |


 Welcome to zeroncy!!!

 A simple zero-dependency python library...
"""

from collections import OrderedDict

from .exceptions import FileExtensionDoesNotCovered, VariableDoesNotExists
from .controllers import DotEnvFileReader, JsonFileReader

FILE_TYPES_AVALIABLE = {None: DotEnvFileReader, dict: JsonFileReader}
ENV = OrderedDict()


def config(file_type: str = None) -> None:
    """
    The method that will call the Reader for
    file type choosed by user and call read_file
    method to make all env variables avaliable to be
    retrieved calling 'get' method

    @param:
        file_type: str -> type of configuration file that
        user writes env vars...
    """

    if not file_type in FILE_TYPES_AVALIABLE.keys():
        raise FileExtensionDoesNotCovered()
    single_controller = FILE_TYPES_AVALIABLE.get(file_type)()
    global ENV
    raw_data = single_controller.read_file()

    # Cleaning commented lines
    for key, value in raw_data.items():
        if not key.startswith("#"):
            ENV.update({key: value})


def get(var_name: str, cast: any = None, many: bool = False) -> any:
    """
    Get a specific env variable located on config file.
    If the var does not in config file, an VariableDoesNotExists
    will be raised...

    @param:
        var_name: str
        cast: any  -> to convert the var value to a detemined type
        many: bool -> if True, return a list of values
    """

    try:
        if cast is not None:
            var = cast(ENV[var_name])
            if cast == bool:
                var = not var
        else:
            var = (
                ENV[var_name].replace(" ", "").split(",")
                if many
                else ENV[var_name]
            )
        return var
    except KeyError:
        raise VariableDoesNotExists()
