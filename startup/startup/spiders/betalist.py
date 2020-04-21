import scrapy
import json
# import pandas as pd
# df = pd.read_excel('../betalist.xlsx')
# total = len(df.index)
# left = df[df['URL'] != df['URL']]
# start_left = total - len(left)
# print(left['Betalist URL'])
# print(start_left)

datas = json.loads('../betalist.json')
# for data in datas:
#     print(data)

# class BetalistSpider(scrapy.Spider):
#     name = "betalist"
#     url_name = 'http://betalist.com/?page=%s'
#     download_delay = 1.5
#     urls = []
#     for i in range(101, 1152):
#         urls.append(url_name % i)

#     def start_requests(self):
#         for url in self.urls:
#             yield scrapy.Request(url, self.parse)

#     def parse(self, response):
#         cards = response.css('div.startupCard')
#         for card in cards:
#             yield {
#                 'name': card.css('a.startupCard__details__name::text').get(), # startupCard__details__name
#                 'pitch': card.css('a.startupCard__details__pitch::text').get(), # startupCard__details__pitch
#                 'upvote': card.css('div.cuteButton__score::text').get(), # cuteButton__score
#                 'path': card.css('a.startupCard__details__name::attr(href)').get(), # startupCard__details__name .href
#             }

        
        # tags = response.css('a.tag::text').getall()
        # response.css('a.button2--contrast::attr(href)').get()
        # response.request.url