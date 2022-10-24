from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

COGs = [
    "MCOperation"
]

class MCServerBot(commands.Bot):
    
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
    
    async def on_ready(self):
        print("=====")
        print("login")
        print("=====")
        await self.load_extension("MCOperation")
    
