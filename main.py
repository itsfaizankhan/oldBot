import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot


from pretty_help import PrettyHelp


from os import environ as cred
BOT_TOKEN = cred['TOKEN']


# Use the below 3 lines of code instead of the above 2 lines if you like but doesn't make any difference.

# import os
# os.getenv['TOKEN']
# BOT_TOKEN = os.environ['TOKEN']



def prefix_var(bot, message):
	prefixes = ['M.']

	if not message.guild:
		return "M."

	return commands.when_mentioned_or(*prefixes)(bot, message)

bot = Bot(command_prefix=prefix_var, case_insensitive=True, help_command=PrettyHelp(), intents=discord.Intents.all())


@bot.check
async def globally_block_dms(ctx):
    return ctx.guild is not None


@bot.event
async def on_guild_join(guild):
	await print(f"Joined new guild: {guild.name}\nGuild id: {guild.id}")

	
@bot.event
async def on_guild_remove(guild):
	await print(f"Removed from a guild: {guild.name}\nGuild id: {guild.id}")

@bot.command()
async def ping(ctx):
	await ctx.send(f'Pong! {round (bot.latency * 1000)}ms')


@bot.event
async def on_ready():
	print("Bot's Online")

# COGS REGION START
for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		bot.load_extension(f'cogs.{filename[:-3]}')
# COGS REGION END


# GENERAL ERROR HANDLER EVENT WHICH SENDS A MESSAGE IN CHANNEL.
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.CommandNotFound):
		await ctx.send("An error has occured. Please check if you've spelled the command correctly or if it exists at all. `Command Not Found`")


#@bot.event
#async def on_command_error_miss(ctx, error):
#	if isinstance(error, commands.MissingRequiredArguments):
#		await ctx.send("An error has occured. Please check if you've spelled the command correctly or if it exists at all. `Missing Required Arguments`")




bot.run(BOT_TOKEN, bot=True, reconnect=True)
