import pytest

from .common import write_data
from .test_dot_env import DATA
import zeroncy


@pytest.fixture
def prepare_json_file() -> None:
    """
    Write env vars data into .env.json data...
    """

    write_data("json", DATA)
    zeroncy.config()


def test_check_data(prepare_json_file) -> None:
    """
    Values checks
    """

    assert not zeroncy.get("DEBUG", cast=bool)
    assert zeroncy.get("NAME") == "Victor"
    assert isinstance(zeroncy.get("ALLOWED_HOSTS", many=True), list)
