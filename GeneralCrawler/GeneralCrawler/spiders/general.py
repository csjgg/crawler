import scrapy
# from bs4 import BeautifulSoup
from GeneralCrawler.items import GeneralcrawlerItem
from pymysql import Connection


class GeneralSpider(scrapy.Spider):
    name = "general"
    start_urls = ["https://jyywiki.cn/OS/2022/"]
    
    def connect_to_database(self):
        conn = Connection(
            host='localhost',
            port=3306,
            user = 'root',
            password = '123456',
            database='test_crawler',
        )
        if not conn:
            print("connect to database failed.")
            exit(1)
        else:
            print("connect to database successfully.")
            return conn
    
    
    def parse(self, response):
        # get all needed data from the response
        html_code = response.text
        # text = BeautifulSoup(html_code, 'html.parser').get_text() 
        start_url = response.url
        urls = response.xpath('//a/@href').getall()
        title = response.css('title::text').get()
        # images = response.css('img::attr(src)').getall()
        # videos = response.css('video::attr(src)').getall()
        # audios = response.css('audio::attr(src)').getall()

        # deal with urls
        absolute_urls = [response.urljoin(url) for url in urls]
        vistied_urls = [] 
        conn = self.connect_to_database()
        select_query = "SELECT * FROM data WHERE url = %s"
        cursor = conn.cursor()   
        for url in absolute_urls:
            if url not in vistied_urls:
                vistied_urls.append(url)
                cursor.execute(select_query, (url,))
                if cursor.fetchone():
                    continue
                else:
                    print("Send New Request")
                    yield scrapy.Request(url, callback=self.parse)
        cursor.close()
        conn.close()
        
        # create a new item
        item = GeneralcrawlerItem()
        #item['text'] = text
        item['url'] = start_url
        item['html'] = html_code
        item['title'] = title
        yield item


