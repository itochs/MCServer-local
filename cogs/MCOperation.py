from discord.ext import commands

class ServerOperation(commands.Cog):
    def __init__(self, bot) -> None:
        super().__init__()
        self.bot = bot
    
    @commands.command()
    async def start(self, context):
        await context.send("start")

def setup(bot):
    return bot.add_cog(ServerOperation(bot=bot))