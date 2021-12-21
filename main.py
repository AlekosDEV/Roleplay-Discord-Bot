from enum import auto
from asyncio.base_events import Server
from re import A, S
from typing import AsyncGenerator
import discord
import asyncio
import functools
import itertools
import math
import json
from discord import message
from discord import member
from discord import user
from datetime import datetime
from discord import mentions
from discord import channel
from discord import role
from discord import embeds
from discord import guild
from discord import reaction
from discord import colour
from discord.abc import _Overwrites, User
from discord.ext import commands, tasks
import random
import os
from discord.ext.commands.bot import Bot
from discord.ext.commands.core import command
from discord.player import AudioSource
from discord.utils import get
from os import name, system, urandom
from itertools import cycle
from async_timeout import timeout
import platform

TOKEN = ""

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    print('FullFear PvP is online')
    print('{0.user} is Online '.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name='FullFear Roleplay'))
    

@client.command()
async def ping(ctx):
    await ctx.send(f'Ping: {round(client.latency * 500)}ms')


@client.command(aliases=['addrole'])
async def add(ctx, role: discord.Role, user: discord.User):
    await user.add_roles(role)
    await ctx.send(f'added {role} {user.mention}')

@client.event
async def on_member_join(member):
    await client.get_channel(913461042632351754)
    await channel.send('{member} join in the server')

@client.event
async def on_member_remove(member):
    await client.get_channel(913461042632351754)
    await channel.send('{member} someone leave from the server')

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='🧍Civilian')
    await client.add_roles(member, role)

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    
@client.command()
async def userinfo(ctx):
    user = ctx.author

    embed=discord.Embed(title="USER INFO", description=f" Your Profile {user}", colour=user.colour)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="NAME", value=user.name, inline=True)
    embed.add_field(name="NICKNAME", value=user.nick, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="STATUS", value=user.status, inline=True)
    embed.add_field(name="TOP ROLE", value=user.top_role.name, inline=True)
    embed.add_field(name="Server Boost", value=user.server_boost, inline=True)
    await ctx.send(embed=embed)

@client.command()
async def ip(ctx):
    user = ctx.author

    embed=discord.Embed(title="Server IP", colour=discord.Colour.purple())
    embed.add_field(name="FullFear PvP", value="Ip coming soon....")
    await ctx.send(embed=embed)

@client.command()
async def rr(ctx):
    user = ctx.author

    embed=discord.Embed(title="Server Restart Plan", colour=discord.Colour.purple())
    embed.add_field(name="FullFear PvP", value="Restart Plan 12:00 2:00 6:00 10:00")
    await ctx.send(embed=embed)

@client.command()
async def Help(ctx):
    user = ctx.author

    embed=discord.Embed(title="Help Commands", description=f"Help commands {user}", colour=discord.Colour.purple())
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Userinfo", value="!userinfo")
    embed.add_field(name="Restarts plan", value="!rr")
    embed.add_field(name="Ip Address", value="!ip")
    embed.add_field(name="Ping", value="!ping")
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed=discord.Embed(title=f'{member} kicked', colour=discord.Colour.purple())
    await ctx.send(embed=embed) 

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed=discord.Embed(title=f'{member} banned', colour=discord.Colour.purple())
    await ctx.send(embed=embed) 

@client.command()
async def say(ctx, *, message):
    await ctx.message.delete()  
    await ctx.send(f"{message}".format(message))    

@client.command()
async def staff(ctx):
    user = ctx.author

    embed=discord.Embed(title="Staff Commands", description=f"Staff commands {user}", colour=discord.Colour.purple())
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Userinfo", value="!userinfo")
    embed.add_field(name="Restarts plan", value="!rr")
    embed.add_field(name="Ip Address", value="!ip")
    embed.add_field(name="Ping", value="!ping")
    embed.add_field(name="Kick", value="!kick")
    embed.add_field(name="Say", value="!say")
    embed.add_field(name="ban", value="!ban")
    embed.add_field(name="AddRole", value="!addrole")
    embed.add_field(name="Mute|Unmute", value="!mute|!unmute")
    embed.add_field(name="Slowmode", value="!slowmode")
    embed.add_field(name="Polls", value="!poll")
    await ctx.send(embed=embed) 

@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}")

@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {ctx.guild.name}")

@client.command()
async def serverup(ctx):
    await ctx.message.delete()
    user = ctx.author

    embed=discord.Embed(title="FullFear PvP", colour=user.colour)
    embed.add_field(name="Server Up", value="Server Address soon.......")
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_channels=True)
async def lock(self,ctx,*,reason='None'):
    channel =ctx.channel
    overwrite = channel.overwrite_for(ctx.guild.default_role)
    overwrite.send_message = False
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

    embed=discord.Embed(title=f'FullFear PvP',description=f'This Channel is now Locked')
    await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(manage_channels=True)
async def unlock(self,ctx,*,reason='None'):
    channel =ctx.channel
    overwrite = channel.overwrite_for(ctx.guild.default_role)
    overwrite.send_message = True
    await channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)

    embed=discord.Embed(title=f'FullFear PvP',description=f'This Channel is now Unlocked')
    await ctx.send(embed=embed)

@client.event
async def  on_message(ctx):
    if 'https' in ctx.content.lower():
        await  ctx.message.delete()
        await ctx.send(f"{ctx.author.mention} !!!")
    else:
        await client.process_commands(ctx) 

@client.command()
async def slowmode(ctx, seconds: int):
    await ctx.message.delete()
    await ctx.channel.edit(slowmode_delay=seconds)
    embed=discord.Embed(title=f"Set the slowmode delay in this channel to {seconds} seconds", colour=discord.Colour.red())
    await ctx.send(embed=embed)

@client.command()
async def poll(ctx,*,message):
    await ctx.message.delete()
    embed=discord.Embed(title='FullFear PvP', description=f"{message}")
    message=await ctx.channel.send(embed=embed)
    await message.add_reaction('👍')
    await message.add_reaction('👎')

@client.command(pass_content=True)
async def nick(ctx, member: discord.Member, nick):
    await member.edit(nick=nick)
    embed=discord.Embed(title=f'Nickname was changed for {member}')
    await ctx.send(embed=embed)

@client.command()
async def message(ctx, user:discord.Member, *,message=None):
    await ctx.message.delete()
    message = 'lol'
    embed = discord.Embed(title=message)
    await user.send(embed=embed)

@client.command()
async def application(ctx): 
    await ctx.message.delete()
    user = ctx.author

    embed=discord.Embed(title='👮🏻Police Application', url='https://google.com')
    await ctx.send(embed=embed)
    embed=discord.Embed(title='🚑ekav Application', url='https://google.com')
    await ctx.send(embed=embed)
    embed=discord.Embed(title='Staff Application', url='https://google.com')
    await ctx.send(embed=embed)

client.run(TOKEN)
