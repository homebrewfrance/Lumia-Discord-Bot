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

ver = "v0.0.2a"

class SerialChecker(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='imsp')
    async def imsp(self, ctx, serial_number: str = None):
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
                embed.add_field(name="__**Compatibilité**__", value="``🟢 Acceptée``").add_field(name="__**Détails**__", value="Votre console n'est pas patchée, elle est donc compatible avec la faille RCM.\n \nVous pouvez commencer le guide dès maintenant en cliquant [ici](https://homebrewfrance.github.io/docu/switch).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
            elif 10074000000 <= num <= 10120000000:
                embed.add_field(name="__**Compatibilité**__", value="``🟠 Rejetée``").add_field(name="__**Détails**__", value="Votre console est peut-être patchée, elle devrait être compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
            elif 10120000000 >= num >= 40000000000:
                embed.add_field(name="__**Compatibilité**__", value="``🔴 Rejetée``").add_field(name="__**Détails**__", value="Votre console est patchée, elle n'est donc pas compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
            elif 40000000000 <= num <= 40011000000:
                embed.add_field(name="__**Compatibilité**__", value="``🟢 Acceptée``").add_field(name="__**Détails**__", value="Votre console n'est pas patchée, elle est donc compatible avec la faille RCM.\n \nVous pouvez commencer le guide dès maintenant en cliquant [ici](https://homebrewfrance.github.io/docu/switch).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
            elif 40011000000 <= num <= 40012000000:
                embed.add_field(name="__**Compatibilité**__", value="``🟠 Rejetée``").add_field(name="__**Détails**__", value="Votre console est peut-être patchée, elle devrait être compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
            elif 40012000000 >= num >= 70000000000:
                embed.add_field(name="__**Compatibilité**__", value="``🔴 Rejetée``").add_field(name="__**Détails**__", value="Votre console est patchée, elle n'est donc pas compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
            elif 70000000000 <= num <= 70017800000:
                embed.add_field(name="__**Compatibilité**__", value="``🟢 Acceptée``").add_field(name="__**Détails**__", value="Votre console n'est pas patchée, elle est donc compatible avec la faille RCM.\n \nVous pouvez commencer le guide dès maintenant en cliquant [ici](https://homebrewfrance.github.io/docu/switch).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
            elif 70017800000 <= num <= 70030000000:
                embed.add_field(name="__**Compatibilité**__", value="``🟠 Rejetée``").add_field(name="__**Détails**__", value="Votre console est peut-être patchée, elle devrait être compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
            elif 70030000000 >= num >= 99999999999 :
                embed.add_field(name="__**Compatibilité**__", value="``🔴 Rejetée``").add_field(name="__**Détails**__", value="Votre console est patchée, elle n'est donc pas compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
        elif prefix == "XAJ":
            if 10000000000 <= num <= 10020000000:
                embed.add_field(name="__**Compatibilité**__", value="``🟢 Acceptée``").add_field(name="__**Détails**__", value="Votre console n'est pas patchée, elle est donc compatible avec la faille RCM.\n \nVous pouvez commencer le guide dès maintenant en cliquant [ici](https://homebrewfrance.github.io/docu/switch).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
            elif 10020000000 <= num <= 10030000000:
                embed.add_field(name="__**Compatibilité**__", value="``🟠 Rejetée``").add_field(name="__**Détails**__", value="Votre console est peut-être patchée, elle devrait être compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
            elif 10030000000 >= num >= 40000000000 :
                embed.add_field(name="__**Compatibilité**__", value="``🔴 Rejetée``").add_field(name="__**Détails**__", value="Votre console est patchée, elle n'est donc pas compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
            elif 40000000000 <= num <= 40046000000:
                embed.add_field(name="__**Compatibilité**__", value="``🟢 Acceptée``").add_field(name="__**Détails**__", value="Votre console n'est pas patchée, elle est donc compatible avec la faille RCM.\n \nVous pouvez commencer le guide dès maintenant en cliquant [ici](https://homebrewfrance.github.io/docu/switch).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
            elif 40046000000 <= num <= 40060000000:
                embed.add_field(name="__**Compatibilité**__", value="``🟠 Rejetée``").add_field(name="__**Détails**__", value="Votre console est peut-être patchée, elle devrait être compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
            elif 40060000000 >= num >= 70000000000:
                embed.add_field(name="__**Compatibilité**__", value="``🔴 Rejetée``").add_field(name="__**Détails**__", value="Votre console est patchée, elle n'est donc pas compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
            elif 70000000000 <= num <= 70040000000:
                embed.add_field(name="__**Compatibilité**__", value="``🟢 Acceptée``").add_field(name="__**Détails**__", value="Votre console n'est pas patchée, elle est donc compatible avec la faille RCM.\n \nVous pouvez commencer le guide dès maintenant en cliquant [ici](https://homebrewfrance.github.io/docu/switch).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
            elif 70040000000 <= num <= 70050000000:
                embed.add_field(name="__**Compatibilité**__", value="``🟠 Rejetée``").add_field(name="__**Détails**__", value="Votre console est peut-être patchée, elle devrait être compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).") .set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
            elif 70050000000 >= num >= 99999999999:
                embed.add_field(name="__**Compatibilité**__", value="``🔴 Rejetée``").add_field(name="__**Détails**__", value="Votre console est patchée, elle n'est donc pas compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
        elif prefix == "XKW" or prefix == "XKJ" or prefix == "XWW":
            if num >= 10000000000:
                embed.add_field(name="__**Compatibilité**__", value="``🔴 Rejetée``").add_field(name="__**Détails**__", value="Votre console est patchée, elle n'est donc pas compatible avec la faille RCM.\n \nVotre console nécessite l'installation d'une puce pour bénéficier d'Atmosphère, un service de puçage de console est disponible [ici](https://homebrewfrance.github.io/prestations).").set_footer(text=f"Lumia {ver} | NS Serial Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
        else:
            embed = discord.Embed(description="Veuillez entrer un numéro de série valide.", color=discord.Color.red())
            await ctx.send(embed=embed)
            return


        await ctx.send(embed=embed)

    @commands.command(name='ps3compat')
    async def ps3compat(self, ctx, model_number: str = None):
        if model_number is None or len(model_number) < 7:
            embed = discord.Embed(description="Veuillez entrer un numéro de série valide (au moins 7 caractères).", color=discord.Color.red())
            await ctx.send(embed=embed)
            return
    
        title = "Compatibilité PS3 CFW/HEN"
        embed = discord.Embed(title=title, description=f"Numéro de modèle : {model_number}", color=discord.Color.blue())
    
        if len(model_number) <= 7:
            embed.add_field(name="__**Compatibilité**__", value="``🟢 Acceptée``").add_field(name="__**Détails**__", value="Votre console est compatible CFW et HEN.").add_field(name="__**Hack recommandé**__", value="Installation du CFW").set_footer(text=f"Lumia {ver} | PS3-Compat Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")

        elif len(model_number) == 10:
            prefix_cech = model_number[:7]

            if prefix_cech == "CECH-20" or prefix_cech == "CECH-21" or prefix_cech == "CECH-25":
                embed.add_field(name="__**Compatibilité**__", value="``🟢 Acceptée``").add_field(name="__**Détails**__", value="Votre console est compatible CFW et HEN.").add_field(name="__**Hack recommandé**__", value="Installation du CFW").set_footer(text=f"Lumia {ver} | PS3-Compat Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")            
            elif prefix_cech == "CECH-30" or prefix_cech == "CECH-40" or prefix_cech == "CECH-42" or prefix_cech == "CECH-43":
                embed.add_field(name="__**Compatibilité**__", value="``🟠 Acceptée``", inline=False).add_field(name="__**Détails**__", value="Votre console est incompatible CFW mais est compatible avec le HEN.").add_field(name="__**Hack recommandé**__", value="Installation du HEN").set_footer(text=f"Lumia {ver} | PS3-Compat Checker", icon_url="https://homebrewfrance.github.io/IMAGES/lumia_bot.png")
            else:
                embed = discord.Embed(description="Invalide")

        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(SerialChecker(bot))

                        