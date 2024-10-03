import scrapy
from scrapy_selenium import SeleniumRequest


class BasicScriptingSeleniumSpider(scrapy.Spider):
    name = "basic_scripting_selenium"
    allowed_domains = ["quotes.toscrape.com"]
    def start_requests(self):
        url = 'https://quotes.toscrape.com'
        yield SeleniumRequest(url=url, callback=self.parse)

    def parse(self, response):
          print(response.text)
