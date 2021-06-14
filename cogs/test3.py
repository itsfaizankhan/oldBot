import discord
from discord.ext import commands


class Test3(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Extension loaded: Test3")

    @commands.command(aliases=["among", "us"])
    async def among_us(self, ctx, imap: str, p_limit: int, im_limit: int, room_code: str, *, vc: str):

        member = ctx.author

        embed = discord.Embed(
            title="Matchmaking", desciption=f"Among Us announcement Command", colour=member.colour)
        embed.add_field(name="Map", value=f"{imap}", inline=False)
        embed.add_field(name="Max. Players", value=f"{p_limit}")
        embed.add_field(name="Imposter(s)", value=f"{im_limit}")
        embed.add_field(name="Room Code", value=f"||{room_code.upper()}||")
        embed.add_field(name="Vc to join", value=f"{vc}")

        embed.set_author(icon_url=member.avatar_url, name=member)

        await ctx.send(embed=embed)

    @among_us.error
    async def among_us_handler(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):

            if error.param.name == "imap":
                miss_para = "imap"
                miss_para = "Map Name"
            elif error.param.name == "p_limit":
                miss_para = "p_limit"
                miss_para = "Max. number of Players"
            elif error.param.name == "im_limit":
                miss_para = "im_limit"
                miss_para = "Number of Imposters"
            elif error.param.name == "room_code":
                miss_para = "room_code"
                miss_para = "Room Code"

            embed = discord.Embed(
                title="You missed something!", color=ctx.author.colour)
            embed.add_field(name="Last missing value",
                            value=f"{miss_para}", inline=True)
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Test3(bot))
