import discord
from discord.ext import commands
from discord.ext.commands import BucketType, cooldown
from aiohttp import request
import random


fact_animal = ["dog", "cat", "panda", "racoon", "kangaroo", "fox", "bird", "koala"]

image_animal = ["dog", "cat", "panda", "koala", "fox", "kangaroo", "racoon", "whale", "bird", "pikachu"]

overlays = ["gay", "glass", "wasted"]

filters = ["greyscale", "invert", "brightness", "threshold", "sepia", "red", "green", "blue", "blurple", "pixelate", "blur"]

class Fun(commands.Cog):
	
	def __init__(self, bot):
		self.bot = bot
		
	
	@commands.Cog.listener()
	async def on_ready(self):
		print('Extension loaded: Fun')
		sheep_channel = self.bot.get_channel(761864233893494796)
		await sheep_channel.send('Extension loaded: Fun')

	
	@commands.command(name="fact", aliases=["ft"])
	@cooldown(3, 60, BucketType.guild)
	async def animal_fact(self, ctx, *, animal: str):
		if (animal := animal.lower()) in fact_animal:
			fact_url = f"https://some-random-api.ml/facts/{animal}"
			image_url = f"https://some-random-api.ml/img/{'birb' if animal == 'bird' else animal}"

			async with request("GET", image_url, headers={}) as response:
				if response.status == 200:
					data = await response.json()
					image_link = data["link"]

				else:
					image_link = None
					

			async with request("GET", fact_url, headers={}) as response:
				if response.status == 200:
					data = await response.json()
					
					rand_colour = random.randint(0, 16777215)
					embed = discord.Embed(title=f"{animal.title()} fact",
								  description=data["fact"],
								  colour=rand_colour)
					embed.set_image(url=image_link)
					embed.set_author(icon_url=ctx.author.avatar_url, name=str(ctx.author))
					await ctx.send(embed=embed)

				else:
					await ctx.send(f"API returned a {response.status} status.")

		else:
			embed=discord.Embed(title=f"No facts are available for \'{animal}\'.", color=discord.Colour.red())
			await ctx.send(embed=embed)

		
	@commands.command(name="image", aliases=["img"])
	@cooldown(3, 60, BucketType.guild)
	async def animal_image(self, ctx, *, animal: str):
		if (animal := animal.lower()) in image_animal:
			
			if animal == "red panda":
				animal = "red_panda"
			
			image_url = f"https://some-random-api.ml/img/{'birb' if animal == 'bird' else animal}"

			async with request("GET", image_url, headers={}) as response:
				if response.status == 200:
					data = await response.json()
					image_link = data["link"]
					
					rand_colour = random.randint(0, 16777215)
					embed = discord.Embed(title=f"{animal.title()} image",
								  colour=rand_colour)
					embed.set_author(icon_url=ctx.author.avatar_url, name=str(ctx.author))
					if image_link is not None:
						embed.set_image(url=image_link)
					await ctx.send(embed=embed)

				else:
					await ctx.send(f"API returned a {response.status} status.")
					
		else:
			embed=discord.Embed(title=f"No images are available for \'{animal}\'.", color=discord.Colour.red())
			await ctx.send(embed=embed)
			
	@commands.command(name="pats", aliases=["pat"])
	@commands.guild_only()
	async def pat_gif(self, ctx, *, member: discord.Member=None):
		
		if not member:
				member = ctx.author
		
		
		pat_url = f"https://some-random-api.ml/animu/pat/"

		async with request("GET", pat_url, headers={}) as response:
			if response.status == 200:
				data = await response.json()
				pat_link = data["link"]
				
				rand_colour = random.randint(0, 16777215)
				if member == ctx.author:
					embed = discord.Embed(title=f"There there {member}", colour=rand_colour)
				else:
					embed = discord.Embed(title=f"{ctx.author} pats {member}", colour=rand_colour)

				if pat_link is not None:
					embed.set_image(url=pat_link)
					await ctx.send(embed=embed)
			else:
				embed=discord.Embed(title=f"No pat media available.", description="Let me pat you! there there~ *pats*", colour=rand_colour)
				await ctx.send(embed=embed)
				
	@commands.command(name="hug")
	@commands.guild_only()
	async def hug_gif(self, ctx, *, member: discord.Member=None):
		
		if not member:
				member = ctx.author
		
		
		hug_url = f"https://some-random-api.ml/animu/hug/"

		async with request("GET", hug_url, headers={}) as response:
			if response.status == 200:
				data = await response.json()
				hug_link = data["link"]
				
				rand_colour = random.randint(0, 16777215)
				if member == ctx.author:
					embed = discord.Embed(title=f"Hugs for {member}!", colour=rand_colour)
				else:
					embed = discord.Embed(title=f"{ctx.author} hugs {member}", colour=rand_colour)

				if hug_link is not None:
					embed.set_image(url=hug_link)
					await ctx.send(embed=embed)
			else:
				embed=discord.Embed(title=f"No hug media available.", description="I'll hug you! *hugs*", colour=rand_colour)
				await ctx.send(embed=embed)
				
	
	@commands.command(name="meme")
	@commands.guild_only()
	async def meme_gif(self, ctx):
		
		meme_url = f"https://some-random-api.ml/meme/"

		async with request("GET", meme_url, headers={}) as response:
			if response.status == 200:
				data = await response.json()
				meme_link = data["image"]
				category = data["category"]
				caption = data["caption"]
				meme_id = data["id"]
				
				
				rand_colour = random.randint(0, 16777215)
				
				embed = discord.Embed(title=f"Requested by: {ctx.author}", description=f"{caption}", colour=rand_colour)
				embed.set_footer(text=f"Meme Category: {category}")
				if meme_link is not None:
					embed.set_image(url=meme_link)
					await ctx.send(embed=embed)
					
				else:
					embed=discord.Embed(title="Something went wrong while loading the image.", colour=rand_colour)
					await ctx.send(embed=embed)
			
			else:
				embed=discord.Embed(title=f"Something went wrong. Better luck next time ಡ ͜ ʖ ಡ", colour=discord.Colour.red())
				await ctx.send(embed=embed)
				
	
			
			
	""" Canvas """


	""" Overlay """
	@commands.command(name="pfpc", aliases=["overlay", "ovrl"])
	@commands.guild_only()
	@cooldown(3, 60, BucketType.guild)
	async def av_overlay(self, ctx, overlay: str, *, member: discord.Member = None):
		
		if not member:
				member = ctx.author
		
		av_url = str(member.avatar_url)
		
		if (overlay := overlay.lower()) in ("gay", "wasted", "glass"):
		
			overlay_url = f"https://some-random-api.ml/canvas/{overlay}?avatar={av_url}"
			
			rand_colour = random.randint(0, 16777215)
			embed=discord.Embed(colour=rand_colour)
			embed.set_author(name=str(member))
			embed.set_footer(text=f"Requested by: {ctx.author}")
			embed.set_image(url=overlay_url)
			await ctx.send(embed=embed)
		else:
			embed=discord.Embed(title=f"No overlay named '{overlay}' available.", color=discord.Colour.red())
			await ctx.send(embed=embed)
	
	""" Filters """
	@commands.command(name="filter", aliases=["fltr"])
	@commands.guild_only()
	@cooldown(3, 60, BucketType.guild)
	async def canvas_filter(self, ctx, av_filter: str, *, member: discord.Member=None):
		
		if not member:
			member = ctx.author
		
		av_url = str(member.avatar_url)
		
		if (av_filter := av_filter.lower()) in filters:
			
			filter_url = f"https://some-random-api.ml/canvas/{av_filter}?avatar={av_url}"
			
			rand_colour = random.randint(0, 16777215)
			embed=discord.Embed(colour=rand_colour)
			embed.set_author(icon_url=member.avatar_url, name=str(member))
			embed.set_footer(text=f"Requested by: {ctx.author}")
			embed.set_image(url=filter_url)
			await ctx.send(embed=embed)
		
		
		
	@commands.command(aliases=["canvas"])
	@commands.guild_only()
	async def canvas_list(self, ctx, *, arg=None):
		
		
		rand_colour = random.randint(0, 16777215)
		
		embed=discord.Embed(title="Available arguments",colour=rand_colour)
		embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
		
		if arg == None:
			embed.add_field(name="Available Animal Names for Facts", value=fact_animal, inline=False)
			embed.add_field(name="Available Animal Names for Images", value=image_animal, inline=False)
			embed.add_field(name="Available Overlays", value=overlays, inline=False)
			embed.add_field(name="Available Filters", value=filters, inline=False)
			await ctx.send(embed=embed)
			
		elif arg == "fact" or arg=="facts":
			embed.add_field(name="Available Animal Names for Facts", value=fact_animal, inline=False)
			await ctx.send(embed=embed)
		elif arg == "image" or arg=="img":
			embed.add_field(name="Available Animal Names for Images", value=image_animal, inline=False)
			await ctx.send(embed=embed)
		
		elif arg == "filters" or arg == "filter":
			embed.add_field(name="Available Filters", value=filters, inline=False)
			await ctx.send(embed=embed)
		
		elif arg == "overlay" or arg == "overlays":
			embed.add_field(name="Available Overlays", value=overlays, inline=False)
			await ctx.send(embed=embed)
			
		else:
			embed=discord.Embed(title="Seems like you've typed something wrong.", colour=discord.Colour.red())
			await ctx.send(embed=embed)
		
		
def setup(bot):
	bot.add_cog(Fun(bot))