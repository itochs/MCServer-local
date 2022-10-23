import os
import subprocess
from server import Server
from discord.ext import commands

class ServerOperation(commands.Cog):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot
        self.server = Server()


    @commands.command()
    async def start(self, context):
        await context.send("start")
        for log in self.server.start("minecraft_server/server-v1.19/"):
            print(log)


    @commands.command()
    async def stop(self, context):
        await context.send("stop")
        for log in self.server.stop():
            print(log)


def setup(bot):
    return bot.add_cog(ServerOperation(bot=bot))