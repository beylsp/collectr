import scrapy
from scrapy.crawler import CrawlerProcess
from crawler.spiders.sm import SparkModelSpider

process = CrawlerProcess()

if __name__ == '__main__':
    process.crawl(SparkModelSpider)
    process.start()
