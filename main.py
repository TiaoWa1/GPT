import discord, os, json, random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class Mybot(commands.Bot):
    async def setup_hook(self):
        for filename in os.listdir("./cmds"): # os.listdir 列出資料夾下的所有文件
            if filename.endswith(".py"):
                try:
                    await self.load_extension(f"cmds.{filename[:-3]}")
                    print(f"✅ Loaded {filename}")
                except Exception as e:
                    print(f"❌ Failed to load {filename}: {e}")

bot_token = os.getenv("DISCORD_BOT_TOKEN")
bot = Mybot(command_prefix='~', intents=intents) # command_prefix Bot命令字首

with open('setting.json', mode='r', encoding='utf8') as jfile:
    jdata = json.load(jfile)

@bot.event # 裝飾器 bot.event 代表被動觸發事件
async def on_ready():
    print(">>Bot is Online<<")

@bot.event
async def on_member_join(member): # 成員加入
    channel = bot.get_channel(int(jdata["channel_id"]))
    await channel.send(f"{member} 剛剛插入!")

@bot.event
async def on_member_remove(member): # 成員退出
    channel = bot.get_channel(int(jdata["channel_id"]))
    await channel.send(f"{member} 剛剛拔出!")

if __name__ == "__main__":
    bot.run(token=bot_token)