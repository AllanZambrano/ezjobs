from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

class CleanNull(object):
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        # check if value is null
        if adapter.get('company'):
            return item
        else:
            # drop item is null
            raise DropItem("Item is NULL")