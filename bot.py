import os
import discord
from dotenv import load_dotenv
import json
from discord.ext import commands
from datetime import date

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
d = date.today()
bot = commands.Bot(command_prefix='!')

@bot.command(name='jobs')
async def daily_jobs(ctx):
    await ctx.send("**Beep-boop bee-boop-boop beep beep beep boop!** \n\nHello, \@everyone :rocket: \nNew jobs found! \n\nBeep-bopp, I'm out.")
    
    with open(f'{d}.json', 'r') as f:
        jobs = json.load(f)
        
    for job in jobs:
        embed = discord.Embed(title= job['company'], description= job['title'], color = discord.Colour.random())
        embed.add_field(name="Location", value=job['location'])
        embed.add_field(name="Link", value= f"[Click here]({job['link']})")
        await ctx.send(embed=embed)
        
bot.run(TOKEN)