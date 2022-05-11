import discord

TOKEN = open('token', 'r').read()

client = discord.Client(activity=discord.Game(name='with myself'))

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return 
    
    if message.channel.name == 'shitposting':
        if user_message[-1] == '?':
            await message.channel.send('what was the question?')
            return

client.run(TOKEN)