import discord
from discord.ext import commands

# sounds like this is the how to tell it's a command ( eg: .gimmeMoney )
client = commands.Bot( command_prefix = '.' )

@client.event
async def on_ready():
    print( "Bot is ready" )

client.run( "Nzk1Mzg5Mzc2NjM2OTExNjE4.X_IqFQ.M8EI-WyLHGcUfnpxgYuKG1aJObI" )