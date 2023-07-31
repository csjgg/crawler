import scrapy


class GeneralSpider(scrapy.Spider):
    name = "general"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://www.xxx.com"]

    def parse(self, response):
        pass
