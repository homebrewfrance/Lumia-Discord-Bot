import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('!guide'):
        args = message.content.split(' ')
        if len(args) != 2:
            await message.channel.send('Invalid command. Usage: !guide <console>')
            return

        console = args[1].lower()
        if console == 'dsi':
            embed = discord.Embed(title='Luma3DS', url='https://caca.com', description='A custom firmware for 3DS')
        elif console == '3ds':
            embed = discord.Embed(title='Guide 3ds', url='https://caca.com', description='Aguied3ds')
        else:
            await message.channel.send('Invalid console. Available consoles: dsi, 3ds')
            return
        
        embed.set_thumbnail(url='https://caca.com/caca-gros.png')
        embed.set_footer(text='Homebrew France', icon_url='https://caca.com/caca.png')
        await message.channel.send(embed=embed)

client.run('MTA4MDIxMDQ3Mzk4MDU0Mjk4Ng.G3dB3Y.TkiLNBjYJJKDHH0xsh4TnzK7Oz4_5htxvJ539c')
