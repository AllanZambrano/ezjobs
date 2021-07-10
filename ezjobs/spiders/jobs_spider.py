import scrapy


class CsJobs(scrapy.Spider):
    name = "cs-jobs"

    start_urls = [
        'https://weworkremotely.com/categories/remote-customer-support-jobs#job-listings',
    ]          

    def parse(self, response):
        for jobs in response.css('.feature'):
            yield {
                'company': jobs.css(".company::text").get(), 
                'title': jobs.css(".title::text").get(),
                'location': jobs.css(".region::text").get(),
                'link': jobs.css("a::attr(href)").get(),
                'date': jobs.css(" a span.date time::text").get(default='NEW')
            }

# scrapy crawl cs-jobs -O csjobs.json
# https://livecodestream.dev/post/how-to-turn-the-web-into-data-with-python-and-scrapy/