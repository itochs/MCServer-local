from discord.ext import commands
from serverstatus import ServerStatus


class ServerOperation(commands.Cog):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot

    async def changeStatus(self, ststus):
        self.bot.server_status = ststus

    @commands.command()
    async def start(self, context):
        if self.bot.server_status not in self.bot.allowed:
            return

        await context.send("start")
        await self.changeStatus(ServerStatus.starting)
        # self.bot.server_status = ServerStatus.starting
        for log in self.bot.server.start("../minecraft_server/server-v1.19/"):
            print(log)

        await self.changeStatus(ServerStatus.waiting)
        # self.bot.server_status = ServerStatus.waiting

    @commands.command()
    async def stop(self, context):
        if self.bot.server_status not in self.bot.allowed:
            return

        await context.send("stop")
        await self.changeStatus(ServerStatus.stopping)
        # self.bot.server_status = ServerStatus.stopping
        for log in self.bot.server.stop():
            print(log)

        await self.changeStatus(ServerStatus.stop)
        # self.bot.server_status = ServerStatus.stop


def setup(bot):
    return bot.add_cog(ServerOperation(bot=bot))
