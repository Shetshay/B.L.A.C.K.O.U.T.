import discord

import responses


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = 'MTA3Nzc0MTQ5Mjk0NjM1MDEwMQ.G25z7i.WHU67NJ5CvgtBUw4GBStNeLSywl5ZD70sCwEVA'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    discord.Activity()

    @client.event
    async def on_ready():
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='over Beaned'))
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if "hate beaned" in message.content:  # Method 1
            await message.author.kick(reason=None)
        if message.author == client.user:
            return
        # async def on_message(message):
        #    if message.author == client.user:
        #        return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    client.run(TOKEN)