import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "24997910"))
    API_HASH = os.environ.get("API_HASH", "7ed17bada7d9666fb73eec77de341186")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1255617228:AAH525jNxJjPl4d4tRi3iXntIY6wxE8Zy00")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1AQAOMTQ5LjE1NC4xNzUuNTMBu7PK686cp3Q2RrB/We/bwLHnl6KdGTwxk6iJgRBqVeFQx56BiB7Li/SGh7EJ9xcrrI+e1JEBc+p481RuE79qV/Vt+HLKzw2w1YmoRkTt+OCCl5MAQwRmvOsKVVrLUt1Qa+3734ByVuN2bRzR2ONXrHxzoD7ZFp7M1gBSztRwS8FdaldhOsqR2d8hTBJ341JlT0yKpgWjtXVss5vFX0+wPfFHOsHD117d8tEjqQcPo7oC3Go2L/dNBOZ9ONk/6KXZ3SRuNfz9MDvl2tCaHvnOA9pk52uzd7TieasHm5uUeRYWhCOTIUBxj/UrFWMUWU2+tFrMv5XI2kGo1qD0FzTLyrI=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "grra_bot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5557283129")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', true) # Change it to "True"
