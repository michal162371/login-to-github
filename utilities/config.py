import os
from dotenv import load_dotenv

DEFULT_TIMEOUT_MS = int(os.getenv("DEFULT_TIMEOUT_MS", 15000))
load_dotenv()

GITHUB_URL = "https://github.com"
TEST_EMAIL = os.getenv("TEST_EMAIL")
TEST_PASSWORD = os.getenv("TEST_PASSWORD")