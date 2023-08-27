import discord
from discord.ext import commands
import os
import sys

class Homebrew(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='sdlock')
    async def sdlock_command(self, ctx):
        embed = discord.Embed(title="Problème de lecture de Carte SD :", description="Retirer la protection en écriture comme indiqué", color=discord.Color.blue())
        embed.set_image(url="https://hbf-files.github.io/sd_lock.jpg")
        embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        await ctx.send(embed=embed)

    @commands.command(name='sdroot')
    async def sdroot_command(self, ctx):
        embed = discord.Embed(title="La racine d'une Carte SD :", color=discord.Color.blue())
        embed.set_image(url="https://hbf-files.github.io/sd_root.png")
        embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        await ctx.send(embed=embed)

    @commands.command(name='config')
    async def config_command(self, ctx, option: str):
        if option.lower() == 'luma':
            embed = discord.Embed(title="Aide à la configuration de Luma :", description="Sélectionner les options cochées comme sur la photo :", color=discord.Color.blue())
            embed.set_image(url="https://hbf-files.github.io/luma_config.png")
            embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Commande non-reconnue. Usage: `.config luma`")

    @commands.command(name='skater')
    async def skater_command(self, ctx):
        """Guide de résolution des erreurs avec super-skaterhax (browserhax)"""
        embed = discord.Embed(title="Résolution des problèmes liés à super-skaterhax", description="- Votre console est-elle à la date correcte ?\n- Avez-vous tous les fichiers nécessaires ? (``arm11code.bin``,  ``browserhax_hblauncher_ropbin_payload.bin``, ``boot.3dsx``) à la racine de votre carte SD ?\n- Avez-vous réinitialisé les paramètres du navigateur ? (menu du navigateur -> Paramètres -> Réinitialiser les données de sauvegarde)\n- Avez-vous séélectionné le bon payload pour votre région ET votre version du système ?\n- Vos paramètres régionaux ont-ils été réglés correctement comme sur cette image :", color=discord.Color.blue())
        embed.set_image(url="https://hbf-files.github.io/skater_lang.png")
        embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        await ctx.send(embed=embed)

    @commands.command(name='non-brick')
    async def non_brick_command(self, ctx):
        """Ouh pinaise"""
        embed = discord.Embed(title="Ma console est-elle brickée ?", description="Si la LED bleue de votre 3DS s'allume puis s'éteint instantanément, non votre console n'est pas brickée. Il s'agit simplement d'un fichier manquant sur votre Carte SD : le `boot.firm`, il est disponible en téléchargement ici, placez le à la racine de votre Carte SD : [Téléchargement du boot.firm](https://github.com/LumaTeam/Luma3DS/releases/latest/download/Luma3DSv13.0.2.zip)", color=discord.Color.blue())
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/959465064556036220/962404229983662100/IMG_20220409_193009.png")
        embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        await ctx.send(embed=embed)

    @commands.command(name='widescreen')
    async def widescreen_command(self, ctx):
        embed = discord.Embed(title="Mode plein écran (TWiLightMenu++)", url="https://wiki.ds-homebrew.com/fr-FR/twilightmenu/playing-in-widescreen", description="Utilisation du mode plein d'écran sur le TWiLightMenu++", color=discord.Color.blue())
        embed.set_author(name="DS-Homebrew Wiki")
        embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/46971470?s=200&v=4")
        embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        await ctx.send(embed=embed)

    @commands.command(name='boxart')
    async def boxart_command(self, ctx):
        embed = discord.Embed(title="Obtenir des box art (Jaquettes de jeux) (TWiLightMenu++)", url="https://wiki.ds-homebrew.com/fr-FR/twilightmenu/how-to-get-box-art", description="Comment ajouter des box art sur le TWiLightMenu++", color=discord.Color.blue())
        embed.set_author(name="DS-Homebrew Wiki")
        embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/46971470?s=200&v=4")
        embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        await ctx.send(embed=embed)


    @commands.command(name='skins')
    async def skins_command(self, ctx, attribute: str):
        if attribute.lower() == 'twl':
            embed = discord.Embed(title="Thèmes (Skins) (TWiLightMenu++)", url="https://skins.ds-homebrew.com/", description="Une collection de thèmes pour le TWiLightMenu++ de DS-Homebrew/twlmenu-extras sur GitHub", color=discord.Color.blue())
            embed.set_author(name="DS-Homebrew Wiki")
            embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/46971470?s=200&v=4")
            embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Commande non-reconnue. Usage: `.skins twl`")

    @commands.command(name='compat')
    async def compat_command(self, ctx, attribute: str):
        if attribute.lower() == 'ps2':
            embed = discord.Embed(title="Compatibilité FreeDVDBoot", description="Vérifiez la compatibilité de votre PS2 avec l'exploit FreeDVDBoot  avec le tableau suivant :", color=discord.Color.blue())
            embed.set_image(url="https://hbf-files.github.io/compatibilite_ps2.png")
            embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
            await ctx.send(embed=embed)
        elif attribute.lower() == 'ntrboot':
            embed = discord.Embed(title="Compatibilité NTRBOOT", description="Vérifiez la compatibilité de votre R4 avec NTRBOOTHAX, les modèles compatibles sont les suivants :", color=discord.Color.blue())
            embed.set_image(url="https://hbf-files.github.io/ntrboot-flashcarts.png")
            embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Commande non-reconnue. Usage: `.compatibility ps2 | ntrboot`")
                        

    @commands.command(name='format')
    async def format_command(self, ctx, attribute: str):
        if attribute.lower() == 'rufus':
            embed = discord.Embed(title="Formatage en FAT32 (Rufus) :", image="https://media.discordapp.net/attachments/960942679473135686/962666707711840306/unknown.png", description="Téléchargez Rufus : [Téléchargement de Rufus](https://github.com/pbatard/rufus/releases/download/v3.17/rufus-3.17.exe), exécutez le logiciel puis suivez les instructions de l'image. Laissez la taille d'unité d'allocation par défaut.", color=discord.Color.blue())
            embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Commande non-reconnue. Usage: `.format rufus`")

    @commands.command(name='ndsforwarders')
    async def ndsforwarders_command(self, ctx):
        embed = discord.Embed(title="NDS-Forwarders", url="https://wiki.ds-homebrew.com/fr-FR/ds-index/forwarders", description="Création de raccourcis de jeux DS dans le menu HOME", color=discord.Color.blue())
        embed.set_author(name="DS-Homebrew Wiki")
        embed.set_thumbnail(url="https://avatars.githubusercontent.com/u/46971470?s=200&v=4")
        embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        await ctx.send(embed=embed)

    @commands.command(name='update')
    async def update_command(self, ctx, attribute: str):
        if attribute.lower() == 'luma':
            embed = discord.Embed(title="Mettre à jour Luma3DS", description="Pour mettre à jour Luma3DS, téléchargez la dernière version de ce dernier avec le lien suivant : [Téléchargement de Luma3DS](https://github.com/LumaTeam/Luma3DS/releases/latest/download/Luma3DSv13.0.2.zip), extrayez le `.zip` et copiez tout son contenu (les fichiers `boot.firm` et `boot.3dsx`) à la racine de votre Carte SD.", color=discord.Color.blue())
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/959465064556036220/962401951046307890/IMG_20220409_191905.png")
            embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Commande non-reconnue. Usage: `.update luma`")

    @commands.command(name='tarifs')
    async def tarifs_command(self, ctx, attribute: str):
        if attribute.lower() == 'pucage':
            embed = discord.Embed(title="Tarifs modification Nintendo Switch (puçage)", url="https://homebrewfrance.github.io/prestations", description="Les tarifs et informations complémentaires sont disponibles sur le site internet, en cas de besoin d'aide, adressez-vous à <@936028537369022474> ou à la société FIXurPHONE au 07.67.76.12.58 (prix d'un appel local)", color=discord.Color.blue())
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/962030917495447613/1058690684711878656/IMG_20221231_111721.png")
            embed.set_footer(text="Le Homebrew France | FIXurPHONE", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Commande non-reconnue. Usage: `.tarifs pucage`")

    @commands.command(name='guide')
    async def guide_command(self, ctx, attribute: str = None):

        if attribute is None:
            embed = discord.Embed(title="Liste des guides disponibles", description="Une liste complètes des guides disponibles.", color=discord.Color.blue()).add_field(name="", value="Guide 3DS (``.guide 3ds``) : https://3ds.hacks.guide/fr-FR/\nGuide DSi (``.guide dsi``) : https://dsi.cfw.guide/fr_FR/\nGuide Wii (``.guide wii``) : https://wii.guide/fr_FR/\nGuide Wii U (``.guide wiiu``) : https://wiiu.hacks.guide/#/fr_FR/\nGuide Switch (``.guide switch``) : https://homebrewfrance.github.io/docu.switch\nGuide PSVita (``.guide psvita``) : https://vita.hacks.guide/\nGuide PSP (``.guide psp``) : https://www.pspunk.com/psp-cfw/\nGuide PS2 (``.guide ps2``) : https://lecrabeinfo.net/ps2-freemcboot-fmcb.html\nGuide PS3 (CFW)(``.guide ps3cfw``) : https://youtu.be/2FrVvZY_qMo\nGuide PS3 (HEN)(``.guide ps3hen``) : https://youtu.be/LLmyzdS-5wY\nGuide PS4 (``.guide ps4``) : https://youtu.be/PAWNe2bi_PU")
            embed.set_footer(text="Le Homebrew France", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
            await ctx.send(embed=embed)
    
        if attribute.lower() == '3ds':
            embed = discord.Embed(title="Guide de Modding 3DS", url="https://3ds.hacks.guide/fr_FR/", description="Un guide complet pour le custom firmware de la 3DS, depuis le firmware original vers boot9strap.", color=discord.Color.blue())
            embed.set_thumbnail(url="https://hbf-files.github.io/nhplai.png")
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

    @commands.command(name='uninstall')
    async def uninstall_command(self, ctx, attribute: str):
        if attribute.lower() == 'luma':
            embed = discord.Embed(title="Désinstaller Luma 3DS", url="https://3ds.hacks.guide/fr_FR/uninstall-cfw.html", description="Un guide complet pour désinstaller intégralement le CFW Luma de votre 3DS.", color=discord.Color.blue())
            embed.set_thumbnail(url="https://lh3.googleusercontent.com/proxy/1P6EQL4b2uEuOudqcTOVXIuddSSk552dDipN7D2A05i9hP3yXsM1Oq6-WRevnj67DBmhw4igm32yIghqrlcRshIQdA9wPEwvz5W7qTRjtVgpAqLRwrmcDblABTobbvwzd7IikURe18ck1mKg")
            embed.set_footer(text="Le Homebrew France | 3DS Hacks Guide", icon_url="https://raw.githubusercontent.com/homebrewfrance/homebrewfrance.github.io/main/IMAGES/favicon.png")
        else:
            await ctx.send("Commande non-reconnue. Usage: `.uninstall luma | twl | unlaunch`")

async def setup(bot):
    await bot.add_cog(Homebrew(bot))