# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GeneralcrawlerPipeline:
    def process_item(self, item, spider):
        path = './Filebase/'+str(item['id'])+'.html'
        print(item['id'])
        with open(path, 'w', encoding='utf-8') as fp:
            fp.write(item['html'])
        # with open('./urls.txt', 'w', encoding='utf-8') as fp:
        #     for url in item['relevent_urls']:
        #         fp.write(url+'\n')
        # 要提交的： 将 path item['title'] item['url'] 上传到数据库id下 ////// 将 item['relevent_urls'] 上传并自动生成id
        
        return item
