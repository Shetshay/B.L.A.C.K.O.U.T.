# from PIL import Image, ImageFont, ImageDraw

import asyncio
import datetime

import discord
from discord.ext import commands
from datetime import timedelta


class UnfilteredBot(commands.Bot):
    """An overridden version of the Bot class that will listen to other bots."""

    async def process_commands(self, message):
        """Override process_commands to listen to bots."""
        ctx = await self.get_context(message)
        await self.invoke(ctx)

    delta = timedelta(
        days=50,
        seconds=27,
        microseconds=10,
        milliseconds=29000,
        minutes=5,
        hours=8,
        weeks=2
    )


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = UnfilteredBot(command_prefix='!', intents=intents)


@client.event
async def on_ready():
    print('Bot is ready!')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='over Beaned'))


@client.command()
@commands.has_role('him')
async def smite(ctx):
    duration = datetime.timedelta(seconds=300)
    await ctx.send("Please mention a user to smite!")

    # Wait for the next message in the channel
    def check(message):
        return message.author != client.user and message.channel == ctx.channel and message.content != ''

    try:
        msg = await client.wait_for('message', check=check, timeout=30)
    except asyncio.TimeoutError:
        await ctx.send("No message received in time, smite command cancelled.")
        return

    user = msg.mentions[0]

    await ctx.send(f"{user.mention}, you have been smited!")
    await ctx.send(file=discord.File('smite.gif'))
    await user.timeout(duration, reason="Smited by bot")
    await ctx.send(f"{user.mention} has been timed out for 5 minutes!")


@client.command()
@commands.has_role('him')
async def stab(ctx):
    duration = datetime.timedelta(seconds=300)
    await ctx.send("Please mention a user to stab!")

    # Wait for the next message in the channel
    def check(message):
        return message.author != client.user and message.channel == ctx.channel and message.content != ''

    try:
        msg = await client.wait_for('message', check=check, timeout=30)
    except asyncio.TimeoutError:
        await ctx.send("No message received in time, stab command cancelled.")
        return

    user = msg.mentions[0]

    await ctx.send(f"{user.mention}, you have been stabbed!")
    await ctx.send(file=discord.File('smite.gif'))
    await user.timeout(duration, reason="Stabbed by bot")
    await ctx.send(f"{user.mention} has been timed out for 5 minutes!")


@client.command()
@commands.has_role('him')
async def holysmite(ctx):
    duration = datetime.timedelta(hours=1)
    await ctx.send("Please mention a user to holysmite!")

    # Wait for the next message in the channel
    def check(message):
        return message.author != client.user and message.channel == ctx.channel and message.content != ''

    try:
        msg = await client.wait_for('message', check=check, timeout=30)
    except asyncio.TimeoutError:
        await ctx.send("No message received in time, stab command cancelled.")
        return

    user = msg.mentions[0]

    await ctx.send(f"{user.mention}, you have been holy smited'!")
    await ctx.send(file=discord.File('holysmite.gif'))
    await user.timeout(duration, reason="Stabbed by bot")
    await ctx.send(f"{user.mention} has been timed out for 1 hour!")


@client.command()
@commands.has_permissions(administrator=True)
async def noblekill(ctx):
    await ctx.send("Please mention a noble to kill!")

    # Wait for the next message in the channel
    def check(message):
        return message.author != client.user and message.channel == ctx.channel and message.content != ''

    try:
        msg = await client.wait_for('message', check=check, timeout=30)
    except asyncio.TimeoutError:
        await ctx.send("No message received in time, noblekill command cancelled.")
        return
    user = msg.mentions[0]
    roles_to_remove = ['Nobility', 'Duke', 'Marquess', 'Earl', 'Viscount', 'Baron']
    roles = [role.name for role in user.roles]
    roles_removed = []
    for role in roles_to_remove:
        if role in roles:
            roles_removed.append(role)
            role_obj = discord.utils.get(user.guild.roles, name=role)
            await user.remove_roles(role_obj)
    if roles_removed:
        await ctx.send(f"{user.mention} had the following roles removed: {', '.join(roles_removed)}")
    else:
        await ctx.send(f"{user.mention} did not have any of the roles to remove.")


@client.command()
@commands.has_permissions(administrator=True)
async def holyknightkill(ctx):
    await ctx.send("Please mention a Holy Knight to dethrone!")

    # Wait for the next message in the channel
    def check(message):
        return message.author != client.user and message.channel == ctx.channel and message.content != ''

    try:
        msg = await client.wait_for('message', check=check, timeout=30)
    except asyncio.TimeoutError:
        await ctx.send("No message received in time, dethroning command cancelled.")
        return
    user = msg.mentions[0]
    roles_to_remove = 'Holy Knight'
    roles = [role.name for role in user.roles]
    roles_removed = []
    for role in roles_to_remove:
        if role in roles:
            roles_removed.append(role)
            role_obj = discord.utils.get(user.guild.roles, name=role)
            await user.remove_roles(role_obj)
    if roles_removed:
        await ctx.send(f"{user.mention} had the following roles removed: {', '.join(roles_removed)}")
    else:
        await ctx.send(f"{user.mention} did not have any of the roles to remove.")


def run_discord_bot():
    # TOKEN = 'token'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    discord.Activity()

    @client.event
    async def on_ready():
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='over Beaned'))
        print(f'{client.user} is now running!')


'''
    @client.event
    async def on_message(message):
        if "hate beaned" in message.content:  # Method 1
            await message.author.kick(reason=None)
            return "No hate speech in Beaned. "

        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")
        
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)
'''

client.run('token')
