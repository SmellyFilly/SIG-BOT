#
# Bot extension file for moderation commands (plugin)
#
import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Kicks the mentioned/id'd user
    @commands.command(name="kick")
    @commands.has_permissions(kick_member=True)
    async def kick_cmd(self, ctx, user:discord.Member, *, reason:str="No reason."):
        '''Kicks the mentioned user (works on ID's too). A reason is not required.'''
        if ctx.author.guild_permissions > user.guild_permissions:
            try:
                await user.send(f"You've been kicked from {ctx.guild.name} for {reason}.")
            except:
                pass
            await user.kick(reason=reason)
            await ctx.send(f"{ctx.author.mention}, kicked {user.mention}!")
        else:
            await ctx.send(f"{ctx.author.mention}, you don't have enough permissions to kick this person.")
    
    # Bans the mentioned/id'd user
    @commands.command(name="ban")
    @commands.has_permissions(ban_member=True)
    async def ban_cmd(self, ctx, user:discord.Member, *, reason:str="No reason."):
        '''Bans the mentioned user (works on ID's too). A reason is not required.'''
        if ctx.author.guild_permissions > user.guild_permissions:
            try:
                await user.send(f"You've been banned from {ctx.guild.name} for {reason}.")
            except:
                pass
            await user.kick(reason=reason)
            await ctx.send(f"{ctx.author.mention}, banned {user.mention}!")
        else:
            await ctx.send(f"{ctx.author.mention}, you don't have enough permissions to ban this person.")

def setup(bot):
    bot.add_cog(Moderation(bot))
