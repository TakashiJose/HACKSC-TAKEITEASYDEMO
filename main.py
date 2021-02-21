#import libraries
import discord
from discord.ext import commands
import random

client=commands.Bot(command_prefix='>')

token = open("token.txt")
TOKEN = token.read()

#Funciton when bot initialized
@client.event
async def on_ready():
    print('Client running')

#Function when requesting image
@client.command()
async def image(ctx):
    print('sending image')
    await ctx.send(file=discord.File('capybottle.png'))
    await ctx.send("hello world")
    
@client.command()
async def guild(ctx):
    activeservers=client.guilds

    for guild in activeservers:
        await ctx.send(guild.id)
        print(client.guilds)

@client.command(pass_context=True)
async def call(ctx, *, arg):
    chosen=random.randint(1 ,len([s for s in client.guilds]))
    iterator=0
    for guild in client.guilds:
        iterator+=1
        if iterator == chosen:
            for channel in guild.channels:
                if channel.name == "bottle":
                    if isinstance(channel, discord.TextChannel):
                        if await channel.send(arg):
                            break


#initializes bot
client.run(TOKEN)