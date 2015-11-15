import scrapy
from walker_tmp.items import WalkerTmpItem

class WalkerTmpSpider(scrapy.Spider):
    name = 'walker_tmp'
    allowed_domains = ['dmoz.org']
    start_urls = [
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
            "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
    
    def parse(self, response):
        filename = response.url.split("/")[-2] + ".html"
        with open(filename, 'wb') as f:
            f.write(response.body)
        for sel in response.xpath('//ul/li'):
            item = WalkerTmpItem()
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item
