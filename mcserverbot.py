import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

class MCServerBot(commands.Bot):
    async def on_ready(self):
        print("=====")
        print("login")
        print("=====")

intents = discord.Intents.default()
intents.message_content = True
server_bot = MCServerBot(command_prefix='!', intents=intents)
server_bot.run(os.getenv("TOKEN"))