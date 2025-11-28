from typing import Optional
from functools import lru_cache
from pydantic import ConfigDict
from pydantic_settings import BaseSettings


class BaseConfig(BaseSettings):
    ENV_STATE: Optional[str] = None

    model_config = ConfigDict(env_file=".env", extra="ignore")


class GlobalConfig(BaseConfig):
    DATABASE_URL: Optional[str] = None
    DB_FORCE_ROLL_BACK: bool = False
    SECRET_KEY: str = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"


class DevConfig(GlobalConfig):
    model_config = ConfigDict(env_prefix="DEV_", env_file=".env", extra="ignore")


class ProdConfig(GlobalConfig):
    model_config = ConfigDict(env_prefix="PROD_", env_file=".env", extra="ignore")


class TestConfig(GlobalConfig):
    DATABASE_URL: str = "sqlite:///test.db"
    DB_FORCE_ROLL_BACK: bool = True

    model_config = ConfigDict(env_prefix="TEST_", env_file=".env", extra="ignore")


@lru_cache()
def get_config(env_state: str):
    configs = {"dev": DevConfig, "prod": ProdConfig, "test": TestConfig}
    return configs[env_state]()


config = get_config(BaseConfig().ENV_STATE)