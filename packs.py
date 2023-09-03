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
import asyncio
import urllib.request
import zipfile
import requests
import shutil
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

ver = config['BotConfig']['ver']
luma_ver = config['LumaConfig']['luma_ver']
boot9strap_ver = config['B9SConfig']['boot9strap_ver']
skater_ver = config['SkaterConfig']['skater_ver']
nimds_ver = config['NimdsConfig']['nimds_ver']

class Packs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def construct_pack(self, ctx, console: str, exploit: str):
        if console == "3ds" and (exploit == "ntrboothax" or exploit == "r4" or exploit == "ntrboot" or exploit == "ntr"):
            embed_initial = discord.Embed(
                title="Construction du pack en cours",
                description="Veuillez patienter...\nCela ne prendra que quelques secondes.",
                color=discord.Color.orange()).set_thumbnail(url="https://homebrewfrance.github.io/IMAGES/redirection.gif").set_footer(text="Pack demandé : NTRBOOTHAX")
            initial_message = await ctx.send(embed=embed_initial)
        
            urllib.request.urlretrieve("https://github.com/LumaTeam/Luma3DS/releases/latest/download/Luma3DSv13.0.2.zip", f"Luma3DSv{luma_ver}.zip")
            urllib.request.urlretrieve("https://github.com/cooolgamer/FBI-Reloaded-FR/releases/latest/download/FBI-FR.3dsx", "FBI-FR.3dsx")
            urllib.request.urlretrieve("https://github.com/cooolgamer/FBI-Reloaded-FR/releases/latest/download/FBI-FR.cia", "FBI-FR.cia")        
            urllib.request.urlretrieve("https://github.com/cooolgamer/Anemone3DS-FR/releases/latest/download/Anemone3DSFR.cia", "Anemone3DSFR.cia")
            urllib.request.urlretrieve("https://github.com/BernardoGiordano/Checkpoint/releases/tag/v3.7.4", "Checkpoint.cia")
            urllib.request.urlretrieve("https://github.com/PabloMK7/homebrew_launcher_dummy/releases/latest/download/Homebrew_Launcher.cia", "Homebrew_Launcher.cia")
            urllib.request.urlretrieve("https://github.com/Universal-Team/Universal-Updater/releases/latest/download/Universal-Updater.cia", "Universal-Updater.cia")
            urllib.request.urlretrieve("https://github.com/d0k3/GodMode9/releases/latest/download/GodMode9-v2.1.1-20220322194259.zip", "GodMode9-v2.1.1-20220322194259.zip")
            urllib.request.urlretrieve("https://github.com/d0k3/SafeB9SInstaller/releases/download/v0.0.7/SafeB9SInstaller-20170605-122940.zip", "SafeB9SInstaller-20170605-122940.zip")      
            urllib.request.urlretrieve("https://github.com/SciresM/boot9strap/releases/latest/download/boot9strap-1.4.zip", f"boot9strap-{boot9strap_ver}.zip")
            urllib.request.urlretrieve("https://github.com/ntrteam/ntrboot_flasher/releases/latest/download/ntrboot_flasher.firm", "ntrboot_flasher.firm")

            with zipfile.ZipFile("GodMode9-v2.1.1-20220322194259.zip", "r") as gm9_zip:
                gm9_zip.extractall()

            with zipfile.ZipFile("SafeB9SInstaller-20170605-122940.zip", "r") as sb9s_zip:
                sb9s_zip.extractall()

            with zipfile.ZipFile(f"boot9strap-{boot9strap_ver}.zip", "r") as b9s_zip:
                b9s_zip.extractall()

            with zipfile.ZipFile(f"Luma3DSv{luma_ver}.zip", "r") as luma_zip:
                luma_zip.extractall()

            with zipfile.ZipFile("LumiAIO NTRBOOTHAX.zip", "w") as zipf:
                zipf.write("FBI-FR.3dsx", "3ds/FBI-FR.3dsx")
                zipf.write("FBI-FR.cia", "cias/FBI-FR.cia")
                zipf.write("Anemone3DSFR.cia", "cias/Anemone3DSFR.cia")
                zipf.write("boot.3dsx", "boot.3dsx")
                zipf.write("SafeB9SInstaller.firm", "boot.firm")
                zipf.write("Checkpoint.cia", "cias/Checkpoint.cia")
                zipf.write("Universal-Updater.cia", "cias/Universal-Updater.cia")
                zipf.write("GodMode9.firm", "luma/payloads/GodMode9.firm")
                zipf.write("Homebrew_Launcher.cia", "cias/Homebrew_Launcher.cia")
                zipf.write("boot9strap.firm", "boot9strap/boot9strap.firm")
                zipf.write("boot9strap.firm.sha", "boot9strap/boot9strap.firm.sha")
                zipf.write("ntrboot_flasher.firm", "luma/payloads/ntrboot_flasher.firm")
                for root, _, files in os.walk("gm9"):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.join(root, file))
                shutil.rmtree("gm9")
                shutil.rmtree("elf")
                shutil.rmtree("ntrboot")
                shutil.rmtree("sample")
                shutil.rmtree("SafeB9SInstaller")

            os.remove("FBI-FR.cia")
            os.remove("FBI-FR.3dsx")
            os.remove("Anemone3DSFR.cia")
            os.remove("Homebrew_Launcher.cia")
            os.remove("boot.3dsx")
            os.remove("boot.firm")
            os.remove("Checkpoint.cia")
            os.remove("Universal-Updater.cia")
            os.remove("GodMode9-v2.1.1-20220322194259.zip")
            os.remove("GodMode9.firm.sha")
            os.remove("GodMode9_dev.firm")
            os.remove("GodMode9_dev.firm.sha")
            os.remove("README.md")
            os.remove("GodMode9.firm")
            os.remove("boot9strap.firm")
            os.remove("boot9strap.firm.sha")
            os.remove("ntrboot_flasher.firm")
            os.remove(f"boot9strap-{boot9strap_ver}.zip")
            os.remove(f"Luma3DSv{luma_ver}.zip")
            os.remove("SafeB9SInstaller.bin")
            os.remove("SafeB9SInstaller.nds")
            os.remove("SafeB9SInstaller.dat")
            os.remove("SafeB9SInstaller.firm")
            os.remove("SafeB9SInstaller-20170605-122940.zip")
            os.remove("arm9.bin")
            os.remove("arm11.bin")
            os.remove("Launcher.dat")

            embed_pack_ready = discord.Embed(title="LumiAIO Nintendo 3DS (NTRBOOTHAX)", 
            description="Tout le contenu de ce pack doit être placé à la racine de la carte SD de votre Nintendo 3DS. Si vous ne savez pas ce qu'est la racine, tapez ``.sdroot``.",
            color=discord.Color.green()).add_field(name="**Contenu du pack :**", value="- Universal-Updater\n- Anemone3DS (en français)\n- FBI (en français)\n- Checkpoint\n- GodMode9\n- SafeB9SInstaller\n- boot9strap\n- ntrboot_flasher").add_field(name="__**Compatibilité :**__", value="``Toutes versions``").add_field(name="__**Format :**__", value="``.zip``").set_thumbnail(url="https://hbf-files.github.io/luma_pack.png").set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true").set_author(name="Dhalian.", icon_url="https://avatars.githubusercontent.com/u/67284307?v=4", url="https://github.com/Dhalian")
            await initial_message.edit(embed=embed_pack_ready)
        
            await ctx.send(file=discord.File("LumiAIO NTRBOOTHAX.zip"))
            os.remove("LumiAIO NTRBOOTHAX.zip")



        elif console == "3ds" and (exploit == "pichaxx" or exploit == "picross"):
            embed_initial = discord.Embed(
                title="Construction du pack en cours",
                description="Veuillez patienter...\nCela ne prendra que quelques secondes.",
                color=discord.Color.orange()).set_thumbnail(url="https://homebrewfrance.github.io/IMAGES/redirection.gif").set_footer(text="Pack demandé : PICHAXX")
            initial_message = await ctx.send(embed=embed_initial)

            urllib.request.urlretrieve("https://github.com/LumaTeam/Luma3DS/releases/latest/download/Luma3DSv13.0.2.zip", f"Luma3DSv{luma_ver}.zip")
            urllib.request.urlretrieve("https://github.com/cooolgamer/FBI-Reloaded-FR/releases/latest/download/FBI-FR.3dsx", "FBI-FR.3dsx")
            urllib.request.urlretrieve("https://github.com/cooolgamer/FBI-Reloaded-FR/releases/latest/download/FBI-FR.cia", "FBI-FR.cia")        
            urllib.request.urlretrieve("https://github.com/cooolgamer/Anemone3DS-FR/releases/latest/download/Anemone3DSFR.cia", "Anemone3DSFR.cia")
            urllib.request.urlretrieve("https://github.com/BernardoGiordano/Checkpoint/releases/tag/v3.7.4", "Checkpoint.cia")
            urllib.request.urlretrieve("https://github.com/PabloMK7/homebrew_launcher_dummy/releases/latest/download/Homebrew_Launcher.cia", "Homebrew_Launcher.cia")
            urllib.request.urlretrieve("https://github.com/Universal-Team/Universal-Updater/releases/latest/download/Universal-Updater.cia", "Universal-Updater.cia")
            urllib.request.urlretrieve("https://github.com/d0k3/GodMode9/releases/latest/download/GodMode9-v2.1.1-20220322194259.zip", "GodMode9-v2.1.1-20220322194259.zip")
            urllib.request.urlretrieve("https://github.com/SciresM/boot9strap/releases/latest/download/boot9strap-1.4.zip", f"boot9strap-{boot9strap_ver}.zip")
            urllib.request.urlretrieve("https://github.com/d0k3/SafeB9SInstaller/releases/download/v0.0.7/SafeB9SInstaller-20170605-122940.zip", "SafeB9SInstaller-20170605-122940.zip")
            urllib.request.urlretrieve("https://github.com/TuxSH/universal-otherapp/releases/latest/download/otherapp.bin", "otherapp.bin")

            with zipfile.ZipFile(f"Luma3DSv{luma_ver}.zip", "r") as luma_zip:
                luma_zip.extractall()

            with zipfile.ZipFile("SafeB9SInstaller-20170605-122940.zip", "r") as sb9s_zip:
                sb9s_zip.extractall()

            with zipfile.ZipFile("GodMode9-v2.1.1-20220322194259.zip", "r") as gm9_zip:
                gm9_zip.extractall()

            with zipfile.ZipFile(f"boot9strap-{boot9strap_ver}.zip", "r") as b9s_zip:
                b9s_zip.extractall()

            with zipfile.ZipFile("LumiAIO PICHAXX.zip", "w") as zipf:
                zipf.write("FBI-FR.3dsx", "3ds/FBI-FR.3dsx")
                zipf.write("FBI-FR.cia", "cias/FBI-FR.cia")
                zipf.write("Anemone3DSFR.cia", "cias/Anemone3DSFR.cia")
                zipf.write("boot.3dsx", "boot.3dsx")
                zipf.write("boot.firm", "boot.firm")
                zipf.write("Checkpoint.cia", "cias/Checkpoint.cia")
                zipf.write("Universal-Updater.cia", "cias/Universal-Updater.cia")
                zipf.write("GodMode9.firm", "luma/payloads/GodMode9.firm")
                zipf.write("Homebrew_Launcher.cia", "cias/Homebrew_Launcher.cia")
                zipf.write("boot9strap.firm", "boot9strap/boot9strap.firm")
                zipf.write("boot9strap.firm.sha", "boot9strap/boot9strap.firm.sha")
                zipf.write("otherapp.bin", "otherapp.bin")
                zipf.write("SafeB9SInstaller.bin", "SafeB9SInstaller.bin")
                for root, _, files in os.walk("gm9"):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.join(root, file))
                shutil.rmtree("gm9")
                shutil.rmtree("elf")
                shutil.rmtree("ntrboot")
                shutil.rmtree("SafeB9SInstaller")
                shutil.rmtree("sample")

            os.remove(f"Luma3DSv{luma_ver}.zip")
            os.remove("FBI-FR.cia")
            os.remove("FBI-FR.3dsx")
            os.remove("Anemone3DSFR.cia")
            os.remove("Homebrew_Launcher.cia")
            os.remove("boot.3dsx")
            os.remove("boot.firm")
            os.remove("Checkpoint.cia")
            os.remove("Universal-Updater.cia")
            os.remove("GodMode9-v2.1.1-20220322194259.zip")
            os.remove("GodMode9.firm.sha")
            os.remove("GodMode9_dev.firm")
            os.remove("GodMode9_dev.firm.sha")
            os.remove("README.md")
            os.remove("GodMode9.firm")
            os.remove("boot9strap.firm")
            os.remove("boot9strap.firm.sha")
            os.remove(f"boot9strap-{boot9strap_ver}.zip")
            os.remove("otherapp.bin")
            os.remove("SafeB9SInstaller.bin")
            os.remove("SafeB9SInstaller.nds")
            os.remove("SafeB9SInstaller.dat")
            os.remove("SafeB9SInstaller.firm")
            os.remove("SafeB9SInstaller-20170605-122940.zip")
            os.remove("arm9.bin")
            os.remove("arm11.bin")
            os.remove("Launcher.dat")

            embed_pack_ready = discord.Embed(title="LumiAIO Nintendo 3DS (PICHAXX)", 
            description="Tout le contenu de ce pack doit être placé à la racine de la carte SD de votre Nintendo 3DS. Si vous ne savez pas ce qu'est la racine, tapez ``.sdroot``.",
            color=discord.Color.green()).add_field(name="**Contenu du pack :**", value="- Luma3DS\n- Universal-Updater\n- Anemone3DS (en français)\n- FBI (en français)\n- Checkpoint\n- GodMode9\n- SafeB9SInstaller\n- boot9strap\n- Universal-Otherapp").add_field(name="__**Compatibilité :**__", value="``11.15``").add_field(name="__**Format :**__", value="``.zip``").set_thumbnail(url="https://hbf-files.github.io/luma_pack.png").set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true").set_author(name="Dhalian.", icon_url="https://avatars.githubusercontent.com/u/67284307?v=4", url="https://github.com/Dhalian")
            await initial_message.edit(embed=embed_pack_ready)
            await ctx.send(file=discord.File("LumiAIO PICHAXX.zip"))
            os.remove("LumiAIO PICHAXX.zip")



        elif console == "3ds" and (exploit == "usm" or exploit == "seedminer"):
            embed_initial = discord.Embed(
                title="Construction du pack en cours",
                description="Veuillez patienter...\nCela ne prendra que quelques secondes.",
                color=discord.Color.orange()).set_thumbnail(url="https://homebrewfrance.github.io/IMAGES/redirection.gif").set_footer(text="Pack demandé : SEEDMINER")
            initial_message = await ctx.send(embed=embed_initial)

            urllib.request.urlretrieve("https://github.com/LumaTeam/Luma3DS/releases/latest/download/Luma3DSv13.0.2.zip", f"Luma3DSv{luma_ver}.zip")
            urllib.request.urlretrieve("https://github.com/cooolgamer/FBI-Reloaded-FR/releases/latest/download/FBI-FR.3dsx", "FBI-FR.3dsx")
            urllib.request.urlretrieve("https://github.com/cooolgamer/FBI-Reloaded-FR/releases/latest/download/FBI-FR.cia", "FBI-FR.cia")        
            urllib.request.urlretrieve("https://github.com/cooolgamer/Anemone3DS-FR/releases/latest/download/Anemone3DSFR.cia", "Anemone3DSFR.cia")
            urllib.request.urlretrieve("https://github.com/BernardoGiordano/Checkpoint/releases/tag/v3.7.4", "Checkpoint.cia")
            urllib.request.urlretrieve("https://github.com/PabloMK7/homebrew_launcher_dummy/releases/latest/download/Homebrew_Launcher.cia", "Homebrew_Launcher.cia")
            urllib.request.urlretrieve("https://github.com/Universal-Team/Universal-Updater/releases/latest/download/Universal-Updater.cia", "Universal-Updater.cia")
            urllib.request.urlretrieve("https://github.com/d0k3/GodMode9/releases/latest/download/GodMode9-v2.1.1-20220322194259.zip", "GodMode9-v2.1.1-20220322194259.zip")
            urllib.request.urlretrieve("https://github.com/SciresM/boot9strap/releases/latest/download/boot9strap-1.4.zip", f"boot9strap-{boot9strap_ver}.zip")
            urllib.request.urlretrieve("https://github.com/d0k3/SafeB9SInstaller/releases/download/v0.0.7/SafeB9SInstaller-20170605-122940.zip", "SafeB9SInstaller-20170605-122940.zip")
            urllib.request.urlretrieve("https://github.com/zoogie/unSAFE_MODE/releases/latest/download/usm.bin", "usm.bin")


            with zipfile.ZipFile(f"Luma3DSv{luma_ver}.zip", "r") as luma_seed:
                luma_seed.extractall()

            with zipfile.ZipFile("SafeB9SInstaller-20170605-122940.zip", "r") as sb9s_seed:
                sb9s_seed.extractall()

            with zipfile.ZipFile("GodMode9-v2.1.1-20220322194259.zip", "r") as gm9_seed:
                gm9_seed.extractall()

            with zipfile.ZipFile(f"boot9strap-{boot9strap_ver}.zip", "r") as b9s_seed:
                b9s_seed.extractall()

            with zipfile.ZipFile("LumiAIO SEEDMINER.zip", "w") as zipf:
                zipf.write("FBI-FR.3dsx", "3ds/FBI-FR.3dsx")
                zipf.write("FBI-FR.cia", "cias/FBI-FR.cia")
                zipf.write("Anemone3DSFR.cia", "cias/Anemone3DSFR.cia")
                zipf.write("boot.3dsx", "boot.3dsx")
                zipf.write("boot.firm", "boot.firm")
                zipf.write("Checkpoint.cia", "cias/Checkpoint.cia")
                zipf.write("Universal-Updater.cia", "cias/Universal-Updater.cia")
                zipf.write("GodMode9.firm", "luma/payloads/GodMode9.firm")
                zipf.write("Homebrew_Launcher.cia", "cias/Homebrew_Launcher.cia")
                zipf.write("boot9strap.firm", "boot9strap/boot9strap.firm")
                zipf.write("boot9strap.firm.sha", "boot9strap/boot9strap.firm.sha")
                zipf.write("usm.bin", "usm.bin")
                zipf.write("SafeB9SInstaller.bin", "SafeB9SInstaller.bin")
                for root, _, files in os.walk("gm9"):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.join(root, file))
                shutil.rmtree("gm9")
                shutil.rmtree("elf")
                shutil.rmtree("ntrboot")
                shutil.rmtree("SafeB9SInstaller")
                shutil.rmtree("sample")

            os.remove(f"Luma3DSv{luma_ver}.zip")
            os.remove("FBI-FR.cia")
            os.remove("FBI-FR.3dsx")
            os.remove("Anemone3DSFR.cia")
            os.remove("Homebrew_Launcher.cia")
            os.remove("boot.3dsx")
            os.remove("boot.firm")
            os.remove("Checkpoint.cia")
            os.remove("Universal-Updater.cia")
            os.remove("GodMode9-v2.1.1-20220322194259.zip")
            os.remove("GodMode9.firm.sha")
            os.remove("GodMode9_dev.firm")
            os.remove("GodMode9_dev.firm.sha")
            os.remove("README.md")
            os.remove("GodMode9.firm")
            os.remove("boot9strap.firm")
            os.remove("boot9strap.firm.sha")
            os.remove(f"boot9strap-{boot9strap_ver}.zip")
            os.remove("usm.bin")
            os.remove("SafeB9SInstaller.bin")
            os.remove("SafeB9SInstaller.nds")
            os.remove("SafeB9SInstaller.dat")
            os.remove("SafeB9SInstaller.firm")
            os.remove("SafeB9SInstaller-20170605-122940.zip")
            os.remove("arm9.bin")
            os.remove("arm11.bin")
            os.remove("Launcher.dat")

            embed_pack_ready = discord.Embed(title="LumiAIO Nintendo 3DS (Seedminer)", 
            description="Tout le contenu de ce pack doit être placé à la racine de la carte SD de votre Nintendo 3DS. Si vous ne savez pas ce qu'est la racine, tapez ``.sdroot``.",
            color=discord.Color.green()).add_field(name="**Contenu du pack :**", value="- Luma3DS\n- Universal-Updater\n- Anemone3DS (en français)\n- FBI (en français)\n- Checkpoint\n- GodMode9\n- SafeB9SInstaller\n- boot9strap\n- unSAFE_MODE").add_field(name="__**Compatibilité :**__", value="``11.16``").add_field(name="__**Format :**__", value="``.zip``").set_thumbnail(url="https://hbf-files.github.io/luma_pack.png").set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true").set_author(name="Dhalian.", icon_url="https://avatars.githubusercontent.com/u/67284307?v=4", url="https://github.com/Dhalian")
            await initial_message.edit(embed=embed_pack_ready)
            await ctx.send(file=discord.File("LumiAIO SEEDMINER.zip"))
            os.remove("LumiAIO SEEDMINER.zip")


        elif console == "3ds" and (exploit == "browserhax" or exploit == "super-skaterhax" or exploit == "superskaterhax" or exploit == "superskater" or exploit == "super-skater" or exploit == "skater"):
            embed_initial = discord.Embed(
                title="Construction du pack en cours",
                description="Veuillez patienter...\nCela ne prendra que quelques secondes.",
                color=discord.Color.orange()).set_thumbnail(url="https://homebrewfrance.github.io/IMAGES/redirection.gif").set_footer(text="Pack demandé : BROWSERHAX-SUPERSKATERHAX")
            initial_message = await ctx.send(embed=embed_initial)

            urllib.request.urlretrieve("https://github.com/LumaTeam/Luma3DS/releases/latest/download/Luma3DSv13.0.2.zip", f"Luma3DSv{luma_ver}.zip")
            urllib.request.urlretrieve("https://github.com/cooolgamer/FBI-Reloaded-FR/releases/latest/download/FBI-FR.3dsx", "FBI-FR.3dsx")
            urllib.request.urlretrieve("https://github.com/cooolgamer/FBI-Reloaded-FR/releases/latest/download/FBI-FR.cia", "FBI-FR.cia")        
            urllib.request.urlretrieve("https://github.com/cooolgamer/Anemone3DS-FR/releases/latest/download/Anemone3DSFR.cia", "Anemone3DSFR.cia")
            urllib.request.urlretrieve("https://github.com/BernardoGiordano/Checkpoint/releases/tag/v3.7.4", "Checkpoint.cia")
            urllib.request.urlretrieve("https://github.com/PabloMK7/homebrew_launcher_dummy/releases/latest/download/Homebrew_Launcher.cia", "Homebrew_Launcher.cia")
            urllib.request.urlretrieve("https://github.com/Universal-Team/Universal-Updater/releases/latest/download/Universal-Updater.cia", "Universal-Updater.cia")
            urllib.request.urlretrieve("https://github.com/d0k3/GodMode9/releases/latest/download/GodMode9-v2.1.1-20220322194259.zip", "GodMode9-v2.1.1-20220322194259.zip")
            urllib.request.urlretrieve("https://github.com/SciresM/boot9strap/releases/latest/download/boot9strap-1.4.zip", f"boot9strap-{boot9strap_ver}.zip")
            urllib.request.urlretrieve("https://github.com/d0k3/SafeB9SInstaller/releases/download/v0.0.7/SafeB9SInstaller-20170605-122940.zip", "SafeB9SInstaller-20170605-122940.zip")
            urllib.request.urlretrieve("https://github.com/zoogie/super-skaterhax/releases/latest/download/release_new3ds_v1.1.zip", f"release_new3ds_v{skater_ver}.zip")
            urllib.request.urlretrieve("https://github.com/luigoalma/nimdsphax/releases/latest/download/nimdsphax_v1.0.zip", f"nimdsphax_v{nimds_ver}.zip")

            with zipfile.ZipFile(f"Luma3DSv{luma_ver}.zip", "r") as luma_bwhax:
                luma_bwhax.extractall()

            with zipfile.ZipFile("SafeB9SInstaller-20170605-122940.zip", "r") as sb9s_bwhax:
                sb9s_bwhax.extractall()

            with zipfile.ZipFile("GodMode9-v2.1.1-20220322194259.zip", "r") as gm9_bwhax:
                gm9_bwhax.extractall()

            with zipfile.ZipFile(f"boot9strap-{boot9strap_ver}.zip", "r") as b9s_bwhax:
                b9s_bwhax.extractall()

            with zipfile.ZipFile(f"release_new3ds_v{skater_ver}.zip", "r") as skater_bwhax:
                skater_bwhax.extractall()

            with zipfile.ZipFile(f"nimdsphax_v{nimds_ver}.zip", "r") as nimds_bwhax:
                nimds_bwhax.extractall()

            with zipfile.ZipFile("LumiAIO BROWSERHAX.zip", "w") as zipf:
                zipf.write("FBI-FR.3dsx", "3ds/FBI-FR.3dsx")
                zipf.write("FBI-FR.cia", "cias/FBI-FR.cia")
                zipf.write("Anemone3DSFR.cia", "cias/Anemone3DSFR.cia")
                zipf.write("boot.3dsx", "boot.3dsx")
                zipf.write("boot.firm", "boot.firm")
                zipf.write("Checkpoint.cia", "cias/Checkpoint.cia")
                zipf.write("Universal-Updater.cia", "cias/Universal-Updater.cia")
                zipf.write("GodMode9.firm", "luma/payloads/GodMode9.firm")
                zipf.write("Homebrew_Launcher.cia", "cias/Homebrew_Launcher.cia")
                zipf.write("boot9strap.firm", "boot9strap/boot9strap.firm")
                zipf.write("boot9strap.firm.sha", "boot9strap/boot9strap.firm.sha")
                zipf.write("SafeB9SInstaller.bin", "SafeB9SInstaller.bin")
                zipf.write("nimdsphax/nimdsphax.3dsx", "3ds/nimdsphax/nimdsphax.3dsx")
                zipf.write("nimdsphax/nimdsphax.xml", "3ds/nimdsphax/nimdsphax.xml")
                zipf.write("nimdsphax/nimdsphax.smdh", "3ds/nimdsphax/nimdsphax.smdh")
                zipf.write("nimdsphax/nim_config.xml", "3ds/nimdsphax/nim_config.xml")
                for root, _, files in os.walk("gm9"):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.join(root, file))
                for root, _, files in os.walk("EUROPE (11.17.0-50E, 11.16.0-49E)"):
                    for file in files:
                        file_path = os.path.join(root, file)
                        arcname = os.path.relpath(file_path, "EUROPE (11.17.0-50E, 11.16.0-49E)")
                        zipf.write(file_path, arcname)
                shutil.rmtree("gm9")
                shutil.rmtree("elf")
                shutil.rmtree("ntrboot")
                shutil.rmtree("SafeB9SInstaller")
                shutil.rmtree("EUROPE (11.17.0-50E, 11.16.0-49E)")
                shutil.rmtree("JAPAN (11.17.0-50J, 11.16.0-49J)")
                shutil.rmtree("KOREA (11.16.0-42K)")
                shutil.rmtree("USA (11.16.0-49U)")
                shutil.rmtree("USA (11.17.0-50U)")
                shutil.rmtree("nimdsphax")
                shutil.rmtree("sample")

            os.remove(f"Luma3DSv{luma_ver}.zip")
            os.remove("FBI-FR.cia")
            os.remove("FBI-FR.3dsx")
            os.remove("Anemone3DSFR.cia")
            os.remove("Homebrew_Launcher.cia")
            os.remove("boot.3dsx")
            os.remove("boot.firm")
            os.remove("Checkpoint.cia")
            os.remove("Universal-Updater.cia")
            os.remove("GodMode9-v2.1.1-20220322194259.zip")
            os.remove("GodMode9.firm.sha")
            os.remove("GodMode9_dev.firm")
            os.remove("GodMode9_dev.firm.sha")
            os.remove("README.md")
            os.remove("GodMode9.firm")
            os.remove("boot9strap.firm")
            os.remove("boot9strap.firm.sha")
            os.remove(f"boot9strap-{boot9strap_ver}.zip")
            os.remove("SafeB9SInstaller.bin")
            os.remove("SafeB9SInstaller.nds")
            os.remove("SafeB9SInstaller.dat")
            os.remove("SafeB9SInstaller.firm")
            os.remove("SafeB9SInstaller-20170605-122940.zip")
            os.remove(f"nimdsphax_v{nimds_ver}.zip")
            os.remove(f"release_new3ds_v{skater_ver}.zip")
            os.remove("arm9.bin")
            os.remove("arm11.bin")
            os.remove("Launcher.dat")

            embed_pack_ready = discord.Embed(title="LumiAIO Nintendo 3DS (Browserhax (super-skaterhax))", 
            description="Tout le contenu de ce pack doit être placé à la racine de la carte SD de votre Nintendo 3DS. Si vous ne savez pas ce qu'est la racine, tapez ``.sdroot``.",
            color=discord.Color.green()).add_field(name="**Contenu du pack :**", value="- Luma3DS\n- Universal-Updater\n- Anemone3DS (en français)\n- FBI (en français)\n- Checkpoint\n- GodMode9\n- SafeB9SInstaller\n- boot9strap\n- nimdsphax\n- Browserhax").add_field(name="__**Compatibilité :**__", value="``11.16 & 11.17 (New 3DS seulement)``").add_field(name="__**Format :**__", value="``.zip``").set_thumbnail(url="https://hbf-files.github.io/luma_pack.png").set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true").set_author(name="Dhalian.", icon_url="https://avatars.githubusercontent.com/u/67284307?v=4", url="https://github.com/Dhalian")
            await initial_message.edit(embed=embed_pack_ready)
            await ctx.send(file=discord.File("LumiAIO BROWSERHAX.zip"))
            os.remove("LumiAIO BROWSERHAX.zip")


        elif console == "3ds" and (exploit == "kartminer" or exploit == "kartminer7" or exploit == "km7" or exploit == "mk7" or exploit == "mariokart" or exploit == "mariokart7"):
            embed_initial = discord.Embed(
                title="Construction du pack en cours",
                description="Veuillez patienter...\nCela ne prendra que quelques secondes.",
                color=discord.Color.orange()).set_thumbnail(url="https://homebrewfrance.github.io/IMAGES/redirection.gif").set_footer(text="Pack demandé : KARTMINER7")
            initial_message = await ctx.send(embed=embed_initial)

            urllib.request.urlretrieve("https://github.com/LumaTeam/Luma3DS/releases/latest/download/Luma3DSv13.0.2.zip", f"Luma3DSv{luma_ver}.zip")
            urllib.request.urlretrieve("https://github.com/cooolgamer/FBI-Reloaded-FR/releases/latest/download/FBI-FR.3dsx", "FBI-FR.3dsx")
            urllib.request.urlretrieve("https://github.com/cooolgamer/FBI-Reloaded-FR/releases/latest/download/FBI-FR.cia", "FBI-FR.cia")        
            urllib.request.urlretrieve("https://github.com/cooolgamer/Anemone3DS-FR/releases/latest/download/Anemone3DSFR.cia", "Anemone3DSFR.cia")
            urllib.request.urlretrieve("https://github.com/BernardoGiordano/Checkpoint/releases/tag/v3.7.4", "Checkpoint.cia")
            urllib.request.urlretrieve("https://github.com/PabloMK7/homebrew_launcher_dummy/releases/latest/download/Homebrew_Launcher.cia", "Homebrew_Launcher.cia")
            urllib.request.urlretrieve("https://github.com/Universal-Team/Universal-Updater/releases/latest/download/Universal-Updater.cia", "Universal-Updater.cia")
            urllib.request.urlretrieve("https://github.com/d0k3/GodMode9/releases/latest/download/GodMode9-v2.1.1-20220322194259.zip", "GodMode9-v2.1.1-20220322194259.zip")
            urllib.request.urlretrieve("https://github.com/SciresM/boot9strap/releases/latest/download/boot9strap-1.4.zip", f"boot9strap-{boot9strap_ver}.zip")
            urllib.request.urlretrieve("https://github.com/d0k3/SafeB9SInstaller/releases/download/v0.0.7/SafeB9SInstaller-20170605-122940.zip", "SafeB9SInstaller-20170605-122940.zip")
            urllib.request.urlretrieve("https://github.com/luigoalma/nimdsphax/releases/latest/download/nimdsphax_v1.0.zip", f"nimdsphax_v{nimds_ver}.zip")

            with zipfile.ZipFile(f"Luma3DSv{luma_ver}.zip", "r") as luma_km7:
                luma_km7.extractall()

            with zipfile.ZipFile("SafeB9SInstaller-20170605-122940.zip", "r") as sb9s_km7:
                sb9s_km7.extractall()

            with zipfile.ZipFile("GodMode9-v2.1.1-20220322194259.zip", "r") as gm9_km7:
                gm9_km7.extractall()

            with zipfile.ZipFile(f"boot9strap-{boot9strap_ver}.zip", "r") as b9s_km7:
                b9s_km7.extractall()

            with zipfile.ZipFile(f"nimdsphax_v{nimds_ver}.zip", "r") as nimds_km7:
                nimds_km7.extractall()

            with zipfile.ZipFile("LumiAIO KARTMINER7.zip", "w") as zipf:
                zipf.write("FBI-FR.3dsx", "3ds/FBI-FR.3dsx")
                zipf.write("FBI-FR.cia", "cias/FBI-FR.cia")
                zipf.write("Anemone3DSFR.cia", "cias/Anemone3DSFR.cia")
                zipf.write("boot.3dsx", "boot.3dsx")
                zipf.write("boot.firm", "boot.firm")
                zipf.write("Checkpoint.cia", "cias/Checkpoint.cia")
                zipf.write("Universal-Updater.cia", "cias/Universal-Updater.cia")
                zipf.write("GodMode9.firm", "luma/payloads/GodMode9.firm")
                zipf.write("Homebrew_Launcher.cia", "cias/Homebrew_Launcher.cia")
                zipf.write("boot9strap.firm", "boot9strap/boot9strap.firm")
                zipf.write("boot9strap.firm.sha", "boot9strap/boot9strap.firm.sha")
                zipf.write("SafeB9SInstaller.bin", "SafeB9SInstaller.bin")
                zipf.write("nimdsphax/nimdsphax.3dsx", "3ds/nimdsphax/nimdsphax.3dsx")
                zipf.write("nimdsphax/nimdsphax.xml", "3ds/nimdsphax/nimdsphax.xml")
                zipf.write("nimdsphax/nimdsphax.smdh", "3ds/nimdsphax/nimdsphax.smdh")
                zipf.write("nimdsphax/nim_config.xml", "3ds/nimdsphax/nim_config.xml")
                for root, _, files in os.walk("gm9"):
                    for file in files:
                        zipf.write(os.path.join(root, file), os.path.join(root, file))
                shutil.rmtree("gm9")
                shutil.rmtree("elf")
                shutil.rmtree("ntrboot")
                shutil.rmtree("SafeB9SInstaller")
                shutil.rmtree("nimdsphax")

            os.remove(f"Luma3DSv{luma_ver}.zip")
            os.remove("FBI-FR.cia")
            os.remove("FBI-FR.3dsx")
            os.remove("Anemone3DSFR.cia")
            os.remove("Homebrew_Launcher.cia")
            os.remove("boot.3dsx")
            os.remove("boot.firm")
            os.remove("Checkpoint.cia")
            os.remove("Universal-Updater.cia")
            os.remove("GodMode9-v2.1.1-20220322194259.zip")
            os.remove("GodMode9.firm.sha")
            os.remove("GodMode9_dev.firm")
            os.remove("GodMode9_dev.firm.sha")
            os.remove("README.md")
            os.remove("GodMode9.firm")
            os.remove("boot9strap.firm")
            os.remove("boot9strap.firm.sha")
            os.remove(f"boot9strap-{boot9strap_ver}.zip")
            os.remove("SafeB9SInstaller.bin")
            os.remove("SafeB9SInstaller.nds")
            os.remove("SafeB9SInstaller.dat")
            os.remove("SafeB9SInstaller.firm")
            os.remove("SafeB9SInstaller-20170605-122940.zip")
            os.remove(f"nimdsphax_v{nimds_ver}.zip")
            os.remove("arm9.bin")
            os.remove("arm11.bin")
            os.remove("Launcher.dat")

            embed_pack_ready = discord.Embed(title="LumiAIO Nintendo 3DS (KartMiner7)", 
            description="Tout le contenu de ce pack doit être placé à la racine de la carte SD de votre Nintendo 3DS. Si vous ne savez pas ce qu'est la racine, tapez ``.sdroot``.",
            color=discord.Color.green()).add_field(name="**Contenu du pack :**", value="- Luma3DS\n- Universal-Updater\n- Anemone3DS (en français)\n- FBI (en français)\n- Checkpoint\n- GodMode9\n- SafeB9SInstaller\n- boot9strap\n- nimdsphax\n- KartMiner7").add_field(name="__**Compatibilité :**__", value="``11.17``").add_field(name="__**Format :**__", value="``.zip``").set_thumbnail(url="https://hbf-files.github.io/luma_pack.png").set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true").set_author(name="Dhalian.", icon_url="https://avatars.githubusercontent.com/u/67284307?v=4", url="https://github.com/Dhalian")
            await initial_message.edit(embed=embed_pack_ready)
            await ctx.send(file=discord.File("LumiAIO KARTMINER7.zip"))
            os.remove("LumiAIO KARTMINER7.zip")


        elif console == "switch" and (exploit == "vanilla" or exploit == "atmo" or exploit == "atmosphere" or exploit == "atmosphère" or exploit == "atmopack" or exploit == "zoria" or exploit == "aio"):
            embed_initial = discord.Embed(
                title="Recherche de la version la plus récente",
                description="Veuillez patienter...\nCela ne prendra que quelques secondes.",
                color=discord.Color.orange()).set_thumbnail(url="https://homebrewfrance.github.io/IMAGES/redirection.gif").set_footer(text="Pack demandé : ATMOPACK")
            initial_message = await ctx.send(embed=embed_initial)

            embed_pack_ready = discord.Embed(title="AtmoPack Vanilla", 
            description="Tout le contenu de ce pack doit être placé à la racine de la carte SD de votre Nintendo Switch. Si vous ne savez pas ce qu'est la racine, tapez ``.sdroot``.",
            color=discord.Color.green()).add_field(name="**Contenu du pack :**", value="- Atmosphère\n- Hekate\n- Sigpatches\n- DayBreak\n- Goldleaf\n- JKSV\n- FTPD\n- NXMTP\n- TinWoo\n- DBI\n- 90DNS_Testeur\n- PayloadReboot\n- Atmopack-Updater\n\n- [GitHub](https://github.com/THZoria/AtmoPack-Vanilla)\n- [Télécharger](https://github.com/THZoria/AtmoPack-Vanilla/releases/latest/download/AtmoPack-Vanilla_Latest.zip)").add_field(name="__**Compatibilité :**__", value="``16.1.0``").add_field(name="__**Format :**__", value="``.zip``").set_thumbnail(url="https://hbf-files.github.io/atmo_pack.png").set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true").set_author(name="THZoria", icon_url="https://avatars.githubusercontent.com/u/50277488?v=4", url="https://github.com/THZoria")
            await initial_message.edit(embed=embed_pack_ready)

        elif console == "switch" and (exploit == "ls" or exploit == "lsatelier" or exploit == "logic" or exploit == "sunrise" or exploit == "logicsunrise" or exploit == "logic-sunrise" or exploit == "atelierls"):
            embed_initial = discord.Embed(
                title="Recherche de la version la plus récente",
                description="Veuillez patienter...\nCela ne prendra que quelques secondes.",
                color=discord.Color.orange()).set_thumbnail(url="https://homebrewfrance.github.io/IMAGES/redirection.gif").set_footer(text="Pack demandé : AIO LS PACK")
            initial_message = await ctx.send(embed=embed_initial)

            embed_pack_ready = discord.Embed(title="Switch AIO LS Pack", 
            description="Lancez le fichier ``nettoyeur.bat`` au préalable puis éxécutez le fichier ``.exe``. Vous pouvez également utiliser le Homebrew 'AIO LS Pack Updater' pour tout configurer depuis la console.",
            color=discord.Color.green()).add_field(name="**Contenu du pack :**", value="- Atmosphère\n- Hekate\n- HWFLY-nx\n- Fichiers pour Picofly\n- Incognito-RCM\n- Lockpick-RCM\n- ProdInfo_gen\n- TegraExplorer\n- Udpih-nxpayload\n- AIO LS Pack Updater\n- AIO Switch Updater\n- Homebrew App Store\n- AtmoXL-Titel-Installer\n- DBI\n- FTPD\n- Gamecard-Installer-NX\n- GoldLeaf\n- Haku33\n- JKSV\n- Linkalho\n- Nxdumptool\n- Nxmp\n- SwitchThemeInjectore\n- Payload_Launcher\n- Pplay\n- ResetParentalControls-NX\n- SimpleModManager\n- SimpleModDownloader\n- Switch_90DNS_Tester\n- Switch_90DNS_Setter\n- Tinfoil\n- nx-ovlloader\n- Tesla-Menu\n- Sys-patch\n- FastCFWSwitch\n- EdiZon overlay\n- OvlSysmodules\n- Status-Monitor-Overlay\n\n- [GitHub](https://github.com/shadow2560/switch_AIO_LS_pack)\n- [Télécharger](https://github.com/shadow2560/switch_AIO_LS_pack/releases/latest)").add_field(name="__**Compatibilité :**__", value="``16.1.0``").add_field(name="__**Format :**__", value="``.zip``").set_thumbnail(url="https://hbf-files.github.io/atmo_pack.png").set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true").set_author(name="shadow2560 & LS", icon_url="https://avatars.githubusercontent.com/u/24191064?v=4", url="https://github.com/shadow2560")
            await initial_message.edit(embed=embed_pack_ready)


    @commands.command(name='pack')
    async def pack(self, ctx, console: str = None, exploit: str = None):
        if console is None or exploit is None:
            embed = discord.Embed(
                title="Liste des packs disponibles",
                description="Toutes les commandes de pack s'utilisent de cette manière : ``.pack [console] [nom du pack]``. Par exemple si je veux le pack Nintendo 3DS 'NTRBOOTHAX', j'écris la commande ``.pack 3ds ntrboothax``.",
                color=discord.Color.red()).add_field(name="__**Nintendo 3DS**__", value="- KatrtMiner7 : ``kartminer7``\n- Browserhax (SSH) ; ``browserhax``\n- Pichaxx : ``pichaxx``\n- ntrboothax : ``ntrboothax``\n- Seedminer : ``seedminer``").add_field(name="__**Nintendo Switch**__", value="- AtmoPack-Vanilla : ``atmopack``\n- LS AIO : ``aio``").set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
            await ctx.send(embed=embed)
            return

        await self.construct_pack(ctx, console, exploit)

    @commands.command(name='packs')
    async def packs(self, ctx, console: str = None, exploit: str = None):
        if console is None or exploit is None:
            embed = discord.Embed(
                title="Liste des packs disponibles",
                description="Toutes les commandes de pack s'utilisent de cette manière : ``.pack [console] [nom du pack]``. Par exemple si je veux le pack Nintendo 3DS 'NTRBOOTHAX', j'écris la commande ``.pack 3ds ntrboothax``.",
                color=discord.Color.red()).add_field(name="__**Nintendo 3DS**__", value="- KatrtMiner7 : ``kartminer7``\n- Browserhax (SSH) ; ``browserhax``\n- Pichaxx : ``pichaxx``\n- ntrboothax : ``ntrboothax``").add_field(name="__**Nintendo Switch**__", value="- AtmoPack-Vanilla : ``atmopack``\n- LS AIO : ``aio``").set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
            await ctx.send(embed=embed)
            return

        await self.construct_pack(ctx, console, exploit)

    @commands.command(name='lumiaio', description='test')
    async def lumiaio(self, ctx, console: str = None, exploit: str = None):
        if console is None or exploit is None:
            embed = discord.Embed(
                title="Liste des packs disponibles",
                description="Toutes les commandes de pack s'utilisent de cette manière : ``.pack [console] [nom du pack]``. Par exemple si je veux le pack Nintendo 3DS 'NTRBOOTHAX', j'écris la commande ``.pack 3ds ntrboothax``.",
                color=discord.Color.red()).add_field(name="__**Nintendo 3DS**__", value="- KatrtMiner7 : ``kartminer7``\n- Browserhax (SSH) ; ``browserhax``\n- Pichaxx : ``pichaxx``\n- ntrboothax : ``ntrboothax``").add_field(name="__**Nintendo Switch**__", value="- AtmoPack-Vanilla : ``atmopack``\n- LS AIO : ``aio``").set_footer(text=f"Lumia {ver}", icon_url="https://github.com/homebrewfrance/Lumia-Discord-Bot/blob/main/lumia_bot.png?raw=true")
            await ctx.send(embed=embed)
            return

        await self.construct_pack(ctx, console, exploit)

async def setup(bot):
    await bot.add_cog(Packs(bot))
