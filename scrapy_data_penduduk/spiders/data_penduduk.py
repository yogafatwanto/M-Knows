import scrapy
from ..items import DataPendudukItem

class DataPenduduk(scrapy.Spider):
    name = 'data_penduduk'  # Ganti dengan nama spider Anda
    start_urls = ['https://sulut.bps.go.id/indicator/12/958/1/jumlah-penduduk-menurut-provinsi-di-indonesia.html']  # Ganti dengan URL yang akan Anda scraping

    def parse(self, response):
        rows = response.xpath('//tbody/tr')  # Asumsi data berada dalam tag tbody

        for row in rows:
            province = row.xpath('.//td[@class="vervar"]/text()').get()
            year_2020 = row.xpath('.//td[@class="text-right"][1]/text()').get()
            year_2021 = row.xpath('.//td[@class="text-right"][2]/text()').get()
            year_2022 = row.xpath('.//td[@class="text-right"][3]/text()').get()

            yield {
                'provinsi': province,
                '2020': year_2020,
                '2021': year_2021,
                '2022': year_2022
            }
