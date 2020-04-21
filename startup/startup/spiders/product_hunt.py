import scrapy
import pandas as pd

# df = pd.read_excel('../product_hunt1.xlsx')
# total = len(df.index)
# left = df[df['URL'] != df['URL']]
# start_left = total - len(left)
# print(left['ProductHunt URL'])
# print(start_left)

# class ProductHuntSpider(scrapy.Spider):
#     name = "product_hunt"

#     def start_requests(self):
#         url = 'http://producthunt.com/'
#         # tag = getattr(self, 'tag', None)
#         # if tag is not None:
#         #     url = url + 'tag/' + tag
#         yield scrapy.Request(url, self.parse)

#     def parse(self, response):
#         pass

        # next_page = response.css('li.next a::attr(href)').get()
        # if(next_page is not None):
        #     yield response.follow(next_page, self.parse)