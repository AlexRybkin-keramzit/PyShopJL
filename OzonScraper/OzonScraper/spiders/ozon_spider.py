import scrapy
from OzonScraper.dynamic_page_download import smartphone_links
from OzonScraper.items import OzonscraperItem


class OzonScraperSpider(scrapy.Spider):
    name = 'ozon_scraper'
    start_urls = smartphone_links()

    def parse(self, response, **kwargs):
        item = OzonscraperItem()
        brand = response.xpath('//*[contains(text(), "Android")]').getall()
        if len(brand) > 0:
            android = response.xpath('//*[contains(text(), "Android ")]/text()').getall()
            if len(android) == 1:
                item['operation_system'] = android[0]
            elif len(android) == 3:
                item['operation_system'] = android[1]
            else:
                item['operation_system'] = 'Android x.'
        else:
            ios = response.xpath('//*[contains(text(), "iOS ")]/text()').getall()
            if len(ios) == 3:
                item['operation_system'] = ios[1]
            elif len(ios) == 1:
                item['operation_system'] = ios[0]
            else:
                item['operation_system'] = 'iOS'
        yield item
