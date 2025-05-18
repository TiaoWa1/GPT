import discord, os, json, random
from discord.ext import commands
from core.classes import Cog_Extension

class Main(Cog_Extension):
    # 已從 /core/classes.py 中繼承
    # def __init__(self, bot):
    #     self.bot = bot

    @commands.command()
    async def ping(self, ctx): # ctx(context) 上下文，包含各種資訊如:user、id、所在伺服器、頻道
        await ctx.send(f"{round(self.bot.latency*1000)} ms")

async def setup(bot):
    await bot.add_cog(Main(bot))