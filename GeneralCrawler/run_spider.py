import time
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from GeneralCrawler.spiders.general import GeneralSpider

first_url = ["https://jyywiki.cn/OS/2022/"]

def read_urls_from_database():
    # 假设从数据库中读入数据
    url = ["http://example.com/page1"]
    id = 1
    return [None,id]

def create_spider(url_list,id):
    class DynamicSpider(GeneralSpider):
        name = 'dynamic_spider'
        start_urls = url_list
        docid = id

    return DynamicSpider

def run_first_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(create_spider(first_url,1))
    process.start()
    process.join()

def run_spider():
    while True:
        [url,id] = read_urls_from_database()
        if not url:
            # 
            print("no urls in database, wait for 20 seconds.")
            time.sleep(20)
            url = read_urls_from_database()
            if not url:
                print("No urls in database, exit.")
                break
        process = CrawlerProcess(get_project_settings())
        process.crawl(create_spider(url,id))
        process.start()


if __name__ == '__main__':
    run_first_spider()
    run_spider()