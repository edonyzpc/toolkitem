import scrapy

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
