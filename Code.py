import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def cat(ctx):
    Bibor = random.randint(1, 104)
    if Bibor == 30 or Bibor <= 30:
        with open('images/sigma.jpg', 'rb') as f:
            picture = discord.File(f)
        for i in range (3):
            if i == 1:
                await ctx.send(file=picture)
            if i == 2:
                await ctx.send('Шанс-30%')
    elif Bibor == 50 or Bibor <= 50 and Bibor >= 30:
        with open('images/pz.jpg', 'rb') as f:
            picture = discord.File(f)
        for i in range (3):
            if i == 1:
                await ctx.send(file=picture)
            if i == 2:
                await ctx.send('Шанс-20%')
    elif Bibor == 75 or Bibor <= 75 and Bibor >= 50:
        with open('images/angy.jpg', 'rb') as f:
            picture = discord.File(f)
        for i in range (3):
            if i == 1:
                await ctx.send(file=picture)
            if i == 2:
                await ctx.send('Шанс-15%')
    elif Bibor == 85 or Bibor <= 85 and Bibor >= 75:
        with open('images/hair.jpeg', 'rb') as f:
            picture = discord.File(f)
        for i in range (3):
            if i == 1:
                await ctx.send(file=picture)
            if i == 2:
                await ctx.send('Шанс-10%')
    elif Bibor == 90 or Bibor <= 90 and Bibor >= 85:
        with open('images/cute.jpg', 'rb') as f:
            picture = discord.File(f)
        for i in range (3):
            if i == 1:
                await ctx.send(file=picture)
            if i == 2:
                await ctx.send('Шанс-5%')
    elif Bibor == 95 or Bibor <= 95 and Bibor >= 90:
        with open('images/army.jpg', 'rb') as f:
            picture = discord.File(f)
        for i in range (3):
            if i == 1:
                await ctx.send(file=picture)
            if i == 2:
                await ctx.send('Шанс-5%')
    elif Bibor == 99 or Bibor <= 99 and Bibor >= 95:
        with open('images/silly.jpg', 'rb') as f:
            picture = discord.File(f)
        for i in range (3):
            if i == 1:
                await ctx.send(file=picture)
            if i == 2:
                await ctx.send('Шанс-4%')
    elif Bibor == 100 and Bibor >= 99:
        with open('images/cool.webp', 'rb') as f:
            picture = discord.File(f)
        for i in range (3):
            if i == 1:
                await ctx.send(file=picture)
            if i == 2:
                await ctx.send('Шанс-1%')
    elif Bibor == 102 or Bibor <= 102 and Bibor >= 100:
        with open('images/water.jpg', 'rb') as f:
            picture = discord.File(f)
        for i in range (3):
            if i == 1:
                await ctx.send(file=picture)
            if i == 2:
                await ctx.send('Шанс-2%')
    elif Bibor == 104 or Bibor <= 104 and Bibor >= 102:
        with open('images/chto.jpg', 'rb') as f:
            picture = discord.File(f)
        for i in range (3):
            if i == 1:
                await ctx.send(file=picture)
            if i == 2:
                await ctx.send('Шанс-2%')

bot.run('Token')
