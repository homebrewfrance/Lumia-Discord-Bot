

import discord
import requests
from datetime import datetime
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
client = discord.Client(intents=intents)

TOKEN = "{BOT_TOKEN}"
CHANNEL_ID = "892813233059151902"

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user}')
    current_time = datetime.now().strftime("%H:%M:%S")
    current_date = datetime.now().strftime("%m/%d/%Y")
    channel = bot.get_channel(int(CHANNEL_ID))
    await channel.send(f"`Statut : Connecté à {current_time} le {current_date} en tant que {bot.user}`")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Le Homebrew France", details=f"{len(bot.guilds[0].members)} membres", state="https://homebrewfrance.fr/discord"))

@bot.command(name='guide')
async def guide(ctx, console):
    if console.lower() == 'dsi':
        embed = discord.Embed(title='Guide DSi', url='https://dsi.cfw.guide/fr-FR', description='Un guide complet pour modder votre Nintendo DSI.', color=discord.Color.blue())
        embed.set_author(name='DS-Homebrew', icon_url='https://avatars.githubusercontent.com/u/46971470?s=200&v=4')
        embed.set_footer(text='Le Homebrew France', icon_url='https://cdn.discordapp.com/icons/883623179979984896/a_52794001e75f82c85b15b01ca971a72b?size=64')
        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/8/89/Nintendo-DSi-Bl-Open.png')
        await ctx.send(embed=embed)
    elif console.lower() == '3ds':
        embed = discord.Embed(title='Guide 3DS', url='https://3ds.hacks.guide/fr_FR/', description='Un guide complet pour le custom firmware de la 3DS, depuis le firmware original vers boot9strap.', color=discord.Color.red())
        embed.set_author(name='Nintendo-Homebrew & Plailect', icon_url='https://avatars.githubusercontent.com/u/38025742?s=280&v=4')
        embed.set_footer(text='Le Homebrew France', icon_url='https://cdn.discordapp.com/icons/883623179979984896/a_52794001e75f82c85b15b01ca971a72b?size=64')
        embed.set_thumbnail(url='https://lh3.googleusercontent.com/proxy/1P6EQL4b2uEuOudqcTOVXIuddSSk552dDipN7D2A05i9hP3yXsM1Oq6-WRevnj67DBmhw4igm32yIghqrlcRshIQdA9wPEwvz5W7qTRjtVgpAqLRwrmcDblABTobbvwzd7IikURe18ck1mKg')
        await ctx.send(embed=embed)
    elif console.lower() == 'psvita':
        embed = discord.Embed(title='Guide PSVita', url='https://vita.hacks.guide/', description='Un guide complet pour le custom firmware PS Vita (TV), depuis le firmware original vers Henkaku.', color=discord.Color.blue())
        embed.set_author(name='emiyl & Plailect', icon_url='https://github.com/emiyl.png')
        embed.set_footer(text='Le Homebrew France', icon_url='https://cdn.discordapp.com/icons/883623179979984896/a_52794001e75f82c85b15b01ca971a72b?size=64')
        embed.set_thumbnail(url='https://enso.henkaku.xyz/enso.png')
        await ctx.send(embed=embed)
    elif console.lower() == 'switch':
        embed = discord.Embed(title='Guide Nintendo Switch', url='https://jeffvi.github.io/Switch-guide-FR/', description='Un guide complet pour le custom firmware de la , depuis le firmware original vers Atmosphère.', color=discord.Color.blue())
        embed.set_author(name='JeffVI et Nintendo-Homebrew', icon_url='https://avatars.githubusercontent.com/u/38025742?s=280&v=4')
        embed.set_footer(text='Le Homebrew France', icon_url='https://cdn.discordapp.com/icons/883623179979984896/a_52794001e75f82c85b15b01ca971a72b?size=64')
        embed.set_thumbnail(url='https://lh3.googleusercontent.com/proxy/rFesUV6hBrxycXemK2Fs99lNXfFbbztnn0v42yZ51gP8sFK5qvKkxEP2lQFIQIxu0ueBVN_8x2RPxgwCYrS3oGA6_98qtENyP4HVxo4H0h4SaBOKq-l0xmctrXRdcNtThjc6u9EDzNg2WG9aGf38XMpzbWu-IWw')
        await ctx.send(embed=embed)
    elif console.lower() == 'wiiu':
        embed = discord.Embed(title='Guide Wii U', url='https://wiiu.hacks.guide/#/fr_FR/', description='Un guide complet pour le custom firmware de la Wii U, depuis le firmware original vers Tiramisu.', color=discord.Color.blue())
        embed.set_author(name='Nintendo-Homebrew', icon_url='https://avatars.githubusercontent.com/u/38025742?s=280&v=4')
        embed.set_footer(text='Le Homebrew France', icon_url='https://cdn.discordapp.com/icons/883623179979984896/a_52794001e75f82c85b15b01ca971a72b?size=64')
        embed.set_thumbnail(url='https://lh3.googleusercontent.com/proxy/DEsQosxV9ZMUn1aYjHC93wxMrAhM3Q-EFeOlhHY_r6LZCW16XyWwrcD0j2xTXdx360F0ts91_zU1RZ70aLcqd-VInGimc0SCrr9iJHIyANc7I0ymikR2OgXsnU5VnGiI4hyYqqiSlV4ZiIWSWJoIer0Jotafvnmx0g')
        await ctx.send(embed=embed)
    elif console.lower() == 'wii':
        embed = discord.Embed(title='Guide Wii', url='https://wii.guide/fr-FR', description='Un guide complet pour le custom firmware de la Wii, depuis le firmware original vers un CFW.', color=discord.Color.blue())
        embed.set_author(name='RiiConnect24', icon_url='https://rc24.xyz/images/logo_small.png')
        embed.set_footer(text='Le Homebrew France', icon_url='https://cdn.discordapp.com/icons/883623179979984896/a_52794001e75f82c85b15b01ca971a72b?size=64')
        await ctx.send(embed=embed)
    else:
        await ctx.send('Commande invalide. Les consoles disponibles sont : ``dsi | 3ds | psvita | switch | wii | wiiu``')

@bot.command(name='config')
async def config(ctx, cfw):
    if cfw.lower() == 'luma':
        embed = discord.Embed(title='Configuration de Luma', description='Sélectionnez les options encadrées.', color=discord.Color.blue())
        embed.set_image(url='https://media.discordapp.net/attachments/962030917495447613/1080578272406032435/IMG_20230224_101417.png')
        embed.set_footer(text='Le Homebrew France', icon_url='https://cdn.discordapp.com/icons/883623179979984896/a_52794001e75f82c85b15b01ca971a72b?size=64')
        await ctx.send(embed=embed)
        
@bot.command(name='sdroot')
async def sdroot(ctx):
    embed = discord.Embed(title='La racine d`une carte SD :', color=discord.Color.blue())
    embed.set_image(url='https://media.discordapp.net/attachments/882625509824004199/917855780533833828/le_root.png')
    embed.set_footer(text='Le Homebrew France', icon_url='https://cdn.discordapp.com/icons/883623179979984896/a_52794001e75f82c85b15b01ca971a72b?size=64')
    await ctx.send(embed=embed)
    
@bot.command(name='sdlock')
async def sdlock(ctx):
    embed = discord.Embed(title='Problème de lecture de Carte SD :', description='Retirez la protection en écriture comme indiqué.', color=discord.Color.blue())
    embed.set_image(url='https://media.discordapp.net/attachments/882625509824004199/917864574429048912/IMG_20211207_204516.png')
    embed.set_footer(text='Le Homebrew France', icon_url='https://cdn.discordapp.com/icons/883623179979984896/a_52794001e75f82c85b15b01ca971a72b?size=64')
    await ctx.send(embed=embed)
   
@bot.command(name='isbricked')
async def isbricked(ctx):
    embed = discord.Embed(title='Ma console est-elle brickée ?', description='Si la LED bleue de votre 3DS sʾallume puis sʾéteint instantanément, non votre console nʾest pas brickée. Il sʾagit simplement dʾun fichier manquant sur votre Carte SD : le `boot.firm`. Placez-le à la racine de votre Carte SD.', color=discord.Color.blue())
    embed.add_field(name="Lien de téléchargement :", value="https://github.com/Nanquitas/Luma3DS/releases/latest/download/boot.firm", inline=False)
    embed.set_thumbnail(url='https://media.discordapp.net/attachments/959465064556036220/962404229983662100/IMG_20220409_193009.png')
    embed.set_footer(text='Le Homebrew France', icon_url='https://cdn.discordapp.com/icons/883623179979984896/a_52794001e75f82c85b15b01ca971a72b?size=64')
    await ctx.send(embed=embed)
    
@bot.command(name='vguides')
async def vguides(ctx):
    embed=discord.Embed(title='Avertissement concernant les tutoriels vidéos sur YouTube', description='Il est déconseillé de suivre des guides vidéos provenant de YouTube ou toute autre plateforme, ces guides sont bien souvent peu mis à jour et les créateurs ont tendance à faire des packs contenant tous les fichiers quʾils hébergent eux-mêmes, rendant impossible la mise à jour de ces fichiers. Vigilance particulière aux tutoriels de MikeGamers étant particulièrement désinformateurs et rempli de fautes en tous genres pouvant parfois aller jusquʾà endommager la console ou certains fichiers. Il est donc déconseillé de suivre ses tutoriels et de manière plus générale les tutoriels vidéos. Ne croyez que les guide `hacks.guide` rédigés par les développeurs eux-mêmes et régulièrement mis à jour.')
    embed.set_footer(text='Le Homebrew France', icon_url='https://cdn.discordapp.com/icons/883623179979984896/a_52794001e75f82c85b15b01ca971a72b?size=64')
    await ctx.send(embed=embed)

@bot.command(name='say')
async def say(ctx, *, arg):
    await ctx.send(arg)
    
@bot.command(name='roubaix')
async def roubaix(ctx):
    await ctx.send('https://france3-regions.francetvinfo.fr/image/iISh83rq9KUA68XxOOhF1j6_p0g/1200x1200/regions/2020/06/08/5ede65ea360b4_6908902064_2b5c2f821f_b.jpg')
    
@bot.command(name='shutdown')
async def shutdown(ctx):
    await ctx.send('``Statut : Déconnexion en cours...``')
    print(f'Fermeture de session de {bot.user}. Déconnexion de {ctx.guild.name} avec succès.')
    await ctx.send('``Statut : Déconnexion : Succès !``')
    await bot.close()

bot.run('{BOT_TOKEN}')
