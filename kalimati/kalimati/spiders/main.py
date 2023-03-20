import scrapy


class KalimatiScraper(scrapy.Spider):
    name = "kalimati"
    start_urls = ['https://kalimatimarket.gov.np/price']

    

    

    def parse(self, response):
        

        for items in response.css('tbody tr'):

            itemsName = items.css('td::text')[0].get()
            itemsMin = items.css('td::text')[2].get()
            itemsMax = items.css('td::text')[3].get()
            itemsAvg = items.css('td::text')[4].get()

            yield{
                'name' : itemsName,
                'min price' : itemsMin,
                'max price' : itemsMax,
                'avg price' : itemsAvg,
            }

            