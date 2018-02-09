import logging
import scrapy

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from crawler.spiders.sm import SparkModelSpider


logger = logging.getLogger(__name__)


def crawl():
    settings = Settings()
    settings.setmodule('crawler.settings')
    proc = CrawlerProcess(settings)
    try:
        proc.crawl(SparkModelSpider)
        proc.start()
    except KeyError as err:
        logger.warning(err.args[0])

