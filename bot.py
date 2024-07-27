import discord
import jishaku
from discord.ext import commands
import os

from commands.searchAnime import animesearch
from commands.searchManga import mangasearch
from commands.searchStudio import studiosearch
from commands.searchCharacter import charsearch


intents = discord.Intents.default()
intents.message_content = True
intents.members = True


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix = '!', intents = intents, owner_id = "Your owner id here")

    async def setup_hook(self):
        print("Setup hook called")
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{filename[:-3]}')
                    print(f"Loaded extension: {filename}")
                except Exception as e:
                    print(f"Failed to load extension {filename}: {e}")

        await bot.load_extension("jishaku")
        print("Loaded extension jishaku")

        print("Attempting to sync commands...")
        try:
            synced = await self.tree.sync()
            print(f"Slash commands synced: {len(synced)} commands")
        except Exception as e:
            print(f"Failed to sync slash commands: {e}")

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')
        print(f"Bot is in {len(self.guilds)} guilds")


bot = MyBot()

@bot.command()
async def anime(ctx, *, title):
    embed = animesearch(title)
    await ctx.send(embed=embed)

@bot.command()
async def manga(ctx, *, title):
    embed = mangasearch(title)
    await ctx.send(embed=embed)

@bot.command()
async def character(ctx, *, charname):
    embed = charsearch(charname)
    await ctx.send(embed=embed)

@bot.command()
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


if __name__ == "__main__":
    bot.run('Your bot token here')
