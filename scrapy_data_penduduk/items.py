# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DataPendudukItem(scrapy.Item):
    provinsi = scrapy.Field()
    tahun_2020 = scrapy.Field()
    tahun_2021 = scrapy.Field()
    tahun_2022 = scrapy.Field()
