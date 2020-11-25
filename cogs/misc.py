import discord
from discord.ext import commands

class Miscellaneous(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print("Extension loaded: Miscellaneous")
		sheep_channel = self.bot.get_channel(761864233893494796)
		await sheep_channel.send(f'Extension loaded: Miscellaneous')

	@commands.command(aliases=["avatar","av"])
	async def show_avatar(self, ctx, *, member: discord.Member=None):
		if not member:
			member = ctx.author
		embed = discord.Embed(title="", desciption = f"Avatar Command", colour=member.colour)
		embed.add_field(name="Avatar", value=f"Role color: `{member.colour}`", inline=False)
		embed.set_image(url=member.avatar_url)
		embed.set_author(icon_url=member.avatar_url, name=str(member))
		await ctx.send(embed=embed)
		
		
	@commands.command(aliases=["gif"])
	async def send_gif(self, ctx):
		embed = discord.Embed(colour=ctx.author.colour)
		embed.set_image(url="https://i.ibb.co/3TmmtXb/Capture-2020-09-20-08-33-04.jpg")
		embed.set_author(icon_url=ctx.author.avatar_url, name=str(ctx.author))
		await ctx.send(embed=embed)
	
	

def setup(bot):
	bot.add_cog(Miscellaneous(bot))