import discord, os, json, random
from discord.ext import commands
from core.classes import Cog_Extension

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

with open("./img/url_img.json") as img_fp:
    img_url = json.load(img_fp)

class React(Cog_Extension):
    @commands.command()
    async def 圖片(self, ctx):
        picture = discord.File(jdata["img_src"])
        await ctx.send(file = picture)

    @commands.command()
    async def 隨機圖片(self, ctx):

        picture = discord.File(random.choice(img_url["img_src"]))
        await ctx.send(file = picture)

async def setup(bot):
    await bot.add_cog(React(bot))