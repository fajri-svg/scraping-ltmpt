import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'https://top-1000-sekolah.ltmpt.ac.id/?page=1&per-page=100',
            'https://top-1000-sekolah.ltmpt.ac.id/?page=2&per-page=100',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # print(response.url)
        
        for i in range(1, 101):
            
            for sekolah in response.css('#w0 > table > tbody'):
                yield{
                    'ranking':sekolah.css('tr:nth-child(' + str(i) + ') > td:nth-child(1)::text').extract(),
                    'npsn':sekolah.css('tr:nth-child(' + str(i) + ') > td:nth-child(3)::text').extract(),
                    'nama_sekolah':sekolah.css('tr:nth-child(' + str(i) + ') > td:nth-child(4)::text').extract(),
                    'nilai_total':sekolah.css('tr:nth-child(' + str(i) + ') > td:nth-child(5)::text').extract(),
                    'provinsi':sekolah.css('tr:nth-child(' + str(i) + ') > td:nth-child(6)::text').extract(),
                    'kab_kota':sekolah.css('tr:nth-child(' + str(i) + ') > td:nth-child(7)::text').extract(),
                    'jenis':sekolah.css('tr:nth-child(' + str(i) + ') > td:nth-child(8)::text').extract(),
                }

#w0 > table > tbody > tr:nth-child(1) > td:nth-child(4)
#w0 > table > tbody > tr:nth-child(2) > td:nth-child(4)
#w0 > table > tbody > tr:nth-child(3) > td:nth-child(4)