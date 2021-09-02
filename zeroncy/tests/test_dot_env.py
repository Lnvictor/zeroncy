import pytest

from typing import List
import os

from .common import write_data
from .. import VariableDoesNotExists, FILE_TYPES_AVALIABLE, JsonFileReader
import zeroncy

DATA = {"DEBUG": "False", "NAME": "Victor", "ALLOWED_HOSTS": "localhost, 127.0.0.0.1", "#FOO": "FOO"}


@pytest.fixture
def prepare_dot_env_file() -> None:
    write_data("", DATA)
    with open(os.getcwd() + "/.env", "w") as file:
        for k, v in DATA.items():
            file.write(f"{k}={v}\n")

    zeroncy.config()


def test_env_vars_value(prepare_dot_env_file):
    """
    Test env variables here
    """
    assert not zeroncy.get("DEBUG", cast=bool)
    assert zeroncy.get("NAME") == "Victor"
    assert zeroncy.get("PATH") == os.environ["PATH"]
    assert isinstance(zeroncy.get("ALLOWED_HOSTS", many=True), list)

    with pytest.raises(VariableDoesNotExists):
        assert zeroncy.get("#FOO")
