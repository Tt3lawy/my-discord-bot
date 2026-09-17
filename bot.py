import discord
from discord.ext import commands

# Create intents
intents = discord.Intents.default()
intents.message_content = True

# Create bot
bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")


@bot.event
async def on_message(message):

    # Ignore bots
    if message.author.bot:
        return

    # Check if the message contains an image
    has_image = any(
        attachment.content_type
        and attachment.content_type.startswith("image/")
        for attachment in message.attachments
    )

    # React to photos
    if has_image:
        await message.add_reaction("💛")

    # Allow commands to continue working
    await bot.process_commands(message)


# Put your bot token here
import os
os.getenv("DISCORD_TOKEN")