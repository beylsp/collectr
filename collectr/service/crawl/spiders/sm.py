import scrapy

from scrapy.loader import ItemLoader
from six.moves.urllib import parse

from collectr.service.crawl.items import SparkModelItem


class SparkModelSpider(scrapy.Spider):
    name = 'sm'
    base_url = 'http://www.sparkmodel.com/search/index/list'
    allowed_domains = ['sparkmodel.com']

    def start_requests(self):
        yield scrapy.http.FormRequest(self.base_url,
                                      formdata=self.get_form_data('1'),
                                      callback=self.parse)

    def parse(self, response):
        self.logger.info('parse function called on %s', response.url)

        items = response.xpath('//li[@class="item"]'
                               '/div[@class="regular"]'
                               '/a[@class="product-image"]/img')
        for item in items:
            try:
                il = ItemLoader(SparkModelItem(), item)
                il.add_xpath('product_id', '@src')
                il.add_xpath('image_url', '@src')
                il.add_xpath('title', '@alt')
                yield il.load_item()
            except ValueError:
                pass

        np = response.xpath('//a[@class="next i-next"]')
        if np:
            yield self.request_next_page(np)

    def request_next_page(self, np):
        np_link = np.xpath('@href').extract_first()
        url = parse.urlparse(np_link)
        q = parse.parse_qs(url.query)
        page = q.get('p')[0]
        self.logger.info('yield next page: %s' % page)
        return scrapy.http.FormRequest(self.base_url,
                                       formdata=self.get_form_data(page),
                                       callback=self.parse)

    def get_form_data(self, page):
        return {
            'category': '51',
            'limit': '60',
            'order': 'position',
            'p': page}
