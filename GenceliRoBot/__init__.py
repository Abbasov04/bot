import logging
from pyrogram import Client
from GenceliRoBot.config import Config

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

LOGGER = logging.getLogger(__name__)

AylinRobot = Client(
    'AylinRobot',
    bot_token = Config.bot_token,
    api_id = Config.API_ID,
    api_hash = Config.API_HASH
)
