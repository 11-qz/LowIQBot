from discord.ext import commands
 #gives access to the bot instance
class GeneralCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f"Hello {ctx.author.mention}!")

# register cog with the bot
def setup(bot):
    bot.add_cog(GeneralCommands(bot))
