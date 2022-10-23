import os
import discord
from discord.ext import commands
from cogs import MCOperation
from dotenv import load_dotenv
load_dotenv()

COGs = [
    "cogs.cog-start"
]

class MCServerBot(commands.Bot):
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
        # for cog in COGs:
        #     self.load_extension(cog)
    
    async def on_ready(self):
        print("=====")
        print("login")
        print("=====")
        await self.add_cog(MCOperation.ServerOperation(self))
        # await cog_start.setup(server_bot)
        # await MCOperation.setup(self)

intents = discord.Intents.default()
intents.message_content = True
server_bot = MCServerBot(command_prefix='!', intents=intents)

server_bot.run(os.getenv("TOKEN"))