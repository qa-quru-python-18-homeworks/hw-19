from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    bs_url: str
    bs_username: str
    bs_access_key: str
    timeout: int


settings = Settings()
