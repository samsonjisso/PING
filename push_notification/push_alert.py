# This program sends alert notificatoin to telegram, when a network 
from dotenv import load_dotenv
from os import getenv
from discord_webhook import DiscordWebhook

load_dotenv()

# Function that sends the alert notifiction
def push_notifiction (alertJson):
    try:
        discord = DiscordWebhook(url=getenv('WEB_HOOKS_URI'),content=alertJson)
        discord.execute()

    except:
        if (KeyboardInterrupt):
            print("Control-c")
        elif(Exception):
            print({"exception":Exception})
        else:
            print("unknown error")