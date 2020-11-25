from discord.ext import commands

class Autores(commands.Cog):

	def __init__(self, bot):
		self.bot = bot


	@commands.Cog.listener()
	async def on_ready(self):
		print('Extension loaded: Autores')
		sheep_channel = self.bot.get_channel(761864233893494796)
		await sheep_channel.send('Extension loaded: Autores')


	@commands.command()
	async def ping_1(self, ctx):
		await ctx.send(f'Pong! (auto-res)')

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.content.startswith('Blek'):
			channel = message.channel
			await channel.send(':( Blek')

		elif message.content.startswith('Hi '  or 'Hii '):
			channel = message.channel
			await channel.send('Hey hey!')

		elif message.content.startswith('Heyhey'):
			channel = message.channel
			await channel.send('***HEY HEEEEEEEY!***')

		elif message.content.startswith(';-;'):
			channel = message.channel
			await channel.send(f'there there {message.author.name}, it\'s alright\n*pats*')

		elif message.content.startswith('Kyot'):
			channel = message.channel
			await channel.send('*O kawai Koto*')

		elif message.content.startswith('lol') or message.content.startswith('Lol') or message.content.startswith('lmao') or message.content.startswith('Lmao'):
			channel = message.channel
			await channel.send('*XD*')

		elif message.content.startswith('Gomen') or message.content.startswith('Gomenosai'):
			channel = message.channel
			await channel.send('Have mercy... ;-;\n*sob sob*')
			await channel.send('<a:pattheatomic:766298363615248394>')

def setup(bot):
	bot.add_cog(Autores(bot))