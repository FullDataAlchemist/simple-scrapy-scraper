import json

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from sample import settings
from sample.spiders.exampleCrawler import ExamplecrawlerSpider
if __name__ == '__main__':
    my_settings = get_project_settings()
    # a = my_settings.get('REDIRECT_ENABLED')
    # a = my_settings.getlist('HTTPERROR_ALLOWED_CODES')

    my_settings.set('REDIRECT_ENABLED', False)
    my_settings.set('HTTPERROR_ALLOWED_CODES', [301, 302, 303])
    my_settings.attributes['BOT_NAME'].value = settings.BOT_NAME
    my_settings.attributes['SPIDER_MODULES'].value = settings.SPIDER_MODULES
    my_settings.attributes['ROBOTSTXT_OBEY'].value = False
    my_settings.attributes['NEWSPIDER_MODULE'].value = settings.NEWSPIDER_MODULE
    my_settings.attributes['USER_AGENT'].value = settings.USER_AGENT
    process = CrawlerProcess(my_settings)

    # process = CrawlerProcess({
    #     'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    #     'ROBOTSTXT_OBEY': False
    # })

    # process.crawl(ExamplespiderSpider)
    # process.start()  # the script will block here until the crawling is finished
    #
    process.crawl(ExamplecrawlerSpider)
    process.start()  # the script will block here until the crawling is finished


# class CustomDownloaderMiddleware:
#     def process_response(self, request, response, spider):
#         if response.status in [302, 303] and 'Location' in response.headers:  # and request.method != 'POST':
#             return request.replace(url=spider.start_urls[0], method='GET',
#                                    meta={'location': response.headers['location']})
#         return response
