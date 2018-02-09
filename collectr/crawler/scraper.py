import logging
import scrapy

from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from crawler.spiders.sm import SparkModelSpider


logger = logging.getLogger(__name__)


def crawl():
    settings = get_project_settings()
    proc = CrawlerProcess(settings)
    try:
        proc.crawl(SparkModelSpider)
        proc.start()
    except KeyError as err:
        logger.warning(err.args[0])

