# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import os
import scrapy

from scrapy.loader.processors import MapCompose


def filter_id(value):
    f = os.path.basename(value)
    n, ext = os.path.splitext(f)
    v = n.split('-')[1]
    if v[:2] in ('12', '18', 'SA') or \
       v[0] in ('M', 'Y') or \
       v.startswith('43MF') or \
       v in ('S0771', 'S0776', 'SF037'):
        raise ValueError
    return v


def filter_venue(value):
    if 'GP' not in value or \
       'F3' in value:
        raise ValueError
    return value


class SparkModelItem(scrapy.Item):
    product_id = scrapy.Field(
        input_processor=MapCompose(filter_id))
    image_url = scrapy.Field()
    title = scrapy.Field(
        input_processor=MapCompose(filter_venue))
