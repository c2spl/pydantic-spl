from dataclasses import dataclass
import os

from app.settings_management import Settings


@dataclass
class Data:
    arg_env_file_value = "d"
    arg_secrets_dir_value = "x"
    env_value = "o"


def test_arg_env_file():
    s = Settings(_env_file="config/d.env", _secrets_dir="config")
    assert s.hello == Data.arg_env_file_value


def test_arg_secret_dir():
    s = Settings(_secrets_dir="config")
    assert s.hello == Data.arg_secrets_dir_value


def test_env_value():
    os.environ["x_hello"] = Data.env_value

    s = Settings()
    assert s.hello == Data.env_value
