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


class PostgresPipeline:

    def __init__(self):
        ## Connection Details
        hostname = os.getenv('hostname')
        username = os.getenv('username')
        password = os.getenv('password')
        database = os.getenv('database')
        

        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        
        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()
        
        ## Create quotes table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS jobs(
            id serial PRIMARY KEY, 
            company varchar (150) NOT NULL,
            title varchar (150) NOT NULL,
            link text NOT NULL,
            date text NOT NULL
        )
        """)

    def process_item(self, item, spider):

        ## Define insert statement
        self.cur.execute(""" insert into jobs (company, title, link, date) values (%s,%s,%s,%s)""", (
            item['company'],
            item['title'],
            item['link'],
            item['date']
        ))

        ## Execute insert of data into database
        self.connection.commit()
        return item

    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.connection.close()


class PostgresNoDuplicatesPipeline:

    def __init__(self):
        ## Connection Details
        hostname = os.getenv('hostname')
        username = os.getenv('username')
        password = os.getenv('password')
        database = os.getenv('database')

        ## Create/Connect to database
        self.connection = psycopg2.connect(host=hostname, user=username, password=password, dbname=database)
        
        ## Create cursor, used to execute commands
        self.cur = self.connection.cursor()
        
        ## Create quotes table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS jobs(
            id serial PRIMARY KEY, 
            company varchar (150) NOT NULL,
            title varchar (150) NOT NULL,
            link text NOT NULL,
            date text NOT NULL
        )
        """)

    def process_item(self, item, spider):

        ## Check to see if text is already in database 
        self.cur.execute("select * from jobs where link = %s", (item['link'],))
        result = self.cur.fetchone()

        ## If it is in DB, create log message
        if result:
            spider.logger.warn("Item already in database: %s" % item['link'])


        ## If text isn't in the DB, insert data
        else:

            ## Define insert statement
            self.cur.execute(""" insert into jobs (company, title, link, date) values (%s,%s,%s,%s)""", (
                item['company'],
                item['title'],
                item['link'],
                item['date']
        ))

            ## Execute insert of data into database
            self.connection.commit()
        return item

    
    def close_spider(self, spider):

        ## Close cursor & connection to database 
        self.cur.close()
        self.connection.close()
