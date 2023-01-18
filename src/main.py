import traceback
import os

import scrapy as scrapy
from scrapy.crawler import CrawlerProcess

from utils.page_processor import process_page

# TARGET_ENDPOINT = 'https://www.herbalife.es'
# TARGET_ENDPOINT = 'https://www.herbalife.com/region-links'
# TARGET_ENDPOINT = 'https://www.herbalife.com/es/productos/tonificador-energizante-de-hierbas-herbalife-50ml/'
# TARGET_ENDPOINT = 'https://www.herbalife.es/productos/244k-formula-1-chocolate-y-naranja-550g/'
# TARGET_ENDPOINT = 'https://www.herbalife.es/nuestros-productos/complementos/proteinas/'
# AVAILABLE_DOMAINS = ['https://www.herbalife.ie', 'https://herbalife.ru', 'https://www.herbalife.pt', 'https://www.herbalife.ee', 'http://www.herbalifeuruguay.com', 'https://www.herbalife-zambia.com', 'http://www.herbalife.com.sv', 'https://www.herbalife.pr', 'http://www.herbalife.co.jp', 'http://www.herbalife.com.hn', 'http://www.herbalife.co.ve', 'http://www.herbalifeghana.com', 'http://www.herbalife.com.bo', 'http://www.herbalife-aruba.com', 'https://www.herbalife.gr', 'http://www.herbalife.ca', 'https://www.herbalife.tt', 'https://www.skherbalife.sk', 'https://www.herbalife.se', 'http://www.herbalife.co.za', 'https://www.herbalife.is', 'http://www.herbalife.com.sg', 'https://support.herbalife.com', 'http://www.herbalife.com.pa', 'http://www.herbalife.cn', 'http://www.herbalife.com.ec', 'https://www.herbalife.no', 'http://www.herbalife.com.py', 'https://www.herbalife.nl', 'https://www.herbalife.bg', 'https://www.herbalife-swaziland.com', 'https://twitter.com', 'https://www.herbalifeserbia.com', 'https://www.herbalife.at', 'https://www.herbalife.ro', 'http://www.herbalife.com.ph', 'http://www.herbalife.co.in', 'http://www.herbalife.com.do', 'http://www.herbalife.com.ni', 'https://www.herbalife.am', 'https://www.facebook.com', 'https://www.herbalife.it', 'https://www.herbalife.md', 'https://www.herbalife.mk', 'http://www.herbalife.com.my', 'http://www.herbalife.com.gt', 'http://www.herbalife-lebanon.com', 'https://www.herbalife.mn', 'http://www.herbalife.co.kr', 'https://www.herbalife.com.na', 'https://www.herbalife.kg', 'https://www.herbalife.ua', 'http://www.herbalife.com.hk', 'https://www.herbalife.com.jm', 'https://www.herbalifemalta.com', 'http://www.herbalife.cr', 'https://assets.herbalifenutrition.com', 'https://www.herbalife.si', 'https://www.herbalife.hr', 'http://www.herbalife.com.mx', 'https://herbalifeuzbekistan.com', 'https://www.herbalife.hu', 'https://www.herbalife.be', 'http://www.herbalife.com.kh', 'https://www.herbalife.dk', 'https://herbalifekazakhstan.com', 'https://www.herbalife.lv', 'http://www.herbalife.cl', 'https://www.herbalife.es', 'https://iamherbalifenutrition.com', 'https://www.herbalife.com.cy', 'https://www.herbalife.co.ls', 'http://www.herbalife.com.tr', 'http://www.herbalife.co.th', 'https://www.bbb.org', 'http://www.herbalife.com.tw', 'https://business.herbalife.com', 'https://www.herbalife-bih.com', 'https://www.herbalife.ch', 'https://www.herbalife.co.uk', 'https://www.herbalife.pl', 'https://www.herbalifefrance.fr', 'http://www.herbalife.com.br', 'https://www.herbalife.com', 'http://www.herbalife-vietnam.com', 'https://www.herbalife.co.il', 'https://www.herbalife.de', 'https://www.herbalife.cz', 'https://www.herbalife.fi', 'https://www.herbalife.co.bw', 'http://www.herbalife.com.au', 'http://www.herbalife.com.co', 'http://www.herbalife.com.pe', 'https://www.herbalife.by', 'http://www.herbalife.co.id', 'https://www.herbalife.ge', 'https://www.herbalife.az', 'https://www.herbalife.lt']
AVAILABLE_DOMAINS = ['https://www.herbalife.es', 'https://www.herbalife.it', 'https://www.herbalife.co.uk', 'https://www.herbalifefrance.fr', 'https://www.herbalife.de', 'https://www.herbalife.pt', 'https://www.herbalife.nl']


class BlogSpider(scrapy.Spider):
    name = 'herbaspider'
    start_urls = AVAILABLE_DOMAINS

    custom_settings = {
        'DOWNLOAD_DELAY': 6,
    }

    def parse(self, response):
        try:
            process_page(response.url, response.text)
        except Exception as e:
            print("ERROR!!!")
            print(e)
            print(traceback.format_exc())
            return

        for link in response.css('a'):
            if link.attrib.get('href'):
                target_url = link.attrib.get('href')
                if list(filter(lambda x: x.replace('www.', '').replace("http://", '').replace("https://", "") in target_url, AVAILABLE_DOMAINS)):
                    if not 'mailto:' in target_url:
                        yield response.follow(link.attrib['href'], self.parse)


process = CrawlerProcess()

process.crawl(BlogSpider)
process.start()  # the script will block here until the crawling is finished