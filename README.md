# EzJobs: Job Data Crawler and Discord Bot

This GitHub repository consists of two parts: a Crawler and a Discord Bot. The Crawler is a Scrapy-based application designed to extract structured job data from WeWorkRemotely.com and post it to our Discord Bot.

## Crawler:

The EzJobs Crawler is a powerful web scraping application built using Scrapy. Its primary purpose is to crawl WeWorkRemotely.com and extract valuable job data, including company details, job titles, locations, and job links. The crawled data is then parsed and utilized by our Discord Bot.

To run the Crawler and obtain job data in a JSON format, execute the following command in your terminal:

```terminal
scrapy crawl jobs
```

This command will create a `jobs.json` file containing all the data crawled from WeWorkRemotely. Subsequently, this data will be used by the Discord Bot to post the latest job updates.

You can find the relevant code responsible for the data extraction in the `ezjobs/spiders/cs_spider.py` file under the yield information section.

## Discord Bot:

To interact with the EzJobs Discord Bot, you'll need to create an application on the Discord Developer Portal. You can find the portal at: [https://discord.com/developers/applications](https://discord.com/developers/applications)

Once you've created your application, use the `bot.py` script to run the Discord Bot. Simply execute the following command in your terminal:

```terminal
python3 bot.py
```

The bot will be up and running, processing the job data from the Crawler and posting it to your Discord channel.

### Setup:

Before running the Crawler and the Discord Bot, make sure you have Scrapy installed. If you don't have Scrapy installed, you can refer to this [guide](https://docs.scrapy.org/en/latest/intro/install.html) for installation instructions.

Additionally, our Discord Bot utilizes Discordpy to embed the job data seamlessly. If you need to learn more about Discordpy and its functionalities, you can review their documentation [here](https://discordpy.readthedocs.io/en/stable/).

### To Do Improvements:

We have identified some areas for improvement in our project:

1. **Enhance Job Links**: Improve the handling of job links to ensure easy access to the original job postings from within Discord.
2. **Code Refactoring**: Clean up the code in `cs_spider.py` and pipeline to enhance readability and maintainability.

### Reference:

If you'd like to learn more about building Discord bots in Python, you can check out this article: [https://builtin.com/software-engineering-perspectives/discord-bot-python](https://builtin.com/software-engineering-perspectives/discord-bot-python)

We welcome your contributions and suggestions to make EzJobs even better! Feel free to fork this repository and submit pull requests to help us grow and improve the project. Happy job hunting!