import logging

from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
from crawl.spiders.sm import SparkModelSpider


logger = logging.getLogger(__name__)


def crawl():
    settings = Settings()
    settings.setmodule('crawl.settings')
    proc = CrawlerProcess(settings)
    try:
        proc.crawl(SparkModelSpider)
        proc.start()
    except KeyError as err:
        logger.warning(err.args[0])
