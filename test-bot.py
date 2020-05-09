from cryptography.fernet import Fernet

import discord, sys, threading, re
from time import sleep

client = discord.Client()

@staticmethod
def repeat(message):
    ''' 
    py:function: set_timer(message)
    py:summary: User invokes command like `$timer DD ECHO_STRING`
    where DD is the number of minutes
    and ECHO_STRING is the sentence to repeat
    :param str message: contains the whole command 
    '''
    print("You asked me to tell you "+ message)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello')
    elif message.content=="$go away":
        await message.channel.send("Goodbye") 
        await client.close()
    elif message.content.startswith('$timer'):
        pattern = re.compile('^\$timer\s*(\d+)\s*(.*)$')
        matches = re.match(pattern,message.content)
        timer = threading.Timer(matches[1], repeat, args=matches[2])

token=open("token","rb")
key=open("key","rb")
fk = Fernet(key.read())
client.run(fk.decrypt(token.read()))