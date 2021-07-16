import json
from datetime import date, datetime
from scrapy.exporters import JsonItemExporter
from itemadapter import ItemAdapter

d = date.today()

class JsonPipeline(object):

    file = None

    def open_spider(self, spider):
        self.file = open(f'{d}.json', 'wb')
        self.exporter = JsonItemExporter(self.file, indent=1)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class JsonWriterPipeline:

    def open_spider(self, spider):
        self.file = open(f'{d}.json', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item