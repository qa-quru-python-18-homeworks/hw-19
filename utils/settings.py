from pathlib import Path

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

_base_url = Path(__file__).resolve().parent.parent
_env_path = _base_url / 'data' / '.env'

load_dotenv(dotenv_path=_env_path)


class Settings(BaseSettings):
    bs_url: str
    bs_username: str
    bs_access_key: str
    timeout: int


settings = Settings()
