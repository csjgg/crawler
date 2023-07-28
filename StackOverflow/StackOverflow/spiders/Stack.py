import scrapy
from StackOverflow.items import StackoverflowItem

class StackSpider(scrapy.Spider):
    name = "Stack"
    # allowed_domains = ["www.ss.com"]
    start_urls = ["https://stackoverflow.com/questions"]
    url = "https://stackoverflow.com/questions?tab=newest&page=%d"
    page_num = 2
    
    # deal with the detail page
    def parse_detail(self, response):
        item = response.meta["item"]
        detail = response.xpath('//*[@id="question"]/div[2]/div[2]/div[1]//text()').extract()
        question = response.xpath('//*[@id="question-header"]/h1/a//text()').extract()
        join_detail = "".join(detail)
        join_question = "".join(question)
        item["question"] = join_question
        item["detail"] = join_detail
        yield item
        
    # deal with the main page
    def parse(self, response):
        div_list = response.xpath('/html/body/div[4]/div[2]/div[1]/div[3]/div')
        main_url = "https://stackoverflow.com"
        for div in div_list:
            item = StackoverflowItem()
            href = div.xpath('./div[2]/h3/a/@href').extract_first()
            final_url = main_url + href
            item["url"] = final_url
            yield scrapy.Request(url=final_url, callback=self.parse_detail,meta={"item":item})
        # deal with the next page
        if self.page_num <= 3:
            new_url = format(self.url % self.page_num)
            self.page_num += 1
            yield scrapy.Request(url=new_url, callback=self.parse)
