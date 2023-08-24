import scrapy
# from bs4 import BeautifulSoup
from GeneralCrawler.items import GeneralcrawlerItem
from GeneralCrawler.database import DatabaseConnection
from scrapy_selenium import SeleniumRequest
from urllib.parse import urljoin
class GeneralSpider(scrapy.Spider):
    name = "general"
    
    def __init__(self): 
        self.db_connection = DatabaseConnection()
        self.connection = self.db_connection.get_connection()
    
    def start_requests(self):
        url = 'https://www.youtube.com'
        yield SeleniumRequest(url=url, callback=self.parse)
        
        
    def parse(self, response):
        # get all needed data from the response
        html_code = response.text
        # # text = BeautifulSoup(html_code, 'html.parser').get_text() 
        start_url = response.url
        urls = response.xpath('//a/@href').getall()
        title = response.css('title::text').get()
        # images = response.css('img::attr(src)').getall()
        # videos = response.css('video::attr(src)').getall()
        # audios = response.css('audio::attr(src)').getall()
        
        absolute_urls = [urljoin(start_url, link) for link in urls]
        vistied_urls = [] 
        conn = self.connection
        print(absolute_urls)
        select_query = "SELECT * FROM data WHERE url = %s"  
        cursor = conn.cursor()
        print("sending new requests")  
        for url in absolute_urls:
            if url not in vistied_urls:
                vistied_urls.append(url)
                cursor.execute(select_query, (url,))
                if cursor.fetchone():
                    continue
                else:
                    print(url)
                    yield SeleniumRequest(url=url, callback=self.parse)
        cursor.close()
        
        # create a new item
        item = GeneralcrawlerItem()
        #item['text'] = text
        item['url'] = start_url
        item['html'] = html_code
        item['title'] = title
        print("item created")
        yield item
    

