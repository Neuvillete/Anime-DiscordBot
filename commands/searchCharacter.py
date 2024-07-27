import discord
from queries.charQuery import searchchar
from queries.runQuery import run_query
from variables.charVar import getbychar
from misc.clean import *


def charsearch(charname):
    query = searchchar()
    variables = getbychar(charname)
    if variables:
        result = run_query(query, variables)
        if not result:
            return discord.Embed(description="There does not exist a character with the name {}.".format(charname))

        embed = discord.Embed(
            colour=discord.Colour.dark_orange(),
            title=result["data"]["Character"]["name"]["full"],
            url=result["data"]["Character"]["siteUrl"]
        )

        desc = cutlength(removetags(result["data"]["Character"]["description"]).replace("&quot;", '"'))
        for title in result["data"]["Character"]["media"]["nodes"]:
            embed.add_field(name="Title of Source", value='[{} ({})]({})'.format(title["title"]["romaji"], title["title"]["english"], title["siteUrl"], inline=False))
        embed.add_field(name="Description", value=desc, inline=False)
        embed.set_thumbnail(url=result["data"]["Character"]["image"]["large"])
        return embed

