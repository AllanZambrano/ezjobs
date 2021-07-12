import scrapy
from datetime import date, datetime
from urllib.parse import urljoin
from ezjobs.items import *


d = date.today()

class CsJobs(scrapy.Spider):
    name = "jobs"
    base = "https://weworkremotely.com"

    start_urls = [
        'https://weworkremotely.com/categories/remote-customer-support-jobs#job-listings',
    ]          

    def parse(self, response):
        job = Jobs()
        for jobs in response.css('div.jobs-container ul li'):
            job_date = jobs.css("a span.date time").xpath('@datetime').get(default='2000-01-01T00:01:01Z')
            job_dt = datetime.strptime(job_date, "%Y-%m-%dT%H:%M:%S%z").date()
            if d == job_dt:       
                job['company'] = jobs.css("a span.company::text").get(), 
                job['title'] = jobs.css(".title::text").get(),
                job['location'] = jobs.css(".region::text").get(default='Check the post'),
                job['link'] = urljoin(self.base, ''.join(jobs.css("a::attr(href)").get())),
#                jobs['date'] = jobs.css("a span.date time::text").get(default='NEW')
                yield job
            else:
                pass

# scrapy crawl cs-jobs -O csjobs.json
