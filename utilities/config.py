import os
from dotenv import load_dotenv

DEFULT_TIMEOUT_MS = int(os.getenv("DEFULT_TIMEOUT_MS", 15000))
load_dotenv()

GITHUB_URL = "https://github.com"
EMAIL = os.getenv("TEST_EMAIL")
PASSWORD = os.getenv("TEST_PASSWORD")