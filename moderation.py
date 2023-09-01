import discord
from discord.ext import commands
from datetime import timedelta
from typing import Union
from github import Github
import os
import sys
import asyncio
import re

authorized_roles_ban = ["883639603817496596", "885187371354705940"]
authorized_roles_tempban = ["883639603817496596", "885187371354705940"]
authorized_roles_banword = ["883639603817496596", "885187371354705940"]
authorized_roles = ["883639603817496596", "885187371354705940"]

muted_users = {}

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.muted_role_id = 894246592654225439

    @commands.command()
    async def mute(self, ctx, member: discord.Member = None, duration: str = None, *, reason: str = None):
        if member is None:
            await ctx.send("Aucun membre n'est spécifié.")
            return
        
        if reason is None:
            await ctx.send("Veuillez indiquer une raison.")
            return
        
        duration_pattern = re.compile(r'^(\d+)([mjd])$')
        match = duration_pattern.match(duration)
        
        if not match:
            await ctx.send("Format de durée invalide. Utilisez [nombre][m/j/d] (ex: 1m, 1j, 1mo).")
            return
        
        amount = int(match.group(1))
        unit = match.group(2)
        
        if unit == 'm':
            seconds = amount * 60
        elif unit == 'j':
            seconds = amount * 86400
        elif unit == 'mo':
            seconds = amount * 86400 * 30
        
        muted_role = discord.utils.get(ctx.guild.roles, id=self.muted_role_id)
        if not muted_role:
            await ctx.send("Le rôle Muted n'a pas été trouvé.")
            return
        
        await member.add_roles(muted_role)
        muted_users[member.id] = ctx.message.created_at + timedelta(seconds=seconds)
        
        await ctx.send(f"{member.mention} a été muté pour {amount} {unit}. Raison: {reason}")
        
        await asyncio.sleep(seconds)
        
        if member.id in muted_users:
            await member.remove_roles(muted_role)
            del muted_users[member.id]

    @commands.command()
    async def unmute(self, ctx, member: discord.Member = None):
        if member is None:
            await ctx.send("Aucun membre n'est spécifié.")
            return
        
        muted_role = discord.utils.get(ctx.guild.roles, id=self.muted_role_id)
        if not muted_role:
            await ctx.send("Le rôle Muted n'a pas été trouvé.")
            return
        
        if muted_role in member.roles:
            await member.remove_roles(muted_role)
            if member.id in muted_users:
                del muted_users[member.id]
            await ctx.send(f"{member.mention} a été démuté.")
        else:
            await ctx.send(f"{member.mention} n'est pas muté.")

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason: str = None):
        """Bannit un membre du serveur."""
        if reason is None:
            await ctx.send("Veuillez fournir une raison pour le bannissement.")
            return

        authorized = any(role.name in authorized_roles_ban for role in ctx.author.roles)
        if not authorized:
            await ctx.send("Vous n'avez pas la permission d'utiliser cette commande.")
            return
        try:
            await member.ban(reason=reason)
            await ctx.send(f"{member.mention} a été banni pour la raison : {reason}")
        except discord.Forbidden:
            await ctx.send("Je n'ai pas les permissions nécessaires pour bannir ce membre.")
        except discord.HTTPException:
            await ctx.send("Une erreur s'est produite lors de la tentative de bannissement.")

    @commands.command()
    async def tempban(self, ctx, member: discord.Member, duration: int, unit: str, *, reason: str = None):
        """Bannit temporairement un membre du serveur."""
        if reason is None:
            await ctx.send("Merci de fournir une raison pour le bannissement temporaire.")
            return
        
        unit = unit.lower()
        if unit not in ["j", "m"]:
            await ctx.send("L'unité de temps doit être 'j (jours)' ou 'm (mois)'.")
            return
        
        if unit == "j":
            duration_seconds = duration * 86400 
        elif unit == "m":
            duration_seconds = duration * 2592000 

        # Vérification des rôles de l'utilisateur
        authorized = any(role.name in authorized_roles_tempban for role in ctx.author.roles)
        if not authorized:
            await ctx.send("Vous n'avez pas la permission d'utiliser cette commande.")
            return

        try:
            await member.ban(reason=reason)
            await ctx.send(f"{member.mention} a été temporairement banni pour {duration} {unit}.")
        except discord.Forbidden:
            await ctx.send("Je n'ai pas les permissions nécessaires pour bannir ce membre.")
        except discord.HTTPException:
            await ctx.send("Une erreur s'est produite lors de la tentative de bannissement.")

        await asyncio.sleep(duration_seconds)
        await member.unban(reason="Fin du bannissement temporaire")

async def setup(bot):
    await bot.add_cog(Moderation(bot))