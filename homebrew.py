'''
//////////////////////////////////////
////////  LUMIA DISCORD BOT //////////
//// © 2023 - Le Homebrew France /////
//////////////////////////////////////
'''
# Aidez-nous à améliorer le bot sur le repo GitHub ! 
# https://github.com/homebrewfrance/Lumia-Discord-Bot

import discord
from discord.ext import commands
import os
import sys
import configparser

config = configparser.ConfigParser()

config.read('config.ini')

ver = config['BotConfig']['ver']
luma_ver = config['LumaConfig']['luma_ver']
boot9strap_ver = config['B9SConfig']['boot9strap_ver']
skater_ver = config['SkaterConfig']['skater_ver']
nimds_ver = config['NimdsConfig']['nimds_ver']

class Homebrew(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='sdlock', description="Solution en cas de problème de lecture d'une carte SD.")
    async def sdlock_command(self, ctx):
        embed = discord.Embed(title="__**Problème de lecture de Carte SD**__", description="***Comment faire ? :***\nRetirez la protection en écriture comme indiqué ci-dessous. Si le problème de lecture persiste, envisagez à vérifier que votre carte SD n'es pas corrompue.", color=discord.Color.dark_orange())
        embed.set_image(url="https://hbf-files.github.io/sd_lock.jpg")
        embed.set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
        embed.set_author(name="🔎 Résolution des problèmes")
        await ctx.send(embed=embed)

    @commands.command(name='sdroot', description="Montre ce qu'est la racine d'une carte SD.")
    async def sdroot_command(self, ctx):
        embed = discord.Embed(title="__**La racine d'une Carte SD**__", description="***Définition :***\nRéférez-vous à l'image ci-dessous.", color=discord.Color.yellow())
        embed.set_image(url="https://hbf-files.github.io/sd_root.png")
        embed.set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
        embed.set_author(name="💡 Aide")
        await ctx.send(embed=embed)

    @commands.command(name='config', description="Indique les options à sélectionner pour la configuration de Luma3DS.")
    async def config_command(self, ctx, option: str):
        if option.lower() == 'luma':
            embed = discord.Embed(title="__**Configuration de Luma**__", description="***Comment faire ? :***\nSélectionnez les options cochées comme sur la photo :", color=discord.Color.yellow())
            embed.set_image(url="https://hbf-files.github.io/luma_config.png")
            embed.set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
            embed.set_author(name="💡 Aide")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Commande non-reconnue. Usage: `.config luma`")

    @commands.command(name='skater', description="Résolution des erreurs liées à Browserhax (super-skaterhax)")
    async def skater(self, ctx):
        """Guide de résolution des erreurs avec super-skaterhax (browserhax)"""
        embed = discord.Embed(title="__**Messages d'erreur lors de l'éxecution de Browserhax**__", description="***Comment faire ?***\nVérifiez les possibilités suivantes :\n\n- Votre console est-elle à la date correcte ?\n- Avez-vous tous les fichiers nécessaires ? (``arm11code.bin``,  ``browserhax_hblauncher_ropbin_payload.bin``, ``boot.3dsx``) à la racine de votre carte SD ?\n- Avez-vous réinitialisé les paramètres du navigateur ? (menu du navigateur -> Paramètres -> Réinitialiser les données de sauvegarde)\n- Avez-vous séélectionné le bon payload pour votre région ET votre version du système ?\n- Vos paramètres régionaux ont-ils été réglés correctement comme sur cette image :", color=discord.Color.dark_orange())
        embed.set_image(url="https://hbf-files.github.io/skater_lang.png")
        embed.set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
        embed.set_author(name="🔎 Résolution des problèmes")
        await ctx.send(embed=embed)

    @commands.command(name='non-brick')
    async def non_brick_command(self, ctx):
        """Ouh pinaise"""
        embed = discord.Embed(title="__**La LED s'allume puis s'éteint immédiatement**__", description=f"***Comment faire ? :***\nSi la LED bleue de votre 3DS s'allume puis s'éteint instantanément, non votre console n'est pas brickée. Il s'agit simplement d'un fichier manquant sur votre Carte SD : le `boot.firm`, il est disponible en téléchargement ici, placez le à la racine de votre Carte SD.\n- [Télécharger le boot.firm](https://github.com/LumaTeam/Luma3DS/releases/latest/download/Luma3DSv{luma_ver}.zip)", color=discord.Color.dark_orange())
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/959465064556036220/962404229983662100/IMG_20220409_193009.png")
        embed.set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
        embed.set_author(name="🔎 Résolution des problèmes")
        await ctx.send(embed=embed)

    @commands.command(name='widescreen')
    async def widescreen_command(self, ctx):
        embed = discord.Embed(title="Mode plein écran (TWiLightMenu++)", url="https://wiki.ds-homebrew.com/fr-FR/twilightmenu/playing-in-widescreen", description="Utilisation du mode plein d'écran sur le TWiLightMenu++", color=discord.Color.blue())
        embed.set_author(name="DS-Homebrew Wiki")
        embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/46971470?s=200&v=4")
        embed.set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
        await ctx.send(embed=embed)

    @commands.command(name='boxart')
    async def boxart_command(self, ctx):
        embed = discord.Embed(title="Obtenir des box art (Jaquettes de jeux) (TWiLightMenu++)", url="https://wiki.ds-homebrew.com/fr-FR/twilightmenu/how-to-get-box-art", description="Comment ajouter des box art sur le TWiLightMenu++", color=discord.Color.blue())
        embed.set_author(name="DS-Homebrew Wiki")
        embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/46971470?s=200&v=4")
        embed.set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
        await ctx.send(embed=embed)


    @commands.command(name='skins')
    async def skins_command(self, ctx, attribute: str):
        if attribute.lower() == 'twl':
            embed = discord.Embed(title="Thèmes (Skins) (TWiLightMenu++)", url="https://skins.ds-homebrew.com/", description="Une collection de thèmes pour le TWiLightMenu++ de DS-Homebrew/twlmenu-extras sur GitHub", color=discord.Color.blue())
            embed.set_author(name="DS-Homebrew Wiki")
            embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/46971470?s=200&v=4")
            embed.set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Commande non-reconnue. Usage: `.skins twl`")

    @commands.command(name='compat')
    async def compat(self, ctx, attribute: str):
        if attribute.lower() == 'ps2':
            embed = discord.Embed(title="Compatibilité FreeDVDBoot", description="Vérifiez la compatibilité de votre PS2 avec l'exploit FreeDVDBoot  avec le tableau suivant :", color=discord.Color.blue())
            embed.set_image(url="https://hbf-files.github.io/compatibilite_ps2.png")
            embed.set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
            await ctx.send(embed=embed)
        elif attribute.lower() == 'ntrboot':
            embed = discord.Embed(title="Compatibilité NTRBOOT", description="Vérifiez la compatibilité de votre R4 avec NTRBOOTHAX, les modèles compatibles sont les suivants :", color=discord.Color.blue())
            embed.set_image(url="https://hbf-files.github.io/ntrboot-flashcarts.png")
            embed.set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Commande non-reconnue. Usage: `.compatibility ps2 | ntrboot`")
                        

    @commands.command(name='format')
    async def format(self, ctx, attribute: str, logiciel: str):
        if attribute.lower() == 'fat32' or attribute.lower() == 'FAT32' or attribute.lower() == 'FAT' or attribute.lower() == 'fat':
            if logiciel.lower() == 'rufus':
                embed = discord.Embed(title=f"Formatage en FAT32 via Rufus", description="Téléchargez la dernière version de Rufus, lancez le logiciel et faites comme indiqué sur l'image.\n- [Télécharger Rufus](https://github.com/pbatard/rufus/releases/download/v4.2/rufus-4.2.exe)", color=discord.Color.blue())
                embed.set_image(url="https://media.discordapp.net/attachments/960942679473135686/962666707711840306/unknown.png")
                embed.set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
                await ctx.send(embed=embed)
            else:
                await ctx.send("Invalide")
        else:
            await ctx.send("Commande non-reconnue. Usage: `.format rufus`")

    @commands.command(name='ndsforwarders')
    async def ndsforwarders_command(self, ctx):
        embed = discord.Embed(title="NDS-Forwarders", url="https://wiki.ds-homebrew.com/fr-FR/ds-index/forwarders", description="Création de raccourcis de jeux DS dans le menu HOME", color=discord.Color.blue())
        embed.set_author(name="DS-Homebrew Wiki")
        embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/46971470?s=200&v=4")
        embed.set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
        await ctx.send(embed=embed)

    @commands.command(name='update')
    async def update_command(self, ctx, attribute: str):
        if attribute.lower() == 'luma':
            embed = discord.Embed(title="__**Mise à jour de Luma3DS**__", description=f"***Comment faire ? - Méthode 1 :***\nPour mettre à jour Luma3DS, téléchargez la dernière version de Luma, extrayez le `.zip` et copiez tout son contenu (les fichiers `boot.firm` et `boot.3dsx`) à la racine de votre Carte SD.\n\n***Méthode 2 :***\nRendez vous dans l'application Universal-Updater (une icône de flèche bleue), cliquez sur la zone de recherche, cherchez 'luma', téléchargez la première entrée. Si vous n'avez pas Universal-Updater sur vôtre console, il suffit de télécharger le `.cia` et de l'installer via FBI.\n\n- [Télécharger Luma3DS](https://github.com/LumaTeam/Luma3DS/releases/latest/download/Luma3DSv{luma_ver}.zip)\n- [Télécharger Universal-Updater](https://github.com/Universal-Team/Universal-Updater/releases/latest/download/Universal-Updater.cia)", color=discord.Color.yellow())
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/959465064556036220/962401951046307890/IMG_20220409_191905.png")
            embed.set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
            embed.set_author(name="💡 Aide")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Commande non-reconnue. Usage: `.update luma`")

    @commands.command(name='fixurphone')
    async def fixurphone(self, ctx):
        embed = discord.Embed(title="__**FIXurPHONE**__", url="https://www.fixurphone.fr/", description="Notre partenaire FIXurPHONE vous propose un service de puçage de consoles, notamment la Nintendo Switch. Bénéficiez d'une réduction sur les prix en mentionnant que vous venez du serveur Discord Homebrew France.\n***Tarifs (-25% par rapport aux prix d'origine) :***\n- Nintendo Switch v1 et v2 : Installation d'un module Picofly (RP2040) : ``149€``\n- Nintendo Switch Lite : Installation d'un module Picofly (RP2040) : ``149€``\n- Nintendo Switch OLED : Installation d'un module Picofly (RP2040) : ``189€``\n\n***Le tarif comprend :***\n- La pose du modchip\n- Une microSD de 256GB préconfigurée\n- Création d'une emuNAND et sa configuration\n- Les derniers Homebrews à jour\n- Un pack personnalisé\n- Un tutoriel d'utilisation et d'installation\n\nLa console est garantie 1 an après intervention\nLa puce est garantie à vie\nLes frais de retour sont offerts\n\n***Contacter FIXurPHONE :***\n07.67.76.12.58 (prix d'un appel local)\ncontact@fixurphone.fr\n7 Boulevard Armand Audibert\n13220 Châteauneuf-les-Martigues", color=discord.Color.red())
        embed.set_thumbnail(url="https://homebrewfrance.github.io/IMAGES/fixurphone.png")
        embed.set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
        await ctx.send(embed=embed)

    @commands.command(name='guide')
    async def guide_command(self, ctx, attribute: str = None):

        if attribute is None:
            embed = discord.Embed(title="Liste des guides disponibles", description="Une liste complètes des guides disponibles.", color=discord.Color.blue()).add_field(name="", value="Guide 3DS (``.guide 3ds``) : https://3ds.hacks.guide/fr-FR/\nGuide DSi (``.guide dsi``) : https://dsi.cfw.guide/fr_FR/\nGuide Wii (``.guide wii``) : https://wii.guide/fr_FR/\nGuide Wii U (``.guide wiiu``) : https://wiiu.hacks.guide/#/fr_FR/\nGuide Switch (``.guide switch``) : https://homebrewfrance.github.io/docu.switch\nGuide PSVita (``.guide psvita``) : https://vita.hacks.guide/\nGuide PSP (``.guide psp``) : https://www.pspunk.com/psp-cfw/\nGuide PS2 (``.guide ps2``) : https://lecrabeinfo.net/ps2-freemcboot-fmcb.html\nGuide PS3 (CFW)(``.guide ps3cfw``) : https://youtu.be/2FrVvZY_qMo\nGuide PS3 (HEN)(``.guide ps3hen``) : https://youtu.be/LLmyzdS-5wY\nGuide PS4 (``.guide ps4``) : https://youtu.be/PAWNe2bi_PU")
            embed.set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
            await ctx.send(embed=embed)
    
        if attribute.lower() == '3ds':
            embed = discord.Embed(title="__**Guide de Modding 3DS**__", url="https://3ds.hacks.guide/fr_FR/", description="Un guide complet pour le custom firmware de la 3DS, depuis le firmware original vers boot9strap.", color=discord.Color.blue())
            embed.set_footer(text=f"Lumia {ver} | NH & Plailect", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
            embed.set_thumbnail(url="https://hbf-files.github.io/nhplai.png")
            embed.set_author(name="📚 Guide")
            await ctx.send(embed=embed)

        elif attribute.lower() == 'vita' or attribute.lower() == "psvita" or attribute.lower() == "pstv":
            embed = discord.Embed(title="Guide de Modding PSVita", url="https://vita.hacks.guide/", description="Un guide complet pour le custom firmware PS Vita (TV), depuis le firmware original vers un CFW.", color=discord.Color.blue())
            embed.set_footer(text=f"Lumia {ver} | emiyl", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true") 
            embed.set_thumbnail(url="https://hbf-files.github.io/emiyl.jpg")
            embed.set_author(name="📚 Guide")
            await ctx.send(embed=embed)   

        elif attribute.lower() == 'wiiu':
            embed = discord.Embed(title="Guide de Modding Wii U", url="https://wiiu.hacks.guide/#/fr_FR/", description="Un guide complet pour le custom firmware de la Wii U, depuis le firmware original vers un CFW.", color=discord.Color.blue())
            embed.set_footer(text=f"Lumia {ver} | Nintendo-Homebrew", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
            embed.set_thumbnail(url="https://hbf-files.github.io/NH.png")
            embed.set_author(name="📚 Guide")
            await ctx.send(embed=embed)

        elif attribute.lower() == 'dsi':
            embed = discord.Embed(title="Guide de Modding DSi", url="https://dsi.cfw.guide/fr_FR/", description="Le guide complet pour modder votre Nintendo DSi.", color=discord.Color.blue())
            embed.set_footer(text=f"Lumia {ver} | DS-Homebrew & emiyl", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
            embed.set_thumbnail(url="https://hbf-files.github.io/ds-homebrew_emiyl.png")
            embed.set_author(name="📚 Guide")
            await ctx.send(embed=embed)

        elif attribute.lower() == 'switch':
            embed = discord.Embed(title="Guide de Modding Nintendo Switch", url="https://homebrewfrance.github.io/docu/switch", description="Un guide complet pour le custom firmware de la Nintendo Switch, depuis le firmware original vers Atmosphère.", color=discord.Color.blue())
            embed.set_footer(text=f"Lumia {ver} | numbersix & Zoria", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
            embed.set_thumbnail(url="https://hbf-files.github.io/nbzoria.png")
            embed.set_author(name="📚 Guide")
            await ctx.send(embed=embed)

        elif attribute.lower() == 'wii':
            embed = discord.Embed(title="Guide de Modding Wii", url="https://wii.guide/fr_FR/", description="Un guide complet pour le custom firmware de la Wii, depuis le firmware original vers un CFW.", color=discord.Color.blue())
            embed.set_footer(text=f"Lumia {ver} | RiiConnect24", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
            embed.set_thumbnail(url="https://hbf-files.github.io/riiconnect24.png")
            embed.set_author(name="📚 Guide")
            await ctx.send(embed=embed)

        elif attribute.lower() == 'psp':
            embed = discord.Embed(title="Guide de Modding PSP", url="https://www.pspunk.com/psp-cfw/", description="Un guide complet pour le custom firmware de la PSP, depuis le firmware original vers un CFW.", color=discord.Color.blue())
            embed.set_footer(text=f"Lumia {ver} | PSPunk", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
            embed.set_author(name="📚 Guide")
            await ctx.send(embed=embed)

        else:
            await ctx.send("Commande non-reconnue. Usage: `.guide 3ds | dsi | switch | wii | wii u | psvita | psp`")

    @commands.command(name='uninstall')
    async def uninstall_command(self, ctx, attribute: str):
        if attribute.lower() == 'luma':
            embed = discord.Embed(title="Désinstaller Luma 3DS", url="https://3ds.hacks.guide/fr_FR/uninstall-cfw.html", description="Un guide complet pour désinstaller intégralement le CFW Luma de votre 3DS.", color=discord.Color.blue())
            embed.set_thumbnail(url="https://lh3.googleusercontent.com/proxy/1P6EQL4b2uEuOudqcTOVXIuddSSk552dDipN7D2A05i9hP3yXsM1Oq6-WRevnj67DBmhw4igm32yIghqrlcRshIQdA9wPEwvz5W7qTRjtVgpAqLRwrmcDblABTobbvwzd7IikURe18ck1mKg")
            embed.set_footer(text=f"Lumia {ver} | 3DS Hacks Guide", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
        else:
            await ctx.send("Commande non-reconnue. Usage: `.uninstall luma | twl | unlaunch`")

async def setup(bot):
    await bot.add_cog(Homebrew(bot))
