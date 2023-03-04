import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5861684593:AAHWwARn74ZZFhjSjOBWeBm5GA61PAA2x48")
    API_ID = int(os.environ.get("API_ID", 18302370))
    API_HASH = os.environ.get("API_HASH", "03c2cced4dea9b1e96dce87558dd2381")
    DB_URL = os.environ.get("DATABASE_URL", "")
