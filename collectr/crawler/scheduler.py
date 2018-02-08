import scrapy
from rq import Queue
from worker import conn
from scrapy.crawler import CrawlerProcess
from crawler.spiders.sm import SparkModelSpider


q = Queue(connection=conn)

process = CrawlerProcess()
process.crawl(SparkModelSpider)


if __name__ == '__main__':
    result = q.enqueue(process.start)
