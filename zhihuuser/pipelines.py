import pymongo


class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db, mongo_username, mongo_pwd):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.mongo_username = mongo_username
        self.mongo_pwd = mongo_pwd

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_username=crawler.settings.get('MONGO_USERNAME'),
            mongo_pwd=crawler.settings.get('MONGO_PWD'),
            mongo_db=crawler.settings.get('MONGO_DATABASE'),
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.client[self.mongo_db].authenticate(self.mongo_username, self.mongo_pwd, self.mongo_db,
                                                mechanism='SCRAM-SHA-1')
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db['user'].update({'url_token': item['url_token']}, {'$set': item}, True)
        return item
