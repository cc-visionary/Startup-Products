import scrapy
import os
import json
import xlsxwriter
import pandas as pd
df = pd.read_excel(os.getcwd() + '\\betalist_final.xlsx')
print(len(df), df['Betalist URL'].nunique()) # proves whether or not every item scraped is unique (it is)
# products = []
# for data in df.iloc:
#     products.append({
#         'product': data['Product Name'],
#         'description': data['Description'],
#         'url': data['URL'],
#         'href': data['Betalist URL'],
#         'tag': data['Tag'],
#         'votes': data['Votes']
#     })

# with open(os.getcwd() + '\\startup\\startup\\betalist.json', 'r') as f:
#     datas = json.load(f)
#     for data in datas:
#         products.append({
#             'product': data['name'],
#             'description': data['pitch'],
#             'url': None,
#             'href': 'https://www.betalist.com' + data['path'],
#             'tag': [],
#             'votes': data['upvote']
#         })

# workbook = xlsxwriter.Workbook('betalist_final.xlsx')
# worksheet = workbook.add_worksheet()
# worksheet.set_column('A:D', 25)
# worksheet.set_column('E:E', 70)
# worksheet.write(0, 0, 'Product Name')
# worksheet.write(0, 1, 'Description')
# worksheet.write(0, 2, 'URL')
# worksheet.write(0, 3, 'Betalist URL')
# worksheet.write(0, 4, 'Tag')
# worksheet.write(0, 5, 'Votes')

# row = 1
# for product in products:
#     worksheet.write(row, 0, product['product'])
#     worksheet.write(row, 1, product['description'])
#     worksheet.write(row, 2, None)
#     worksheet.write(row, 3, product['href'])
#     worksheet.write(row, 4, None)
#     if(product['votes'] == None):
#         worksheet.write(row, 5, 0)
#     else:
#         worksheet.write(row, 5, int(product['votes']))
#     row += 1
    
# workbook.close()
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