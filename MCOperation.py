# from server import Server
from discord.ext import commands
from serverstatus import ServerStatus

class ServerOperation(commands.Cog):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot
        

    @commands.command()
    async def start(self, context):
        if self.bot.server_status not in self.bot.allowed:
            return

        await context.send("start")
        self.bot.server_status = ServerStatus.starting
        for log in self.bot.server.start("../minecraft_server/server-v1.19/"):
            print(log)
        
        self.bot.server_status = ServerStatus.waiting


    @commands.command()
    async def stop(self, context):
        if self.bot.server_status not in self.bot.allowed:
            return

        await context.send("stop")
        self.bot.server_status = ServerStatus.stopping
        for log in self.bot.server.stop():
            print(log)
        
        self.bot.server_status = ServerStatus.stop


def setup(bot):
    return bot.add_cog(ServerOperation(bot=bot))