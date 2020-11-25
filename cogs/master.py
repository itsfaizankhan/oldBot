from discord.ext import commands
from discord.ext.commands import is_owner

class Master(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print("Extention loaded: Master")
		sheep_channel = self.bot.get_channel(761864233893494796)
		await sheep_channel.send('Extension loaded: Master')
		
	# COGS REGION START
	@commands.command(aliases=["ld"])
	@commands.is_owner()
	async def load(self, ctx, extension):
		self.bot.load_extension(f'cogs.{extension}')
		await ctx.send(f'Command `load` taken.\nExtension `{extension}` loaded.')
		
		
	@commands.command(aliases=["ud"])
	@commands.is_owner()
	async def unload(self, ctx, extension):
		self.bot.unload_extension(f'cogs.{extension}')
		await ctx.send(f'Command `unload` taken.\nExtension `{extension}` unloaded.')


	@commands.command(aliases=["rd"])
	@commands.is_owner()
	async def reload(self, ctx, extension):
		self.bot.reload_extension(f'cogs.{extension}')
		await ctx.send(f'Command `reload` taken.\nExtension `{extension}` reloaded.')

# COGS REGION END

	

def setup(bot):
	bot.add_cog(Master(bot))