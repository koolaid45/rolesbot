import os
import requests
import random
import discord
from discord import app_commands
from discord.ext import commands
import sys
sys.setrecursionlimit(100000)

TOKEN = ""

client = commands.Bot(command_prefix="^", intents = discord.Intents.all())

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


client.command()
async def give(ctx, user : discord.Member, role : discord.Role):
    if role in user.roles:
        await ctx.send("that doofus has that role mister")
    else:
        await user.add_roles(role)
        await ctx.send("okey dokey!")


@client.command()
async def create(ctx, rolename, clor):
    await ctx.guild.create_role(name=rolename, permissions=discord.Permissions(permissions=0), colour=clor)
    await ctx.send("done :3")

client.run(TOKEN)
