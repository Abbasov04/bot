import os

class Config:

   API_ID = int(os.getenv("API_ID", "29918051"))
   API_HASH = os.getenv("API_HASH", "793e62b1b2aefe53f84976d38215959e")
   bot_token = os.getenv("bot_token", "5746131579:AAEDzPqfVsHst13-AlVCxs3Z2rZqOly8fPw")
   SUDO_USERS = os.getenv("SUDO_USERS", "5317589296")
   log_qrup = os.getenv("log_qrup", "-1001875414285")
