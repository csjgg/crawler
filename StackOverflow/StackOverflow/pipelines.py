# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class StackoverflowPipeline:
    def process_item(self, item, spider):
        with open("stackoverflow.txt", "a", encoding="utf-8") as f:
            f.write(item["question"] + "\n")
            f.write(item["url"] + "\n")
            f.write(item["detail"] + "\n")
        return item
