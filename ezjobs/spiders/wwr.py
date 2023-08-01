import scrapy
from datetime import date, datetime, timedelta
from urllib.parse import urljoin
from ezjobs.items import JobsItem

today = date.today()
class wwr(scrapy.Spider):
    name = "wwr"
    base = "https://weworkremotely.com"
    custom_settings = {
        'FEEDS': {
                'wwr-jobs.json': {'format': 'json','overwrite': True}
                } 
            }
    start_urls = [
        'https://weworkremotely.com/categories/remote-customer-support-jobs#job-listings',
        'https://weworkremotely.com/categories/remote-design-jobs#job-listings',
        'https://weworkremotely.com/categories/remote-devops-sysadmin-jobs#job-listings',
        'https://weworkremotely.com/categories/remote-management-and-finance-jobs#job-listings',
        'https://weworkremotely.com/categories/remote-product-jobs',
        'https://weworkremotely.com/categories/remote-sales-and-marketing-jobs#job-listings',
        'https://weworkremotely.com/remote-full-time-jobs#job-listings',
        'https://weworkremotely.com/remote-contract-jobs#job-listings',
        'https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings',
        'https://weworkremotely.com/categories/remote-front-end-programming-jobs#job-listings', 
        'https://weworkremotely.com/categories/remote-back-end-programming-jobs#job-listings'
    ]          

    def parse(self, response):
        for jobs in response.css('article ul li'):
            job_date = jobs.css("a span.date time").xpath('@datetime').get(default='2000-01-01T00:01:01Z')
            job_dt = datetime.strptime(job_date, "%Y-%m-%dT%H:%M:%S%z").date()
            if today == job_dt: 
                yield {
                    'company': jobs.css("a span.company::text").get(),
                    'title': jobs.css(".title::text").get(),
                    'link': urljoin(self.base, ''.join(jobs.css("a::attr(href)").extract()[1])),
                    'region': jobs.css("span.region.company::text").get(),
                    'tags': jobs.css("span.company::text").extract()[1],
                    'date': today,
                    'crawled': 'WeWorkRemotely'
                }      
