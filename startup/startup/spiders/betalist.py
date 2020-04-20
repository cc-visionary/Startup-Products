import scrapy
import json

class BetalistSpider(scrapy.Spider):
    name = "betalist"
    url_name = 'http://betalist.com/?page%s'
    urls = []
    for i in range(100, 1000):
        urls.append(url_name % i)
    download_delay = 1.5

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        cards = response.css('div.startupCard')
        for card in cards:
            yield {
                'name': card.css('a.startupCard__details__name::text').get(), # startupCard__details__name
                'pitch': card.css('a.startupCard__details__pitch::text').get(), # startupCard__details__pitch
                'upvote': card.css('div.cuteButton__score::text').get(), # cuteButton__score
                'path': card.css('a.startupCard__details__name::attr(href)').get(), # startupCard__details__name .href
            }