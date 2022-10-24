from discord.ext import commands, tasks
from serverstatus import ServerStatus
from server import Server
from dotenv import load_dotenv
load_dotenv()

COGs = [
    "MCOperation"
]

class MCServerBot(commands.Bot):
    
    def __init__(self, command_prefix, intents):
        super().__init__(command_prefix=command_prefix, intents=intents)
        self.server = Server()
        self.server_status = ServerStatus.stop
        self.allowed = [ServerStatus.stop, ServerStatus.playing, ServerStatus.waiting]

    
    async def on_ready(self):
        print("=====")
        print("login")
        print("=====")
        await self.load_extension("MCOperation")
        self.loop_joinlog.start()
    

    @tasks.loop(seconds=10)
    async def loop_joinlog(self):
        if(self.server_status == ServerStatus.waiting):
            print(self.server.getJoinLog()) 
    
