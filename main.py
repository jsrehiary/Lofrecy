import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} has connected")

@bot.command()
async def join(ctx):
    """Command buat join ke voice channel"""
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect() # ini tindakan join nya
        await ctx.send(f"Bergabung ke {channel.name} 🎵")
    else:
        await ctx.send("Kamu gak ada di voice channel...")

@bot.command()
async def leave(ctx):
    """Command buat keluar dari voice channel"""
    if ctx.voice_client:  # Check if the bot is in a voice channel
        await ctx.voice_client.disconnect()
        await ctx.send("Keluar dari voice channel 👋")
    else:
        await ctx.send("Lah.")

bot_token = os.getenv('BOT_TOKEN')
bot.run(bot_token)