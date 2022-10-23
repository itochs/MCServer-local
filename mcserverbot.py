import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

COGs = [
    "cogs.MCOperation"
]

class MCServerBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
    
    async def on_ready(self):
        print("=====")
        print("login")
        print("=====")
        await self.load_extension("cogs.MCOperation")

intents = discord.Intents.default()
intents.message_content = True
server_bot = MCServerBot(command_prefix='!', intents=intents)

server_bot.run(os.getenv("TOKEN"))