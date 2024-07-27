import discord
from queries.idQuery import searchbyid
from queries.titleQuery import searchbytitle
from variables.idVar import getbyid
from variables.titleVar import getbytitle
from queries.runQuery import run_query
from misc.clean import removetags


def animesearch(title):
    if title.isnumeric():
        query = searchbyid()
        variables = getbyid('anime', title)
    elif not title.isnumeric():
        query = searchbytitle()
        variables = getbytitle('anime', title)
    if variables:
        result = run_query(query, variables)
        if not result:
            return discord.Embed(description="There does not exist an anime with a title/ID of {}.".format(title))

        embed = discord.Embed(
            colour=discord.Colour.blue(),
            title=('{} ({}) {}'.format(result["data"]["Media"]["title"]["romaji"],
                                       result["data"]["Media"]["title"]["english"],
                                       result["data"]["Media"]["format"])),
            url=result["data"]["Media"]["siteUrl"],
            description=(removetags(result["data"]["Media"]["description"])).replace("&quot;", '"')
        )
        embed.add_field(name="Status", value=result["data"]["Media"]["status"].upper(), inline=True)
        embed.add_field(name="Season",
                        value='{} {}'.format(result["data"]["Media"]["season"], result["data"]["Media"]["seasonYear"]),
                        inline=True)
        embed.add_field(name="Number of Episodes", value=result["data"]["Media"]["episodes"], inline=True)
        embed.add_field(name="Duration",
                        value='{} minutes/episode'.format(result["data"]["Media"]["duration"], inline=True))
        embed.add_field(name="Favourites", value=result["data"]["Media"]["favourites"], inline=True)
        embed.add_field(name="Average Score", value='{}%'.format(result["data"]["Media"]["averageScore"], inline=True))
        embed.set_thumbnail(url=result["data"]["Media"]["coverImage"]["large"])
        return embed

