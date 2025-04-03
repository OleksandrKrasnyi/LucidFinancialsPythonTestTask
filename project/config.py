import os

# Configuration
SECRET_KEY = os.urandom(32).hex()
ALGORITHM = "HS256"
DATABASE_URL = "mysql+pymysql://your_username:your_password@localhost/myapp"  # !!! Replace with your data !!!
TOKEN_EXPIRY = 30  # minutes
CACHE_TTL = 5    # minutes for caching