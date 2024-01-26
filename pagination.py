import scrapy
from scrapy.crawler import CrawlerProcess
from scrapping.items import QuoteItem


class QuotesSpiderSpider(scrapy.Spider):
    name = "quotes_spider"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["http://quotes.toscrape.com/"]

    def parse(self, response):
        quotes = response.xpath("//div[@class='quote']")
        for quote in quotes:
            text = quote.xpath(".//span[@class='text']/text()").get()
            author = quote.xpath(".//small//text()").get()

            item = QuoteItem()
            item["quote"] = text
            item["author"] = author

            yield item

        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url:
            yield scrapy.Request(
                url=response.urljoin(next_page_url), callback=self.parse
            )
