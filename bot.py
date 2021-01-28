import os

import discord

commands = discord.ext.commands

print("Logging in...")
bot = commands.Bot(command_prefix="[",
                   pm_help=True)


for file in os.listdir("ext"):
    if file.endswith(".py"):
        name = file[:-3]
        bot.load_extension(f"ext.{name}")


@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("jeff"))


@bot.command(name='invite')
async def invite_cmd(ctx):
    await ctx.author.send(f"Follow this link to add me to your server. Everything will be seperate from any other server!\nhttps://discordapp.com/api/oauth2/authorize?client_id={ctx.bot.client_id}&permissions=268823793&scope=bot")

bot.run("token")
