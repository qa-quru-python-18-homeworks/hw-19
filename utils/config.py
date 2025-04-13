import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="data/.env")


class Config:
    BS_USERNAME = os.getenv("BS_USERNAME")
    BS_ACCESS_KEY = os.getenv("BS_ACCESS_KEY")
    TIMEOUT = float(os.getenv("TIMEOUT", "10.0"))
