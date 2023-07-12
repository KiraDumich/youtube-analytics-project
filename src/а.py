import os
from dotenv import load_dotenv

# load environment variables from .env file
load_dotenv()

print(os.getenv("YI-API-KEY"))