# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from GeneralCrawler.database import DatabaseConnection
import time 

class GeneralcrawlerPipeline:
    
    def __init__(self):
        self.db_connection = DatabaseConnection()
        self.connection = self.db_connection.get_connection()
        
        
    def process_item(self, item, spider):
        # deal with the database
        conn = self.connection
        # print("database connected.")
        cursor = conn.cursor()
        insert_query = "INSERT INTO data (path, url, title) VALUES (%s, %s, %s)"
        select_query = "SELECT * FROM data WHERE url = %s"
        
        # store data in the local file system
        path = './Filebase/'+str(item['title'])+'.html'
        # fp = open(path, 'w',encoding='utf-8')
        # if fp:
        #     fp.write(item['html'])
        #     print("Save new file in local")
        #     fp.close()
        # else:
        #     print("open file failed.")
        # save the path item['title'] item['url'] to database
        cursor.execute(select_query, (item['url']))
        if cursor.fetchone():
            # print("data already exists.")
            cursor.close()
        else:
            cursor.execute(insert_query, (path, item['url'], item['title']))
            conn.commit()
            cursor.close()
            print("save data to database successfully.")
        return item
    
    def close_spider(self, spider):
        self.connection.close()