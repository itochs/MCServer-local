import os
import subprocess
import server
from discord.ext import commands

class ServerOperation(commands.Cog):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot
        self.server = server.Server()
    
    @commands.command()
    async def start(self, context):
        await context.send("start")
        for log in server.start():
            print(log)


    @commands.command()
    async def end(self, context):
        await context.send("end")
        for log in server.stop():
            print(log)

def setup(bot):
    return bot.add_cog(ServerOperation(bot=bot))