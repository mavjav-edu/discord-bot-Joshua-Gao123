import discord, sys, threading, re, asyncio, keyring

from discord.ext import commands
from time import sleep

bot = commands.Bot(command_prefix='$')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello')

@bot.command()
async def goaway(ctx):
    await ctx.send('Goodbye')
    await client.close()

@bot.command()
async def timer(ctx,*,args)
    pattern = re.compile("""
        \s*     # matches zero or more whitespace characters
        (\d+)   # capturing group 1: matches one or more digit characters
        \s*     # matches zero or more whitespace characters
        (.*)    # capturing group 2: matches zero or more of any character
        """,re.VERBOSE)
        matches = re.match(pattern,args) # `matches[0]` is the entire string matching the pattern; `matches[1]` is the first capture group; `matches[2]` is the second capture group
        await message.channel.send("Sure. I'll remind you in "+matches[1]+" second"+('','s')[int(matches[1])>1]) # bot uses the correct plural or singular for time based on number of seconds specified
        asyncio.ensure_future(settimer(int(matches[1]),ctx,matches[2])) # multithreaded function calls

async def settimer(t,channel,message): # TODO: Make serializable
    await asyncio.sleep(t)
    await channel.send("Remember, "+"'"+message+"'")

@staticmethod
def repeat(message): # TODO: Make serializable
    ''' 
    py:function: set_timer(message)
    py:summary: User invokes command like `$timer DD ECHO_STRING`
    where DD is the number of minutes
    and ECHO_STRING is the sentence to repeat
    :param str message: contains the whole command 
    '''
    print("You asked me to tell you "+ message)


@client.event
async def on_ready(): # TODO: Replace with `command.Bot` notation
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): # TODO: Check if this is OK with `command.Bot` implementation
    if message.author == bot.user:
        return       

key=open("key","rb")

bot.run(keyring.get_password("system", (key.read())))