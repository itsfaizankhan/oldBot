import discord
from discord.ext import commands

class Test(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print("Extension loaded: Test")
		sheep_channel = self.bot.get_channel(761864233893494796)
		await sheep_channel.send(f'Extension loaded: Test')

	@commands.command()
	async def test(self, ctx, *, member: discord.Member=None):
		if not member:
			member = ctx.author
		embed = discord.Embed(title="Title", desciption = "Discription\n\nBlek", colour=member.colour)
		embed.add_field(name="Blek field name:", value="Blek value", inline=True)
		embed.add_field(name="Blek field2 name:", value="Blek value2", inline=True)
		embed.set_author(icon_url=member.avatar_url, name=str(member))
		await ctx.send(content=None, embed=embed)

	@commands.command()
	@commands.guild_only()
	async def joined(self, ctx, *, member: discord.Member):
		"""Says when a member joined."""
		await ctx.send(f'{member.display_name} joined on:\n{member.joined_at}')


	@commands.command(name='top_role', aliases=['toprole'])
	@commands.guild_only()
	async def show_toprole(self, ctx, *, member: discord.Member=None):
		"""Simple command which shows the members Top Role."""

		if member is None:
			member = ctx.author

		await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')
		
	@commands.command(name='perms', aliases=['perm', 'perms_for', 'permissions'])
	@commands.guild_only()
	async def check_permissions(self, ctx, *, member: discord.Member=None):
			"""A simple command which checks a members Guild Permissions.
			If member is not provided, the author will be checked."""

			if not member:
				member = ctx.author

			# Here we check if the value of each permission is True.
			perms = '\n'.join(perm for perm, value in member.guild_permissions if value)

			# And to make it look nice, we wrap it in an Embed.
			embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
			embed.set_author(icon_url=member.avatar_url, name=str(member))

			# \uFEFF is a Zero-Width Space, which basically allows us to have an empty field name.
			embed.add_field(name='\uFEFF', value=perms)

			await ctx.send(content=None, embed=embed)



def setup(bot):
	bot.add_cog(Test(bot))