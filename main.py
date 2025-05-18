import discord, os
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot_token = os.getenv("DISCORD_BOT_TOKEN")
bot = commands.Bot(command_prefix='/', intents=intents) # Bot命令字首

@bot.event
async def on_ready():
    print(">>Bot is Online<<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(846291467595939900)
    await channel.send(f"{member} 剛剛插入!")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(846291467595939900)
    await channel.send(f"{member} 剛剛拔出!")


bot.run(token=bot_token)