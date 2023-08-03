# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class GeneralcrawlerPipeline:
    def process_item(self, item, spider):
        path = './Filebase/'+item['title']+'/source.html'
        fp = open(path, 'a', encoding='utf-8')
        fp.write(item['html'])
        fp.close()
        fp2 = open('./Filebase/'+item['title']+'/url.txt', 'a', encoding='utf-8')
        fp2.write(path+'\n'+item['url']+'\n')
        fp2.close()
        return item
