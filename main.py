import discord
from discord.ext import commands
from discord.ext.commands.help import HelpCommand
from discord import app_commands
import os
import sys
import asyncio
import urllib.request
import zipfile
from datetime import datetime
import requests
import shutil
from bs4 import BeautifulSoup
import httpx
import aiohttp

intents = discord.Intents.all()
ver = "v0.0.2a"

class MyHelp(HelpCommand):
    async def send_bot_help(self, mapping):
        bot = self.context.bot
        ctx = self.context
        
    
        embed_pages = [
             discord.Embed(title="Aide sur les commandes", description="Tapez ``.info [commande]`` pour obtenir des informations sur une commande ou ``.info [catégorie] pour une catégorie``", color=discord.Color.green()).add_field(name="**Générales :**", value="``.help``\n``.ping``\n``.info``").set_footer(text=f"Lumia {ver} | Page 1/3", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png").set_thumbnail(url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png"), 
             discord.Embed(title="Aide sur les commandes", description="Tapez ``.info [commande]`` pour obtenir des informations sur une commande ou ``.info [catégorie] pour une catégorie``", color=discord.Color.blue()).add_field(name="**Homebrew :**", value="``.boxart``\n``.config``\n``.format``\n``.guide``\n``.ndsforwarders``\n``.non-brick``\n``.sdlock``\n``.packs``\n``.ps3compat``").add_field(name="``.lumiaio``", value="``.sdroot``\n``.skins``\n``.tarifs``\n``.uninstall``\n``.update``\n``.widescreen``\n``.packs``\n``.imsp``").set_thumbnail(url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png").set_footer(text=f"Lumia {ver} | Page 2/3", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png"),
             discord.Embed(title="Aide sur les commandes", description="Tapez ``.info [commande]`` pour obtenir des informations sur une commande ou ``.info [catégorie] pour une catégorie``", color=discord.Color.red()).add_field(name="**Modération :**", value="``.ban``\n``.tempban``\n``.mute``\n``.serverinfo``\n``.listservers``").set_footer(text=f"Lumia {ver} | Page 3/3", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png").set_thumbnail(url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png"), 
        ] 

        current_page = 0
        max_page = len(embed_pages) - 1

        embed = embed_pages[current_page]

        message = await ctx.send(embed=embed)
        await message.add_reaction("⏪")
        await message.add_reaction("◀️")
        await message.add_reaction("▶️")
        await message.add_reaction("⏩")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in ["⏪", "◀️", "▶️", "⏩"]

        while True:
            try:
                reaction, _ = await bot.wait_for('reaction_add', timeout=120, check=check)

                if str(reaction.emoji) == "⏪":
                    current_page = 0
                elif str(reaction.emoji) == "◀️":
                    current_page = max(0, current_page - 1)
                elif str(reaction.emoji) == "▶️":
                    current_page = min(max_page, current_page + 1)
                elif str(reaction.emoji) == "⏩":
                    current_page = max_page

                await message.edit(embed=embed_pages[current_page])
                await message.remove_reaction(reaction, ctx.author)

            except asyncio.TimeoutError:
                await message.clear_reactions()
                break

bot = commands.Bot(command_prefix='.', intents=intents, help_command=MyHelp())

extensions = [
    'homebrew', 'moderation', 'serialchecker', 'packs'
]

@bot.event
async def on_ready():
    print(f'Connected as {bot.user.name}')
    sys.stdout.flush()
    print(f'PIRACY IS NOT PARTY')
    sys.stdout.flush()
    channel = bot.get_channel(883797017892106250)
    
    ping_message = f"``🟢 EN LIGNE (Ping: {bot.latency * 1000:.2f}ms)``"

    await channel.send(ping_message)
    await channel.send("``🟢 CONNECTE EN TANT QUE Lumia SUR Le Homebrew France``")
    await channel.send(f"``Lumia {ver} - Multipurposes Discord Bot for Le Homebrew France``")

    activities = [
        discord.Game(name=f"Lumia#5037 | {ver}"),
        discord.Activity(type=discord.ActivityType.watching, name="Le Homebrew France | .help")
    ]
    current_activity_index = 0
    
    while not bot.is_closed():
        await bot.change_presence(activity=activities[current_activity_index])
        
        current_activity_index = 1 - current_activity_index
        
        await asyncio.sleep(10)

async def load_extensions():
    for extension in extensions:
        try:
            await bot.load_extension(extension)
            print(f'Loaded extension: {extension}')
            sys.stdout.flush()
        except Exception as e:
            print(f'Error loading extension {extension}: {e}')
            sys.stdout.flush()

@bot.event
async def on_connect():
    await load_extensions()

@bot.event
async def on_command(ctx):
    command = ctx.command
    author = ctx.author
    channel = ctx.channel
    print(f"Commande '{command.name}' appelée par {author} dans le canal '{channel}'")
    sys.stdout.flush()

@bot.command()
@commands.has_role(883639603817496596)
async def serverinfo(ctx):
    serveur = ctx.guild
    nom_serveur = serveur.name
    description_serveur = serveur.description if serveur.description else "Aucune description"
    nombre_membres_serveur = serveur.member_count
    proprietaire_serveur = serveur.owner
    date_creation_serveur = serveur.created_at.strftime("%d/%m/%Y %H:%M:%S") if serveur.created_at else "Date de création inconnue"

    embed = discord.Embed(title="Informations du serveur", color=discord.Color.blue())
    embed.add_field(name="Nom", value=nom_serveur, inline=False)
    embed.add_field(name="Description", value=description_serveur, inline=False)
    embed.add_field(name="Nombre de membres", value=nombre_membres_serveur, inline=False)
    embed.add_field(name="Propriétaire", value=proprietaire_serveur, inline=False)
    embed.add_field(name="Date de création", value=date_creation_serveur, inline=False)
    await ctx.send(embed=embed)

@bot.command()
async def info(ctx, command_name):
    command = bot.get_command(command_name)
    if command:
        embed = discord.Embed(title=f"__**Informations sur la commande :**__ ``{command.name}``", description=command.description, color=discord.Color.yellow())
        embed.set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
        embed.set_author(name="💡 Aide")
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(description="La commande spécifiée n'a pas été trouvée.")
        await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, message):
    if "@everyone" in message or "@here" in message:
        await ctx.send("Désolé, mais vous ne pouvez pas utiliser ``everyone`` ou ``here`` avec cette commande.")
    else:
        await ctx.send(message)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    error_message = f"Erreur lors de l'exécution de la commande {ctx.command}: {error}"
    channel_id = 883797017892106250
    error_channel = bot.get_channel(channel_id)
    if error_channel:
        await error_channel.send(error_message)

@bot.command()
async def ping(ctx):
    latency = bot.latency * 1000
    await ctx.send(f'Pong! Latence: {latency:.2f}ms')

@bot.command()
@commands.has_role(883639603817496596)
async def stop(ctx):
    await ctx.send("``🔴 ARRÊT...``")
    await ctx.send("``🔴 DECONNEXION DE Le Homebrew France...``")
    await bot.close()

print("Bot is now running...")
sys.stdout.flush()
bot.run('')
