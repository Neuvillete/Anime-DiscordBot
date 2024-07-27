import discord
from queries.studioQuery import searchstudio
from queries.runQuery import run_query
from variables.studioVar import getbystudio


def studiosearch(studioname):
    query = searchstudio()
    variables = getbystudio(studioname)
    if variables:
        result = run_query(query, variables)
        if not result:
            return discord.Embed(description="There does not exist a studio with a name of {}.".format(studioname))

        embed = discord.Embed(
            colour=discord.Colour.purple(),
            title=result["data"]["Studio"]["name"],
            url=result["data"]["Studio"]["siteUrl"]
        )
        studioShows = ""

        for show in result["data"]["Studio"]["media"]["nodes"]:
            studioShows += '[{} ({})]({})'.format((show["title"]["romaji"]), (show["title"]["english"]), show["siteUrl"]) + "\n\n"
        embed.add_field(name = "Anime produced by {}".format(result["data"]["Studio"]["name"]), value=studioShows)
        return embed

