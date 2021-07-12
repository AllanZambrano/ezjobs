import scrapy
from datetime import date, datetime
from urllib.parse import urljoin

d = date.today()

class CsJobs(scrapy.Spider):
    name = "cs-jobs"
    base = "https://weworkremotely.com"

    start_urls = [
        'https://weworkremotely.com/categories/remote-customer-support-jobs#job-listings',
    ]          

    def parse(self, response):
        for jobs in response.css('div.jobs-container ul li'):
            job_date = jobs.css("a span.date time").xpath('@datetime').get(default='2000-01-01T00:01:01Z')
            job_dt = datetime.strptime(job_date, "%Y-%m-%dT%H:%M:%S%z").date()
            if d == job_dt:       
                yield { 
                    'company': jobs.css("a span.company::text").get(), 
                    'title': jobs.css(".title::text").get(),
                    'location': jobs.css(".region::text").get(default='Check the post'),
                    'link': urljoin(self.base, ''.join(jobs.css("a::attr(href)").get())),
                    'date': jobs.css("a span.date time::text").get(default='NEW')
                }
            else:
                pass

# scrapy crawl cs-jobs -O csjobs.json
