import discord
from discord.ext import commands
from dotenv import load_dotenv
load_dotenv()

class Client:
    def __init__(self, intents):
        self.client = discord.Client(intents=intents)