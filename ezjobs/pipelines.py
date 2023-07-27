from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem
import json

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
