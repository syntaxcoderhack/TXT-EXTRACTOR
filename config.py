import os
from os import getenv

API_ID = int(os.environ.get("API_ID", "27426550"))  # Replace "123456" with your actual api_id or use .env
API_HASH = os.environ.get("API_HASH", "994f8e90abd48bad09b64c0bed0e56b7")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7777329402:AAGg2dW9YnScNQRAoYqh2ExpnZHW2Wn3zXg")

OWNER_ID = int(os.environ.get("OWNER_ID", "1977145189"))  # Your Telegram user ID
SUDO_USERS = list(map(int, os.environ.get("SUDO_USERS", "1977145189").split()))  # Space-separated user IDs

MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://creatorar30:fdINvMPYXYwUyHdq@cluster0.pbaou.mongodb.net/?retryWrites=true&w=majority")
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002607772171"))  # Telegram channel ID (with -100 prefix)

PREMIUM_LOGS = os.environ.get("PREMIUM_LOGS", "-1002607772171")  # Optional
