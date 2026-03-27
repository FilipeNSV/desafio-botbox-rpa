from dotenv import load_dotenv
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

load_dotenv(ENV_FILE, override=True)

BASE_URL = os.getenv("BASE_URL", "").strip()
USERNAME = os.getenv("USERNAME", "").strip()
PASSWORD = os.getenv("PASSWORD", "").strip()

SLOW_MO = float(os.getenv("SLOW_MO", "1.0"))
DEFAULT_TIMEOUT = int(os.getenv("DEFAULT_TIMEOUT", "30"))
IMAGE_CONFIDENCE = float(os.getenv("IMAGE_CONFIDENCE", "0.85"))

ASSETS_DIR = BASE_DIR / os.getenv("ASSETS_DIR", "assets/bootbox_admin")