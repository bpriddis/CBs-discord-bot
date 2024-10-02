# main.py
import os
import discord
from discord.ext import commands
import asyncio
import csv
import configparser
from datetime import datetime, timedelta
import logging
from ocr_simulator import simulate_ocr
from data_processor import process_message_data, append_to_csv
from error_handler import log_error

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot version
VERSION = "1.0.0"

# Load configuration
config = configparser.ConfigParser()
config.read('config.ini')

# Bot setup
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

# Channel ID (from environment variable)
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))

# Rate limiting
RATE_LIMIT = float(config['Settings']['RateLimit'])

async def process_message(message):
    try:
        # Check if message matches the expected format
        if not message.content.lower().startswith(('win', 'loss', 'draw')):
            return

        # Simulate OCR
        ocr_data = simulate_ocr(message.attachments[0].url if message.attachments else None)
        
        # Process data
        processed_data = process_message_data(message, ocr_data)
        
        # Append to CSV
        append_to_csv(processed_data)

    except Exception as e:
        await log_error(e, message)
        await message.channel.send(f"Error processing message: {message.jump_url}", delete_after=10)

@bot.event
async def on_ready():
    logger.info(f'Bot is ready. Logged in as {bot.user.name}')

@bot.command()
@commands.has_permissions(administrator=True)
async def process_history(ctx):
    if ctx.channel.id != CHANNEL_ID:
        await ctx.send("This command can only be used in the designated channel.")
        return

    await ctx.send("Processing message history...")
    
    messages = []
    async for message in ctx.channel.history(limit=None):
        messages.append(message)
        if len(messages) == 100:
            for msg in messages:
                await process_message(msg)
                await asyncio.sleep(RATE_LIMIT)
            messages.clear()
    
    # Process any remaining messages
    for msg in messages:
        await process_message(msg)
        await asyncio.sleep(RATE_LIMIT)

    await ctx.send("Finished processing message history.")

@bot.command()
@commands.has_permissions(administrator=True)
async def process_new(ctx):
    if ctx.channel.id != CHANNEL_ID:
        await ctx.send("This command can only be used in the designated channel.")
        return

    await ctx.send("Processing new messages...")
    
    five_minutes_ago = datetime.utcnow() - timedelta(minutes=5)
    async for message in ctx.channel.history(after=five_minutes_ago, oldest_first=True):
        await process_message(message)
        await asyncio.sleep(RATE_LIMIT)

    await ctx.send("Finished processing new messages.")

@bot.command()
async def status(ctx):
    await ctx.send(f"Bot is online. Version: {VERSION}")

@bot.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID and not message.author.bot:
        await process_message(message)
    await bot.process_commands(message)

if __name__ == "__main__":
    bot.run(os.getenv('BOT_TOKEN'))