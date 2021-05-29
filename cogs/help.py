import discord
from discord.ext import commands


class helpcommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Help", description="Commands", color=discord.Color.red())
        embed.add_field(name="Level", value="Shows a member's rank")
        embed.add_field(name="Leaderboard", value="Shows the top 10 in the leaderboard. **True** is **global** and **False** is **guild only**")
        embed.add_field(name="Set", value="Sets a user's xp or level")
        embed.add_field(name="Usage:", value="```\nrank [member]```")
        embed.add_field(name="Usage:", value="```\nleaderboard [true/false]```")
        embed.add_field(name="Usage:", value="```\nset [level/xp] [member] [amount]```")
        embed.add_field(name="Restart", value="Restart Bot")
        embed.add_field(name="Shutdown", value="Shutdowns the bot")
        embed.add_field(name="Refresh", value="Refresh the current code with the code on github")
        embed.add_field(name="Usage:", value="```\nrestart```")
        embed.add_field(name="Usage:", value="```\nshutdown```")
        embed.add_field(name="Usage:", value="```\nrefresh```")
        embed.add_field(name="Load", value="Load a module")
        embed.add_field(name="Unload", value="Unload a module")
        embed.add_field(name="Reload", value="Reload a module")
        embed.add_field(name="Usage:", value="```\nload [module name]```")
        embed.add_field(name="Usage:", value="```\nunload [module name]```")
        embed.add_field(name="Usage:", value="```\nreload [module name]```")
        embed.add_field(name="Uptime", value="See Bot's Uptime")
        embed.add_field(name="Source", value="Get the bot source code")
        embed.add_field(name="Stats", value="See bot's stats")
        embed.add_field(name="Usage:", value="```\nuptime```")
        embed.add_field(name="Usage:", value="```\nsource [command name]```")
        embed.add_field(name="Usage:", value="```\nstats```")
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}#{ctx.author.discriminator}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
        
 

def setup(bot):
    bot.add_cog(helpcommand(bot))
