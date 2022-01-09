# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# # useful for handling different item types with a single interface
# from itemadapter import ItemAdapter


# class StackPipeline:
    # def process_item(self, item, spider):
        # return item
import pymongo

from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem
import logging

settings = get_project_settings()

class MongoDBPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            settings.get('MONGODB_SERVER'),
            settings.get('MONGODB_PORT')
        )
        db = connection[settings.get('MONGODB_DB')]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            logging.debug("Question added to MongoDB database!")
        return item