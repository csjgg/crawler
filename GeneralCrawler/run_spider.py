import pymysql
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from GeneralCrawler.spiders.general import general

# fist_url = 'https://www.baike.baidu.com'

def read_urls_from_database():
    pass

def create_spider(url_list):
    class DynamicSpider(general):
        name = 'dynamic_spider'
        start_urls = url_list

    return DynamicSpider

if __name__ == '__main__':
    urls = read_urls_from_database()
    process = CrawlerProcess(get_project_settings())
    process.crawl(create_spider(urls))
    process.start()
