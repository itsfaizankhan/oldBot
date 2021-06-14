from discord.utils import get
from discord.ext import commands
from discord.ext.commands import has_permissions


class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Extension loaded: roles')

    @commands.command()
    async def ping_2(self, ctx):
        await ctx.send(f'Pong! (roles)')

    # Giving role via command

    @commands.command()
    @has_permissions(manage_roles=True)
    # This must be exactly the name of the appropriate role
    @commands.has_role("Moderator")
    async def addrole_ext(self, ctx, ROLE: str):
        member = ctx.message.author
        role = get(member.guild.roles, name=ROLE)
        await member.add_roles(role)
        await ctx.message.channel.send(f"Given role: {ROLE}")

    @commands.command()
    @has_permissions(manage_roles=True)
    # This must be exactly the name of the appropriate role
    @commands.has_role("Moderator")
    # Removing role via command
    async def removerole_ext(self, ctx, ROLE: str):
        member = ctx.message.author
        role = get(member.guild.roles, name=ROLE)
        await member.remove_roles(role)
        await ctx.message.channel.send(f"Removed role: {ROLE}")


def setup(bot):
    bot.add_cog(Roles(bot))
