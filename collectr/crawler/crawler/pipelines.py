# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from database.models import SparkModelData
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker

import settings


class PgPipeline(object):

    @classmethod
    def from_crawler(cls, _):
        return cls()

    def open_spider(self, spider):
        engine = create_engine(URL(**settings.DATABASE))
        self.db = scoped_session(sessionmaker(autocommit=False,
                                              autoflush=False,
                                              bind=engine))

    def process_item(self, item, spider):
        product_id = item['product_id'][0]
        image_url = item['image_url'][0]
        title = item['title'][0]

        it = self.get_it(product_id)
        if not it:
            record = SparkModelData(
                product_id=product_id,
                image_url=image_url,
                title=title,
                in_collection=False)
            self.db.add(record)
        else:
            it.image_url = image_url
            it.title = title
        self.db.commit()
        return item

    def get_it(self, product_id):
        return self.db.query(SparkModelData).filter(
                SparkModelData.product_id == product_id).first()
