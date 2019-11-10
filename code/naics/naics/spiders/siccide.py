# -*- coding: utf-8 -*-
import scrapy


class SiccideSpider(scrapy.Spider):
    name = 'siccide'
    allowed_domains = ['https://siccode.com/']
    start_urls = ['http://https://siccode.com//']

    def start_requests(self):
        urls = [
            "https://siccode.com/business/google-inc",
            "https://siccode.com/business/apple-inc",
            "https://siccode.com/business/apple-store-1",
            "https://siccode.com/business/microsoft-corp",
            "https://siccode.com/business/microsoft-store-1",
            "https://siccode.com/business/fitbit-inc",
            "https://siccode.com/business/youtube-llc",
            "https://siccode.com/business/facebook-inc"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        row = response.xpath('//*[@id="description"]/div[2]/div/div/a[2]/span')
        code = row.css("::text").get().split(" CODE ")[1]

        row = response.xpath('//*[@id="main"]/div/div/h1/a/span')
        name = row.css("::text").get()
        table = {'name': name, 'code': code}
        yield{
            **table
        }
