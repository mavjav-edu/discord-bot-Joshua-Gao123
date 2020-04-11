import discord 

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello')
    elif message.content=="go away":
        await message.channel.send("Goodbye") 
        await client.close()

client.run('NjU3MDM0MzU1NTYyMjUwMjQx.XpI2bg.eY5lJ1K1OoLNpPrwVh_hpxu-p6A') 