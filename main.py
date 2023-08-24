import discord
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    activity = discord.Game(name="HBF Helper | Le Homebrew France", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f'Connected as {bot.user.name}')
    channel = bot.get_channel(883797017892106250)
    await channel.send("``🟢 EN LIGNE``")
    await channel.send("``🟢 CONNECTE EN TANT QUE HOMEBREW FRANCE HELPER SUR Le Homebrew France)``")

@bot.event
async def on_command(ctx):
    command = ctx.command
    author = ctx.author
    channel = ctx.channel
    print(f"Commande '{command.name}' appelée par {author} dans le canal '{channel}'")

@bot.command(name='sdroot')
async def yagpdb_command(ctx):
    embed = discord.Embed(title="La racine d'une Carte SD :", color=discord.Color.blue())
    embed.set_image(url="https://media.discordapp.net/attachments/882625509824004199/917855780533833828/le_root.png")
    embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
    
    await ctx.send(embed=embed)

@bot.command(name='sdlock')
async def yagpdb_command(ctx):
    embed = discord.Embed(title="Problème de lecture de Carte SD :", description="Retirer la protection en écriture comme indiqué", color=discord.Color.blue())
    embed.set_image(url="https://media.discordapp.net/attachments/882625509824004199/917864574429048912/IMG_20211207_204516.png")
    embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
    
    await ctx.send(embed=embed)

@bot.command(name='config')
async def config_command(ctx, option: str):
    if option.lower() == 'luma':
        embed = discord.Embed(title="Aide à la configuration de Luma :", description="Sélectionner les options encadrées", color=discord.Color.blue())
        embed.set_image(url="https://media.discordapp.net/attachments/962030917495447613/1080578272406032435/IMG_20230224_101417.png")
        embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        
        await ctx.send(embed=embed)
    else:
        await ctx.send("Commande non-reconnue. Usage: `.config luma`")

@bot.command(name='non-brick')
async def yagpdb_command(ctx):
    embed = discord.Embed(title="Ma console est-elle brickée ?", description="Si la LED bleue de votre 3DS s'allume puis s'éteint instantanément, non votre console n'est pas brickée. Il s'agit simplement d'un fichier manquant sur votre Carte SD : le `boot.firm`, il est disponible en téléchargement ici, placez le à la racine de votre Carte SD : [Téléchargement du boot.firm](https://github.com/Nanquitas/Luma3DS/releases/download/latest/boot.firm)", color=discord.Color.blue())
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/959465064556036220/962404229983662100/IMG_20220409_193009.png")
    embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
    
    await ctx.send(embed=embed)

@bot.command(name='widescreen')
async def yagpdb_command(ctx):
    embed = discord.Embed(title="Mode plein écran (TWiLightMenu++)", url="https://wiki.ds-homebrew.com/fr-FR/twilightmenu/playing-in-widescreen", description="Utilisation du mode plein d'écran sur le TWiLightMenu++", color=discord.Color.blue())
    embed.set_author(name="DS-Homebrew Wiki")
    embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/46971470?s=200&v=4")
    embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
    
    await ctx.send(embed=embed)

@bot.command(name='boxart')
async def yagpdb_command(ctx):
    embed = discord.Embed(title="Obtenir des box art (Jaquettes de jeux) (TWiLightMenu++)", url="https://wiki.ds-homebrew.com/fr-FR/twilightmenu/how-to-get-box-art", description="Comment ajouter des box art sur le TWiLightMenu++", color=discord.Color.blue())
    embed.set_author(name="DS-Homebrew Wiki")
    embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/46971470?s=200&v=4")
    embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
    
    await ctx.send(embed=embed)

@bot.command(name='skins')
async def skins_command(ctx, attribute: str):
    if attribute.lower() == 'twl':
        embed = discord.Embed(title="Thèmes (Skins) (TWiLightMenu++)", url="https://skins.ds-homebrew.com/", description="Une collection de thèmes pour le TWiLightMenu++ de DS-Homebrew/twlmenu-extras sur GitHub", color=discord.Color.blue())
        embed.set_author(name="DS-Homebrew Wiki")
        embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/46971470?s=200&v=4")
        embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        
        await ctx.send(embed=embed)
    else:
        await ctx.send("Commande non-reconnue. Usage: `.skins twl`")

@bot.command(name='format')
async def format_command(ctx, attribute: str):
    if attribute.lower() == 'rufus':
        embed = discord.Embed(title="Formatage en FAT32 (Rufus) :", image="https://media.discordapp.net/attachments/960942679473135686/962666707711840306/unknown.png", description="Téléchargez Rufus : [Téléchargement de Rufus](https://github.com/pbatard/rufus/releases/download/v3.17/rufus-3.17.exe), exécutez le logiciel puis suivez les instructions de l'image. Laissez la taille d'unité d'allocation par défaut.", color=discord.Color.blue())
        embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        
        await ctx.send(embed=embed)
    else:
        await ctx.send("Commande non-reconnue. Usage: `.format rufus`")

@bot.command(name='ndsforwarders')
async def ndsforwarders_command(ctx):
    embed = discord.Embed(title="NDS-Forwarders", url="https://wiki.ds-homebrew.com/fr-FR/ds-index/forwarders", description="Création de raccourcis de jeux DS dans le menu HOME", color=discord.Color.blue())
    embed.set_author(name="DS-Homebrew Wiki")
    embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/46971470?s=200&v=4")
    embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
    
    await ctx.send(embed=embed)

@bot.command(name='update')
async def update_command(ctx, attribute: str):
    if attribute.lower() == 'luma':
        embed = discord.Embed(title="Mettre à jour Luma3DS", description="Pour mettre à jour Luma3DS, téléchargez la dernière version de ce dernier avec le lien suivant : [Téléchargement de Luma3DS](https://github.com/Nanquitas/Luma3DS/releases/download/latest/boot.firm), extrayez le `.zip` et copiez tout son contenu (les fichiers `boot.firm` et `boot.3dsx`) à la racine de votre Carte SD.", color=discord.Color.blue())
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/959465064556036220/962401951046307890/IMG_20220409_191905.png")
        embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        
        await ctx.send(embed=embed)
    else:
        await ctx.send("Commande non-reconnue. Usage: `.update luma`")

@bot.command(name='tarifs')
async def tarifs_command(ctx, attribute: str):
    if attribute.lower() == 'pucage':
        embed = discord.Embed(title="Tarifs modification Nintendo Switch (puçage)", url="https://homebrewfrance.github.io/prestations", description="Les tarifs et informations complémentaires sont disponibles sur le site internet, en cas de besoin d'aide, adressez-vous à <@936028537369022474> ou à la société FIXurPHONE au 07.67.76.12.58 (prix d'un appel local)", color=discord.Color.blue())
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/962030917495447613/1058690684711878656/IMG_20221231_111721.png")
        embed.set_footer(text="Le Homebrew France | FIXurPHONE", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        
        await ctx.send(embed=embed)
    else:
        await ctx.send("Commande non-reconnue. Usage: `.tarifs pucage`")

@bot.command(name='guide')
async def guide_command(ctx, attribute: str):
    if attribute.lower() == '3ds':
        embed = discord.Embed(title="Guide de Modding 3DS", url="https://3ds.hacks.guide/fr_FR/", description="Un guide complet pour le custom firmware de la 3DS, depuis le firmware original vers boot9strap.", color=discord.Color.blue())
        embed.set_thumbnail(url="https://lh3.googleusercontent.com/proxy/1P6EQL4b2uEuOudqcTOVXIuddSSk552dDipN7D2A05i9hP3yXsM1Oq6-WRevnj67DBmhw4igm32yIghqrlcRshIQdA9wPEwvz5W7qTRjtVgpAqLRwrmcDblABTobbvwzd7IikURe18ck1mKg")
        embed.set_footer(text="Le Homebrew France | 3DS Hacks Guide", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        await ctx.send(embed=embed)
    elif attribute.lower() == 'vita':
        embed = discord.Embed(title="Guide de Modding PSVita", url="https://vita.hacks.guide/", description="Un guide complet pour le custom firmware PS Vita (TV), depuis le firmware original vers Ensō.", color=discord.Color.blue())
        embed.set_thumbnail(url="https://enso.henkaku.xyz/enso.png")
        embed.set_footer(text="Le Homebrew France | Vita Hacks Guide", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png") 
        await ctx.send(embed=embed)   
    elif attribute.lower() == 'psvita':
        embed = discord.Embed(title="Guide de Modding PSVita", url="https://vita.hacks.guide/", description="Un guide complet pour le custom firmware PS Vita (TV), depuis le firmware original vers Ensō.", color=discord.Color.blue())
        embed.set_thumbnail(url="https://enso.henkaku.xyz/enso.png")
        embed.set_footer(text="Le Homebrew France | Vita Hacks Guide", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        await ctx.send(embed=embed)
    elif attribute.lower() == 'wii u':
        embed = discord.Embed(title="Guide de Modding Wii U", url="https://wiiu.hacks.guide/#/fr_FR/", description="Un guide complet pour le custom firmware de la Wii U, depuis le firmware original vers un CFW.", color=discord.Color.blue())
        embed.set_thumbnail(url="https://lh3.googleusercontent.com/proxy/DEsQosxV9ZMUn1aYjHC93wxMrAhM3Q-EFeOlhHY_r6LZCW16XyWwrcD0j2xTXdx360F0ts91_zU1RZ70aLcqd-VInGimc0SCrr9iJHIyANc7I0ymikR2OgXsnU5VnGiI4hyYqqiSlV4ZiIWSWJoIer0Jotafvnmx0g")
        embed.set_footer(text="Le Homebrew France | Wii U Hacks Guide", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        await ctx.send(embed=embed)
    elif attribute.lower() == 'dsi':
        embed = discord.Embed(title="Guide de Modding DSi", url="https://dsi.cfw.guide/fr_FR/", description="Le guide complet pour modder votre Nintendo DSi.", color=discord.Color.blue())
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/882625509824004199/921361253262323732/1639739970816.png")
        embed.set_footer(text="Le Homebrew France | DSi CFW Guide", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        await ctx.send(embed=embed)
    elif attribute.lower() == 'switch':
        embed = discord.Embed(title="Guide de Modding Nintendo Switch", url="https://homebrewfrance.github.io/docu/switch", description="Un guide complet pour le custom firmware de la Nintendo Switch, depuis le firmware original vers un CFW.", color=discord.Color.blue())
        embed.set_thumbnail(url="https://lh3.googleusercontent.com/proxy/rFesUV6hBrxycXemK2Fs99lNXfFbbztnn0v42yZ51gP8sFK5qvKkxEP2lQFIQIxu0ueBVN_8x2RPxgwCYrS3oGA6_98qtENyP4HVxo4H0h4SaBOKq-l0xmctrXRdcNtThjc6u9EDzNg2WG9aGf38XMpzbWu-IWw")
        embed.set_footer(text="Le Homebrew France | numbersix & Zoria", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        await ctx.send(embed=embed)
    elif attribute.lower() == 'wii':
        embed = discord.Embed(title="Guide de Modding Wii", url="https://wii.guide/fr_FR/", description="Un guide complet pour le custom firmware de la Wii, depuis le firmware original vers un CFW.", color=discord.Color.blue())
        embed.set_footer(text="Le Homebrew France | Wii Guide", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        await ctx.send(embed=embed)
    else:
        await ctx.send("Commande non-reconnue. Usage: `.guide 3ds | dsi | switch | wii | wii u | psvita`")

@bot.command(name='uninstall')
async def uninstall_command(ctx, attribute: str):
    if attribute.lower() == 'luma':
        embed = discord.Embed(title="Désinstaller Luma 3DS", url="https://3ds.hacks.guide/fr_FR/uninstall-cfw.html", description="Un guide complet pour désinstaller intégralement le CFW Luma de votre 3DS.", color=discord.Color.blue())
        embed.set_thumbnail(url="https://lh3.googleusercontent.com/proxy/1P6EQL4b2uEuOudqcTOVXIuddSSk552dDipN7D2A05i9hP3yXsM1Oq6-WRevnj67DBmhw4igm32yIghqrlcRshIQdA9wPEwvz5W7qTRjtVgpAqLRwrmcDblABTobbvwzd7IikURe18ck1mKg")
        embed.set_footer(text="Le Homebrew France | 3DS Hacks Guide", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
    else:
        await ctx.send("Commande non-reconnue. Usage: `.uninstall luma | twl | unlaunch`")

@bot.command()
async def list_servers(ctx):
    server_info = []
    for server in bot.guilds:
        owner = server.owner
        server_info.append(f"Server: {server.name} (ID: {server.id}), Owner: {owner.name} (ID: {owner.id})")

    await ctx.send(f"**Servers and Owners:**\n\n" + "\n".join(server_info))

@bot.command()
async def send_message(ctx, server_id: int, *, message_content: str):
    server = bot.get_guild(server_id)
    if server:
        await server.text_channels[0].send(message_content)
        await ctx.send(f"Message sent to {server.name}!")
    else:
        await ctx.send("Server not found!")


@bot.command()
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
async def stop_bot(ctx):
    await ctx.send("``🔴 ARRÊT...``")
    await ctx.send("``🔴 DECONNEXION DE Le Homebrew France...``")
    await bot.close()

print("Bot is now running...")  # Print bot is running in the console

bot.run('')