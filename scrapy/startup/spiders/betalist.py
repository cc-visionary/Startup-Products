import scrapy
import os
import json
import xlsxwriter
import pandas as pd
import numpy as np
df = pd.read_excel(os.getcwd() + '\\betalistpage.xlsx')
print(len(df), df['Betalist URL'].nunique()) # proves whether or not every item scraped is unique (it is)
print(np.sum(df['Featured Date'].apply(lambda x: 0 if x != x else 1))) # gets all the sum of the 
print(df)
products = []
for data in df.iloc:
    products.append({
        'product': None if data['Product Name'] !=  data['Product Name'] else data['Product Name'],
        'description': None if data['Description'] != data['Description'] else data['Description'],
        'featured_date': None if data['Featured Date'] != data['Featured Date'] else data['Featured Date'],
        'href': None if data['Betalist URL'] != data['Betalist URL'] else data['Betalist URL'],
        'tags': None if data['Tag'] != data['Tag'] else data['Tag'],
        'votes': None if data['Votes'] != data['Votes'] else data['Votes']
    })

# Get data from JSON file
# with open(os.getcwd() + '\\startup\\startup\\betalistlisting.json', 'r') as f:
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

# tags and date from JSON file
# tagsDate = []
# with open(os.getcwd() + '\\startup\\betalistpage.json', 'r') as f:
#     datas = json.load(f)
#     for data in datas:
#         tagsDate.append({
#             'path': data['path'],
#             'featured_date': data['featured_date'],
#             'tag': data['tags'],
#         })

# print(len(tagsDate))
# for tagDate in tagsDate:
#     for product in products:
#         if(tagDate['path'].split('/')[-1] == product['href'].split('/')[-1]):
#             product['tags'] = tagDate['tag']
#             product['featured_date'] = tagDate['featured_date']
#             break

# url from json from JSON file
# listingsurl = []
# with open(os.getcwd() + '\\betalisturl.json', 'r') as f:
#     datas = json.load(f)
#     for data in datas:
#         listingsurl.append({
#             'path': data['path'],
#             'url': data['url'].split('?')[0],
#         })
# print(len(listingsurl))

# for listing in listingsurl:
#     for product in products:
#         if(listing['path'].split('/')[-1] == product['href'].split('/')[-1]):
#             product['url'] = listing['url']
#             break 
# df = pd.DataFrame()
# print(df)

workbook = xlsxwriter.Workbook('betalistfinal.xlsx')
worksheet = workbook.add_worksheet()
worksheet.set_column('A:E', 25)
worksheet.write(0, 0, 'Product Name')
worksheet.write(0, 1, 'Description')
worksheet.write(0, 2, 'Featured Date')
worksheet.write(0, 3, 'Betalist URL')
worksheet.write(0, 4, 'Tag')
worksheet.write(0, 5, 'Votes')

row = 1
for product in products:
    worksheet.write(row, 0, 'nan' if product['product'] != product['product'] else product['product'])
    worksheet.write(row, 1, 'nan' if product['description'] != product['description'] else product['description'])
    worksheet.write(row, 2, 'nan' if product['featured_date'] != product['featured_date'] else product['featured_date'])
    worksheet.write(row, 3, 'nan' if product['href'] != product['href'] else product['href'])
    worksheet.write(row, 4, 'nan' if product['tags'] != product['tags'] else product['tags'])
    worksheet.write(row, 5, 0 if product['votes'] == None else int(product['votes']))
    row += 1
    
workbook.close()
# for data in datas:
#     print(data)

# Scrape listings
# class BetalistSpider(scrapy.Spider):
#     name = "listing"
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

# Scrape pages 
# class BetalistSpider(scrapy.Spider):
#     name = "product-page"
#     urls = list(df['Betalist URL'])
#     download_delay = 1.5
#     months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

#     def start_requests(self): 
#         for url in self.urls:
#             yield scrapy.Request(url, self.parse)

#     def parse(self, response):
#         yield {
#             'path': response.request.url,
#             'tags': ','.join(response.css('a.tag::text').getall()),
#             'featured_date': response.css('time::attr(datetime)').getall()[-1].split('T')[0]
#         }
        
# class BetalistSpider(scrapy.Spider):
#     name = "product-url"
#     url = None
#     urls = list(df['Betalist URL'])
#     download_delay = 1.5

#     def start_requests(self):
#         for u in self.urls:
#             self.url = u
#             yield scrapy.Request(u + '/visit', self.parse)

#     def parse(self, response):
#         yield {
#           'path': self.url,
#           'url': response.request.url
#         }