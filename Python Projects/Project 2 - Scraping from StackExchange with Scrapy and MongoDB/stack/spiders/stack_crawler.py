import scrapy
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from stack.items import StackItem


class StackCrawlerSpider(CrawlSpider):
    name = 'stack_crawler'
    allowed_domains = ['stackoverflow.com']
    start_urls = ['https://stackoverflow.com/questions']

    rules = [
    Rule(LinkExtractor(allow=r'questions\?tab=newest&page=\b[0-9]\b'),
         callback='parse_item', follow=True)
    ]

    def parse_item(self, response):
        questions = response.xpath('//div[@class="summary"]/h3')

        for question in questions:
            item = StackItem()
            item['url'] = question.xpath(
                'a[@class="question-hyperlink"]/@href').extract()[0]
            item['title'] = question.xpath(
                'a[@class="question-hyperlink"]/text()').extract()[0]
            yield item