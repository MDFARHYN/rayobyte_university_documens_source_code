#read the docs for more info https://github.com/scrapy-plugins/scrapy-playwright
import scrapy

class BasicScriptingPlaywrightSpider(scrapy.Spider):
    name = "basic_scripting_playwright"
    allowed_domains = ["quotes.toscrape.com"]
     
    def start_requests(self):
        # GET request
        yield scrapy.Request("https://quotes.toscrape.com", meta={"playwright": True})
         
    def parse(self, response):
        # Print the HTML of the page
        print(response.text)
