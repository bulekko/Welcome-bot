#importy
import discord
from discord.ext import commands
from discord import app_commands
from discord.app_commands import Choice
import random

#zmienne
list = ['your phrases', 'your phrases']
channel-id = #Welcome channel id in here

#potrzebne
intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)
bot.guilds

#Wiadmomość uruchomienia
@bot.event
async def on_ready():
    print("online")
    try:
        synced = await bot.tree.sync()
        print(f"Zynschronizowano {len(synced)}")
    except Exception as e:
        print(e)

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(channel-id)
    
    random_slowo = random.choice(list)
    embed = discord.Embed(
    title=f"Welcome {member.name}", 
    description=random_world, 
    color=discord.Color.green()
    )

    if channel:
        await channel.send(embed=embed)

bot.run(your token)
