import hashlib

import scrapy
from scrapy.http import HtmlResponse
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy.utils.response import open_in_browser

from sample.spiders import utils


class ExamplecrawlerSpider(CrawlSpider):
    name = 'exampleCrawler'
    dn = 'eghtesadonline.com'
    allowed_domains = ['eghtesadonline.com']
    start_urls = ['http://eghtesadonline.com/']
    cat = ''
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parsepage', follow=True),
    )

    def parse_item(self, response):
        item = {}
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        return item

    def extract_data(self, response: HtmlResponse):
        article = utils.paring_html(url=response.url, html_body=response.text)
        keywords = utils.get_top_n_keywords(article)
        res = dict()
        res['html'] = response.text
        res['url'] = response.url
        res['text'] = article.text
        res['title'] = article.title
        res['keywords'] = keywords
        res['cat'] = ExamplecrawlerSpider.cat

        utils.json_writer(domain=ExamplecrawlerSpider.dn,
                          cat=hashlib.sha1(ExamplecrawlerSpider.cat.encode()).hexdigest(),
                          name=hashlib.sha1(response.url.encode()).hexdigest(),
                          out_data=res)

    def parsepage(self, response):
        self.extract_data(response)

    def parse_details(self, response):
        if "item name" not in response.body:
            open_in_browser(response)
