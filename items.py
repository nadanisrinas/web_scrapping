import scrapy


class QuoteItem(scrapy.Item):
    author = scrapy.Field()
    quote = scrapy.Field()