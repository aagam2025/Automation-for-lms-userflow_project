import os
from dataclasses import dataclass
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

# -----------------------------
# Application Configuration
# -----------------------------
BASE_URL = os.getenv("BASE_URL", "https://qaautomationtesting1.empowerlms.com/")
LOGIN_EMAIL = os.getenv("LOGIN_EMAIL", "")
LOGIN_PASSWORD = os.getenv("LOGIN_PASSWORD", "")
LOGIN_EMAIL_1 = os.getenv("LOGIN_EMAIL_1", "")
LOGIN_PASSWORD_1 = os.getenv("LOGIN_PASSWORD_1", "")
USER_NAME = os.getenv("USER_NAME", "Abc")
USEREMAIL = os.getenv("USEREMAIL", "")
COURSE_ID = int(os.getenv("COURSE_ID", "719"))
CLIENT_ID = os.getenv("CLIENT_ID", "")
CLIENT_SECRET = os.getenv("CLIENT_SECRET", "")
TOKEN = os.getenv("TOKEN", "")

COURSE_PLAYER_PATH = "/local/courses/{course_id}/index.html"

# -----------------------------
# Timeouts (ms)
# -----------------------------
DEFAULT_TIMEOUT_MS = int(os.getenv("DEFAULT_TIMEOUT_MS", "30000"))
SHORT_TIMEOUT_MS = int(os.getenv("SHORT_TIMEOUT_MS", "5000"))

# -----------------------------
# Headless toggle
# Default = headed (visible)
# HEADLESS=1 -> headless
# HEADLESS=0 -> headed
# -----------------------------
HEADLESS = os.getenv("HEADLESS", "0").strip().lower() not in {"0", "false", "no"}

@dataclass(frozen=True)
class DeviceConfig:
    name: str
    viewport: dict
    user_agent: str
    device_scale_factor: float
    is_mobile: bool
    has_touch: bool

DEVICES = {
    # Laptop/Desktop
    "Desktop_1366x768": DeviceConfig(
        name="Desktop_1366x768",
        viewport={"width": 1366, "height": 768},
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120.0 Safari/537.36"
        ),
        device_scale_factor=1.0,
        is_mobile=True,
        has_touch=True,
    ),
    # "Desktop_1920x1080": DeviceConfig(
    #     name="Desktop_1920x1080",
    #     viewport={"width": 1920, "height": 1080},
    #     user_agent=(
    #         "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    #         "AppleWebKit/537.36 (KHTML, like Gecko) "
    #         "Chrome/120.0 Safari/537.36"
    #     ),
    #     device_scale_factor=1.0,
    #     is_mobile=False,
    #     has_touch=False,
    # ),
    # "Android_Pixel_5": DeviceConfig(
    #     name="Android_Pixel_5",
    #     viewport={"width": 393, "height": 851},
    #     user_agent=(
    #         "Mozilla/5.0 (Linux; Android 11; Pixel 5) "
    #         "AppleWebKit/537.36 (KHTML, like Gecko) "
    #         "Chrome/120.0.0.0 Mobile Safari/537.36"
    #     ),
    #     device_scale_factor=2.625,
    #     is_mobile=True,
    #     has_touch=True,
    # ),
    # "iPhone_12": DeviceConfig(
    #     name="iPhone_12",
    #     viewport={"width": 390, "height": 844},
    #     user_agent=(
    #         "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) "
    #         "AppleWebKit/605.1.15 (KHTML, like Gecko) "
    #         "Version/14.0 Mobile/15E148 Safari/604.1"
    #     ),
    #     device_scale_factor=3.0,
    #     is_mobile=True,
    #     has_touch=True,
    # ),
    # "iPad_Pro_11": DeviceConfig(
    #     name="iPad_Pro_11",
    #     viewport={"width": 834, "height": 1194},
    #     user_agent=(
    #         "Mozilla/5.0 (iPad; CPU OS 14_0 like Mac OS X) "
    #         "AppleWebKit/605.1.15 (KHTML, like Gecko) "
    #         "Version/14.0 Mobile/15E148 Safari/604.1"
    #     ),
    #     device_scale_factor=2.0,
    #     is_mobile=True,
    #     has_touch=True,
    # ),
}

# MOBILE_DEVICE_NAMES = []

# for device_name, device_config in DEVICES.items():
#     # Perform your action here
#     print(f"Processing device: {device_name}")
#     print(f"Viewport: {device_config.viewport}")
