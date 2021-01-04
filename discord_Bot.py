import discord
import random
from discord.ext import commands

import ast

# sounds like this is the how to tell it's a command ( eg: .gimmeMoney )
client = commands.Bot( command_prefix = '.' )

# Get dictionary from file and store is as usersDict
file = open("storage_File.txt", "r")

try: 
    contents = file.read()
    usersDict = ast.literal_eval( contents )
    file.close()
except:
    # file is empty
    usersDict = {}

print( "Dictionary from file: ", usersDict )

# Working write dictionary to file
with open('storage_File.txt', 'w') as f:
    print(usersDict, file=f)

@client.event
async def on_ready():
    print( "Bot is ready" )

# example command: ".roll 50"
@client.command()
async def roll(ctx, secondArg):
    try: 
        secondArg = int(secondArg)
        # wait for user input here
    except:
        await ctx.send("INVALID NUMBER")

    if ctx.message.author.id not in usersDict:
        usersDict[ctx.message.author.id] = 0
    win_status = random.choice([0,1])
    if win_status == 1:
        usersDict[ctx.message.author.id] += secondArg
    elif win_status == 0:
        usersDict[ctx.message.author.id] -= secondArg
        
    username = ctx.message.server.get_member("id")
    usermoney = usersDict[ctx.message.author.id]
    if usersDict[ctx.message.author.id] < 0 :
        await ctx.send(f'{username} is broke.')
    await ctx.send(f'{username} has {usermoney}')
    with open('storage_File.txt', 'w') as f:
        print(usersDict, file=f)


    
    
    


with open("bot_Token.txt","r") as f:
    string = f.read()
    token = str( string )

client.run( token )