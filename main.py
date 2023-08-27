import discord
from discord.ext import commands
from discord.ext.commands.help import HelpCommand
import os
import sys
import asyncio
from datetime import datetime

intents = discord.Intents.all()

class MyHelp(HelpCommand):
    async def send_bot_help(self, mapping):
        bot = self.context.bot
        ctx = self.context
        
    
        embed_pages = [
             discord.Embed(title="Aide sur les commandes", description="Tapez ``.info [commande]`` pour obtenir des informations sur une commande ou ``.info [catégorie] pour une catégorie``", color=discord.Color.green()).add_field(name="**Générales :**", value="``.help``\n``.ping``\n``.info``").set_footer(text="Le Homebrew France | Page 1/3", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png").set_thumbnail(url="https://hbf-files.github.io/hbf_helper.png"), 
             discord.Embed(title="Aide sur les commandes", description="Tapez ``.info [commande]`` pour obtenir des informations sur une commande ou ``.info [catégorie] pour une catégorie``", color=discord.Color.blue()).add_field(name="**Homebrew :**", value="``.boxart``\n``.config``\n``.format``\n``.guide``\n``.ndsforwarders``\n``.non-brick``\n``.sdlock``").add_field(name="", value="``.sdroot``\n``.skins``\n``.tarifs``\n``.uninstall``\n``.update``\n``.widescreen``\n``.packs``\n``.imsp``").set_thumbnail(url="https://hbf-files.github.io/hbf_helper.png").set_footer(text="Le Homebrew France | Page 2/3", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png"),
             '''discord.Embed(title="Page 3", color=discord.Color.red()).add_field(name="Field 1", value="test3").add_field(name="Field 2", value="test3"),
             discord.Embed(title="Page 4", color=discord.Color.orange()).add_field(name="Field 1", value="test").add_field(name="Field 2", value="test4"),
             discord.Embed(title="Page 5", description="This is a multiline content:\nLine 1\nLine 2", color=discord.Color.purple())'''
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
    'homebrew', 'moderation'
]

@bot.event
async def on_ready():
    activity = discord.Game(name="KRAKEN LE MANGE GOURDE", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'Connected as {bot.user.name}')
    channel = bot.get_channel(883797017892106250)
    
    ping_message = f"``🟢 EN LIGNE (Ping: {bot.latency * 1000:.2f}ms)``"

    await channel.send(ping_message)
    await channel.send("``🟢 CONNECTE EN TANT QUE HBF HELPER SUR Le Homebrew France``")
    await channel.send("``HBF HELPER v0.0.1a - Multipurpose Discord Bot for Le Homebrew France``")

async def load_extensions():
    for extension in extensions:
        try:
            await bot.load_extension(extension)
            print(f'Loaded extension: {extension}')
        except Exception as e:
            print(f'Error loading extension {extension}: {e}')

@bot.event
async def on_connect():
    await load_extensions()

@bot.event
async def on_command(ctx):
    command = ctx.command
    author = ctx.author
    channel = ctx.channel
    print(f"Commande '{command.name}' appelée par {author} dans le canal '{channel}'")

@bot.command()
async def send_message(ctx, server_id: int, *, message_content: str):
    server = bot.get_guild(server_id)
    if server:
        await server.text_channels[0].send(message_content)
        await ctx.send(f"Message sent to {server.name}!")
    else:
        await ctx.send("Server not found!")


@bot.command()
async def imsp(ctx, serial_number: str = None):
    if serial_number is None:
        embed = discord.Embed(description="Veuillez entrer un numéro de série.", color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    
    if len(serial_number) < 14:
        embed = discord.Embed(description="Le numéro de série doit avoir au moins 14 caractères.", color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    
    prefix = serial_number[:3]
    try:
        num = int(serial_number[3:])
    except ValueError:
        embed = discord.Embed(description="Numéro de série invalide.", color=discord.Color.red())
        await ctx.send(embed=embed)
        return
    
    title = "Is My Switch Patched ?"   
    embed = discord.Embed(title=title, description=f"Numéro de série : {serial_number}", color=discord.Color.blue())
    
    if prefix == "XAW":
        if 10000000000 <= num < 10074000000:
            embed.add_field(name="__**Compatibilité**__", value="``🟢 Acceptée``").add_field(name="__**Détails**__", value="Votre console n'est pas patchée, elle est donc compatible avec la faille RCM.\n \nVous pouvez commencer le guide dès maintenant en cliquant [ici](https://homebrewfrance.github.io/docu/switch).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
        elif 10074000000 <= num <= 10120000000:
            embed.add_field(name="__**Compatibilité**__", value="``🟠 Rejetée``").add_field(name="__**Détails**__", value="Votre console est peut-être patchée, elle devrait être compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
        elif 10120000000 >= num >= 40000000000:
            embed.add_field(name="__**Compatibilité**__", value="``🔴 Rejetée``").add_field(name="__**Détails**__", value="Votre console est patchée, elle n'est donc pas compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
        elif 40000000000 <= num <= 40011000000:
            embed.add_field(name="__**Compatibilité**__", value="``🟢 Acceptée``").add_field(name="__**Détails**__", value="Votre console n'est pas patchée, elle est donc compatible avec la faille RCM.\n \nVous pouvez commencer le guide dès maintenant en cliquant [ici](https://homebrewfrance.github.io/docu/switch).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
        elif 40011000000 <= num <= 40012000000:
            embed.add_field(name="__**Compatibilité**__", value="``🟠 Rejetée``").add_field(name="__**Détails**__", value="Votre console est peut-être patchée, elle devrait être compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
        elif 40012000000 >= num >= 70000000000:
            embed.add_field(name="__**Compatibilité**__", value="``🔴 Rejetée``").add_field(name="__**Détails**__", value="Votre console est patchée, elle n'est donc pas compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
        elif 70000000000 <= num <= 70017800000:
            embed.add_field(name="__**Compatibilité**__", value="``🟢 Acceptée``").add_field(name="__**Détails**__", value="Votre console n'est pas patchée, elle est donc compatible avec la faille RCM.\n \nVous pouvez commencer le guide dès maintenant en cliquant [ici](https://homebrewfrance.github.io/docu/switch).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
        elif 70017800000 <= num <= 70030000000:
            embed.add_field(name="__**Compatibilité**__", value="``🟠 Rejetée``").add_field(name="__**Détails**__", value="Votre console est peut-être patchée, elle devrait être compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
        elif 70030000000 >= num >= 99999999999 :
            embed.add_field(name="__**Compatibilité**__", value="``🔴 Rejetée``").add_field(name="__**Détails**__", value="Votre console est patchée, elle n'est donc pas compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
    elif prefix == "XAJ":
        if 10000000000 <= num <= 10020000000:
            embed.add_field(name="__**Compatibilité**__", value="``🟢 Acceptée``").add_field(name="__**Détails**__", value="Votre console n'est pas patchée, elle est donc compatible avec la faille RCM.\n \nVous pouvez commencer le guide dès maintenant en cliquant [ici](https://homebrewfrance.github.io/docu/switch).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
        elif 10020000000 <= num <= 10030000000:
            embed.add_field(name="__**Compatibilité**__", value="``🟠 Rejetée``").add_field(name="__**Détails**__", value="Votre console est peut-être patchée, elle devrait être compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
        elif 10030000000 >= num >= 40000000000 :
            embed.add_field(name="__**Compatibilité**__", value="``🔴 Rejetée``").add_field(name="__**Détails**__", value="Votre console est patchée, elle n'est donc pas compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
        elif 40000000000 <= num <= 40046000000:
            embed.add_field(name="__**Compatibilité**__", value="``🟢 Acceptée``").add_field(name="__**Détails**__", value="Votre console n'est pas patchée, elle est donc compatible avec la faille RCM.\n \nVous pouvez commencer le guide dès maintenant en cliquant [ici](https://homebrewfrance.github.io/docu/switch).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
        elif 40046000000 <= num <= 40060000000:
            embed.add_field(name="__**Compatibilité**__", value="``🟠 Rejetée``").add_field(name="__**Détails**__", value="Votre console est peut-être patchée, elle devrait être compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
        elif 40060000000 >= num >= 70000000000:
            embed.add_field(name="__**Compatibilité**__", value="``🔴 Rejetée``").add_field(name="__**Détails**__", value="Votre console est patchée, elle n'est donc pas compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
        elif 70000000000 <= num <= 70040000000:
            embed.add_field(name="__**Compatibilité**__", value="``🟢 Acceptée``").add_field(name="__**Détails**__", value="Votre console n'est pas patchée, elle est donc compatible avec la faille RCM.\n \nVous pouvez commencer le guide dès maintenant en cliquant [ici](https://homebrewfrance.github.io/docu/switch).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
        elif 70040000000 <= num <= 70050000000:
            embed.add_field(name="__**Compatibilité**__", value="``🟠 Rejetée``").add_field(name="__**Détails**__", value="Votre console est peut-être patchée, elle devrait être compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).") .set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
        elif 70050000000 >= num >= 99999999999:
            embed.add_field(name="__**Compatibilité**__", value="``🔴 Rejetée``").add_field(name="__**Détails**__", value="Votre console est patchée, elle n'est donc pas compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
    elif prefix == "XKW" or prefix == "XKJ" or prefix == "XWW":
        if num >= 10000000000:
            embed.add_field(name="__**Compatibilité**__", value="``🔴 Rejetée``").add_field(name="__**Détails**__", value="Votre console est patchée, elle n'est donc pas compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text="Le Homebrew France | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/favicon.png")
    else:
        embed = discord.Embed(description="Veuillez entrer un numéro de série valide.", color=discord.Color.red())
        await ctx.send(embed=embed)
        return


    await ctx.send(embed=embed)

@bot.event
async def on_message(message):
    if message.author.id == 854048178907512884:
        if message.embeds:
            for embed in message.embeds:
                if embed.title == "📦 LumaPack • THZoria" or embed.author == "📦 LumaPack • THZoria":
                    await message.delete()
                    warning_embed = discord.Embed(
                        description="Cette commande de Poyo n'est pas disponible sur ce serveur.",
                        color=discord.Color.red()
                    )
                    await message.channel.send(embed=warning_embed)
        return
    await bot.process_commands(message)

@bot.command()
@commands.has_role(883639603817496596)
async def infos_serveur(ctx):
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
bot.run('BOT_TOKEN')
