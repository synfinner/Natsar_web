#!/usr/bin/env python3

# script to create a natsar telegram client with Telethon
# import the required libraries
import os
from telethon import TelegramClient, events, sync
from pathlib import Path
from dotenv import load_dotenv

# load the environment variables
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# get the telegram app id and hash
telegram_app_id = os.getenv("TELEGRAM_APP_ID")
telegram_app_hash = os.getenv("TELEGRAM_APP_HASH")

# create a telegram client
client = TelegramClient('natsar', telegram_app_id, telegram_app_hash)

# connect to the telegram client
client.start()

# disconnect from the telegram client
client.disconnect()