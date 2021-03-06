from scrapy import Spider
from scrapy.selector import Selector
from stack.items import StackItem


class StackSpider(Spider):
    name = "stack_spider"
    allowed_domains = ["stackoverflow.com"]
    start_urls = [
        'https://stackoverflow.com/questions'
    ]

    def parse(self, response):
        questions = Selector(response).xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = StackItem()
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            yield item