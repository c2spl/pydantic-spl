"""
1. Arguments passed to the Settings class initialiser.
2. Environment variables, e.g. my_prefix_special_function as described above.
3. Variables loaded from a dotenv (.env) file.
4. Variables loaded from the secrets directory.
5. The default field values for the Settings model.
"""

from pydantic import BaseSettings


class Settings(BaseSettings):
    hello: str = "world"

    class Config:
        env_prefix = "x_"

        env_file = ".m.env"
        env_file_encoding = "utf8"

        secrets_dir = "./configs"
