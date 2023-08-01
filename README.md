# EzJobs: Job Data Crawler

The crawler primary purpose is to crawl jobs from job boards and extract valuable job data, including company details, job titles, locations, and job links. 

## Setup:
Before using the Scrapy Crawler Bot, follow these steps to set up your environment:

1. Install the required packages by running the following commands in your terminal:

```terminal
pipenv shell
pipenv install

```

2. Create an .env file with the following requiements: 

```terminal
DB_HOST='YOURHOST'
DB_NAME='YourDB'
DB_USERNAME='YourUsername'
DB_PASSWORD='YourPassword!'
```

3. To run the Crawler and obtain job data in a JSON format, execute the following command in your terminal:

```terminal
scrapy crawl wwr 
scrapy crawl remotive
# We use different crawlers for every page
```

This command will create a `{{wwr/remotive}}.json` file containing all the data crawled from the job boards and also save it on your database.

You can find the relevant code responsible for the data extraction in the `ezjobs/spiders/wwr.py` & `ezjobs/spiders/remotive.py` file under the yield information section.

### Reference:

Before running the Crawler and the Discord Bot, make sure you have Scrapy installed. If you don't have Scrapy installed, you can refer to this [guide](https://docs.scrapy.org/en/latest/intro/install.html) for installation instructions.

Additionally, our Discord Bot utilizes Discordpy to embed the job data seamlessly. If you need to learn more about Discordpy and its functionalities, you can review their documentation [here](https://discordpy.readthedocs.io/en/stable/).

If you'd like to learn more about building Discord bots in Python, you can check out this article: [https://builtin.com/software-engineering-perspectives/discord-bot-python](https://builtin.com/software-engineering-perspectives/discord-bot-python)

We welcome your contributions and suggestions to make EzJobs even better! Feel free to fork this repository and submit pull requests to help us grow and improve the project. Happy job hunting!