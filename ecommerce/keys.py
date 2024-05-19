from dotenv import load_dotenv
import os

load_dotenv()

keys = os.environ.get("api_key")
print(keys)
