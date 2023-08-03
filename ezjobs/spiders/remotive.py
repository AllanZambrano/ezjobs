import scrapy
from urllib.parse import urljoin
from datetime import date, timedelta 

today = date.today()

class remotive(scrapy.Spider):
    name = "remotive"
    base = "https://remotive.com/"
    custom_settings = {
        'FEEDS': {
                'remotive-jobs.json': {'format': 'json','overwrite': True}
                } 
            }
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
            location = list.css("span.job-tile-location::text").extract()[1].strip()
            if list.css('span.tw-text-xs.tw-mr-4::text').get(default='').strip() == 'YDay':
                if (location != 'USA Only'):
                    yield {
                        'company': list.css('div.job-tile-title a.remotive-url-visit span::text').extract()[2],
                        'title': list.css('div.job-tile-title a.remotive-url-visit span::text').extract()[0],
                        'link': urljoin(self.base, ''.join(list.css('a.job-tile-apply::attr("href")').get())),
                        'region': list.css("span.job-tile-location::text").extract()[1].strip(),
                        'tags': list.css("a.job-tile-category::text").get(),
                        'date': today - timedelta(days = 1),
                        'crawled': 'Remotive'
                    }