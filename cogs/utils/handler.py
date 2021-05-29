import discord
from discord.ext import commands
import asyncio



class CommandErrorHandler(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"Command doesn't exist")
            return

        if isinstance(error, discord.errors.HTTPException):
            await ctx.send("Something went wrong. Note: The bot might be ratelimited")
            return

        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f'The command has been disabled.')
            return
        
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"You are cooldown. Please try again in **{error.retry_after:.2f}s**")
            return

        
        if isinstance(error, discord.ext.commands.errors.NotOwner):
            await ctx.send("You are not the owner of this bot so you can't use this command")
            return

        if isinstance(error, IndexError):
            await ctx.send("Thats not a valid number choice")
            return

        if isinstance(error, ValueError):
            await ctx.send("You need to tell me what I need to do, ig this is a image, separate text on the top and bottom with a comma.")
            return

        if isinstance(error, discord.ext.commands.ChannelNotFound):
            await ctx.send("Channel doesn't exist")


        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the permissions to do that! Please contact a server admin to do that for you.")
            return

        if isinstance(error, commands.ChannelNotFound):
            await ctx.send("Channel not found.")
            return
        
        
        if isinstance(error, commands.MemberNotFound):
            await ctx.send("That member doesn't exist.")
            return

        if isinstance(error, commands.MissingRole):
            await ctx.send("`You don't have have the role to use this")

        if isinstance(error, discord.Forbidden):
            await ctx.send("I can't do this. I'm forbidden to do this.")

        if isinstance(error, discord.NotFound):
            await ctx.send("Couldn't find that sorry")
            return

        if isinstance(error, asyncio.TimeoutError):
            await ctx.send("You waited too long :(")
            return

        if isinstance(error, discord.ext.commands.errors.MissingRequiredArgument):
            await ctx.send("There are required arguements/parameters you need to input")
            return

        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'Command can not be used in Private Messages.')
                return
            except discord.HTTPException:
                await ctx.send("Something went wrong. We'll report it. Note: The bot might be ratelimited")
        

        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == 'tag list':
                await ctx.send('I could not find that member. Please try again.')
                return
            else:
                await ctx.send("You were supposed to type that but you ended typing that")
                return
        else:
            raise error


def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))