from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()
class CleanNull(object):
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        # check if value is null
        if adapter.get('company'):
            #if ok, returns the item
            return item
        else:
            #if item is null, it drops it
            raise DropItem("Item is NULL")

class PostgresNoDuplicatesPipeline:

    def __init__(self):
        ## Connection Details
        hostname = os.getenv('DB_HOST')
        username = os.getenv('DB_USERNAME')
        password = os.getenv('DB_PASSWORD')
        database = os.getenv('DB_NAME')

        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        
        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()


    def process_item(self, item, spider):

        # IF psycopg2.errors.InFailedSqlTransaction: current transaction is aborted, 
        # commands ignored until end of transaction block
        # ROLLBACK
        # self.cur.execute("ROLLBACK")
        ## Check to see if link is already in database 
        self.cur.execute("select * from jobs where link = %s", (item['link'],))
        result = self.cur.fetchone()

        ## If it is in DB, create log message
        if result:
            spider.logger.warn("Item already in database: %s" %item['link'])


        ## If text isn't in the DB, insert data
        else:

            ## Define insert statement
            self.cur.execute(""" insert into jobs (company, title, link, region, tags, date, crawled) values (%s,%s,%s,%s,%s,%s,%s)""", (
                item['company'],
                item['title'],
                item['link'],
                item['region'],
                item['tags'],
                item['date'],
                item['crawled'],
        ))

            ## Execute insert of data into database
            self.connection.commit()
        return item

    
    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.connection.close()
