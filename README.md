# EzJobs Crawler

## Overview: 

EzJobs consists of 2 parts: 
1. Crawler
2. Discord Bot

### Crawler:

EzJobs Crawler is an crawler application created by using Scrapy. The main goal for it is to crawl web sites and extracting structured data, for this specific crawler, we'll crawl data from WeWorkRemotely.com and then parse it through Discord. 

For running the crawler, you can run the following command: 
> scrapy crawl jobs -O jobs.json

This will create a JSON file with the data that was crawled from WeWorkRemotely and then by using the Bot.py, it will embed the json content and post it to the our Discord Bot. 

The data that crawls specific is: 
1. Company
2. Title of the job
3. Location
4. Link

You can review this on the file `ezjobs/spiders/cs_spider.py/` under the yield information. 

### Discord Bot

You'll need to create an application on the discord developer link: https://discord.com/developers/applications
For this, you'll use `bot.py`. 

To run the bot, you'll need to run `bot.py` on the terminal use:
> python3 bot.py 

### Setup
In order to setup the crawler and run it, you'll need to install Scrapy. 
For this, you can follow this [guide](https://docs.scrapy.org/en/latest/intro/install.html)

Also, we use Discordpy to embed our json data. 
You can reviw their documentation [here](https://discordpy.readthedocs.io/en/stable/).

### To do improvement:
- Link can be improved to access the link and retrieve the specific link from the site. 
- Clean code on cs_spider.py

### Reference: 
https://builtin.com/software-engineering-perspectives/discord-bot-python
