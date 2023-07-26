import scrapy
from datetime import date, datetime
from urllib.parse import urljoin
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

d = date.today()

class wwr(scrapy.Spider):
    name = "wwr"
    base = "https://weworkremotely.com"
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
            if d == job_dt: 
                yield {
                    'company': jobs.css("a span.company::text").get(),
                    'title': jobs.css(".title::text").get(),
                    'location': jobs.css(".region::text").get(default='Check the post'),
                    'link': urljoin(self.base, ''.join(jobs.css("a::attr(href)").extract()[1])),
                    'date': jobs.css("a span.date time::text").get()
                }      
            else:
                pass


class remotive(scrapy.Spider):
    name = "remotive"
    base = "https://remotive.com/?locations=Worldwide"
    start_urls = [
        'https://remotive.com/remote-jobs/customer-support',
        'https://remotive.com/remote-jobs/software-dev',
        'https://remotive.com/remote-jobs/customer-support',
        'https://remotive.com/remote-jobs/design',
        'https://remotive.com/remote-jobs/marketing',
        'https://remotive.com/remote-jobs/sales', 
        'https://remotive.com/remote-jobs/product', 
        'https://remotive.com/remote-jobs/data', 
        'https://remotive.com/remote-jobs/devops', 
        'https://remotive.com/remote-jobs/finance-legal', 
        'https://remotive.com/remote-jobs/hr', 
        'https://remotive.com/remote-jobs/qa', 
        'https://remotive.com/remote-jobs/writing', 
        'https://remotive.com/remote-jobs/all-others',
    ]          

    def parse(self, response):
        for list in response.css('div#initial_job_list ul li'):
            if list.css('span.tw-text-xs.tw-mr-4::text').get(default='').strip() == 'YDay':
                yield {
                    'company': list.css('div.job-tile-title a.remotive-url-visit span::text').extract()[2],
                    'title': list.css('div.job-tile-title a.remotive-url-visit span::text').extract()[0],
                    'date': list.css('span.tw-text-xs.tw-mr-4::text').get().strip(),
                    'link': urljoin(self.base, ''.join(list.css('a.job-tile-apply::attr("href")').get())),
                }
            else:
                pass
# https://docs.scrapy.org/en/latest/topics/practices.html#running-multiple-spiders-in-the-same-process
settings = get_project_settings()
process = CrawlerProcess(settings)
process.crawl(wwr)
process.crawl(remotive)
process.start() 