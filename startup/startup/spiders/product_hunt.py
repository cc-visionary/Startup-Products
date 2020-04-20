import scrapy

class ProductHuntSpider(scrapy.Spider):
    name = "product_hunt"

    def start_requests(self):
        url = 'http://producthunt.com/'
        # tag = getattr(self, 'tag', None)
        # if tag is not None:
        #     url = url + 'tag/' + tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        pass

        # next_page = response.css('li.next a::attr(href)').get()
        # if(next_page is not None):
        #     yield response.follow(next_page, self.parse)