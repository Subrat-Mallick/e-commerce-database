# settings.py

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "E-Commerce App"
    debug: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
