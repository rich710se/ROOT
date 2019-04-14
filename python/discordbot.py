import discord

TOKEN = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    print(message.content)

    # Do stuff
    if message.content.startswith('!'):
        await bot_actions(message)

async def post_embed(message, emoji="", title="", body=""):
    embed = discord.Embed(title=emoji+" "+title, description=body, color=0xffffff)
    embed.set_footer(text="Invoked by: "+message.author.name)
    await message.delete()
    await message.channel.send(embed=embed)

## Spesific actions
async def bot_actions(message):
    if message.content.startswith('!ping'):
        await post_embed(message, ":ping_pong:","ping?", "PONG!")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('---------------')

client.run(TOKEN)
