import scrapy
from datetime import date, datetime
from urllib.parse import urljoin

date_time = date.today()

class CsJobs(scrapy.Spider):
    name = "date-jobs"
    base = "https://weworkremotely.com"

    start_urls = [
        'https://weworkremotely.com/categories/remote-customer-support-jobs#job-listings',
    ]          

    def parse(self, response):
        for jobs in response.css('.feature'):
            d = date_time.strftime("%Y-%m-%d")
            job_date = jobs.css("a span.date time").xpath('@datetime').get(default='2000-01-01T00:01:01Z')
            job_dt = datetime.strptime(job_date, "%Y-%m-%dT%H:%M:%S%z")
            if d >= job_date:         
                yield { 
                    'company': jobs.css(".company::text").get(), 
                    'title': jobs.css(".title::text").get(),
                    'location': jobs.css(".region::text").get(),
                    'link': urljoin(self.base, ''.join(jobs.css("a::attr(href)")[1].get())),
                    'date': jobs.css(" a span.date time::text").get(default='NEW')
                }
            else:
                return

# scrapy crawl date-jobs -O datejobs.json
# https://livecodestream.dev/post/how-to-turn-the-web-into-data-with-python-and-scrapy/

# todo
# fix the date since it's not getting the dates properly
