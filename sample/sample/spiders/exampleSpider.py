import scrapy


class ExamplespiderSpider(scrapy.Spider):
    name = 'exampleSpider'
    allowed_domains = ['eghtesadonline.com']
    start_urls = ['http://eghtesadonline.com/']

    def parse(self, response):
        pass
