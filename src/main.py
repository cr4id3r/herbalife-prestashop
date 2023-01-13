import scrapy as scrapy
from scrapy.crawler import CrawlerProcess

from utils.page_processor import process_page

TARGET_ENDPOINT = 'https://www.herbalife.es/nuestros-productos/todos-los-productos/'


class BlogSpider(scrapy.Spider):
    name = 'herbaspider'
    start_urls = [TARGET_ENDPOINT]

    custom_settings = {
        'DOWNLOAD_DELAY': 6,
    }


    def parse(self, response):

        process_page(response.url, response.text)

        for link in response.css('.cmp-contentfragment__element.cmp-contentfragment__element--title-text-link a'):
            yield response.follow(link.attrib['href'], self.parse)

        for link in response.css('.cmp-list__item-link'):
            yield response.follow(link.attrib['href'], self.parse)

        for link in response.css('.cmp-teaser__action-link'):
            yield response.follow(link.attrib['href'], self.parse)


process = CrawlerProcess()

process.crawl(BlogSpider)
process.start()  # the script will block here until the crawling is finished