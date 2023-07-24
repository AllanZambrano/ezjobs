import os
import discord
from dotenv import load_dotenv
import json
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Json file
file_name = 'jobs.json'

#Intents
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='jobs')
async def daily_jobs(ctx):
    await ctx.send("**Beep-boop bee-boop-boop beep beep beep boop!** \n\nHello, \@everyone :rocket: \nNew jobs found! \n\nBeep-bopp, I'm out.")

    with open(file_name, 'r', encoding='utf-8') as f:
        jobs = json.load(f)

        for job in jobs:
            embed = discord.Embed(title= job['company'], description= job['title'], color = discord.Colour.random())
            embed.add_field(name="Location", value=job['location'])
            embed.add_field(name="Link", value= f"[Click here]({job['link']})")
            embed.add_field(name="Date", value= job['date'])
            await ctx.send(embed=embed)

@bot.command(name='test')
async def daily_jobs(ctx):
    await ctx.send("Beep-boop bee-boop-boop beep beep beep boop! \nThis is a test!:rocket: \n\nBeep-bopp, I'm out.")
               
bot.run(TOKEN)