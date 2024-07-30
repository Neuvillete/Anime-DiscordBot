import os
import discord
import jishaku
from discord.ext import commands
from discord.ext import app_commands

from commands.searchAnime import animesearch
from commands.searchManga import mangasearch
from commands.searchStudio import studiosearch
from commands.searchCharacter import charsearch


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='!', intents=intents, owner_id="Your owner id here")

    async def setup_hook(self):
        print("Setup hook called")
        print("Attempting to sync commands...")
        try:
            synced = await self.tree.sync()
            print(f"Slash commands synced: {len(synced)} commands")
        except Exception as e:
            print(f"Failed to sync slash commands: {e}")

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        print(f"Bot is in {len(self.guilds)} guilds")
        await bot.load_extension('jishaku')


bot = MyBot()

@bot.tree.command()
async def anime(ctx, *, title):
    embed = animesearch(title)
    await ctx.send(embed=embed)

@bot.tree.command()
async def manga(ctx, *, title):
    embed = mangasearch(title)
    await ctx.send(embed=embed)

@bot.tree.command()
async def character(ctx, *, charname):
    embed = charsearch(charname)
    await ctx.send(embed=embed)

@bot.tree.command()
async def studio(ctx, *, title):
    embed = studiosearch(title)
    await ctx.send(embed=embed)


@bot.command()
@commands.is_owner()
async def sync(ctx):
    try:
        print("Manual sync initiated")
        synced = await bot.tree.sync()
        print(f"Slash commands manually synced: {len(synced)} commands")
        await ctx.send(f"Synced {len(synced)} commands.")
    except Exception as e:
        print(f"Failed to manually sync commands: {e}")
        await ctx.send(f"Failed to sync commands: {e}")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Command not found. Available commands: {', '.join([c.name for c in bot.commands])}")
    else:
        print(f"An error occurred: {error}")
bo

if __name__ == "__main__":
    bot.run('Your bot token here')
