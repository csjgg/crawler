import scrapy
from bs4 import BeautifulSoup
from GeneralCrawler.items import GeneralcrawlerItem



class GeneralSpider(scrapy.Spider):
    name = "general"
    id = 0
    def parse(self, response):
        # get all needed data from the response
        html_code = response.text
        text = BeautifulSoup(html_code, 'html.parser').get_text() 
        start_url = response.url
        urls = response.xpath('//a/@href').getall()
        title = response.css('title::text').get()
        '''
        images = response.css('img::attr(src)').getall()
        videos = response.css('video::attr(src)').getall()
        audios = response.css('audio::attr(src)').getall()
        '''

        # deal with them
        absolute_urls = [response.urljoin(url) for url in urls]
        
        # create a new item
        item = GeneralcrawlerItem()
        item['id'] = self.id
        item['text'] = text
        item['url'] = start_url
        item['html'] = html_code
        item['title'] = title
        item['relevent_urls'] = absolute_urls
        yield item


