from cryptography.fernet import Fernet

import discord 
import re

client = discord.Client()

@staticmethod
def set_timer(message):
    # $timer 1 echo
    # The above will repeat the word 'echo' in one minute
    minutes = re.search("\d+", message)
    echo = re.search("")
    print("You asked me to say "+)


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
        set_timer(message.content)

token=open("token","rb")
key=open("key","rb")
fk = Fernet(key.read())
client.run(fk.decrypt(token.read()))