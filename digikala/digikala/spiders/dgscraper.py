from typing import KeysView
import scrapy
import re
import json


class QuotesSpider(scrapy.Spider):
    name = "digikala"

    def start_requests(self):
        urls = [
            # 'https://www.digikala.com/product/dkp-476001',
            'https://www.digikala.com/product/dkp-20401'
            # 'https://www.digikala.com/product/dkp-551270'
            # 'https://www.digikala.com/product/dkp-2360300'
            # 'https://www.digikala.com/product/dkp-6103504'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        search = re.findall("var variants =(.+?);\n", response.body.decode('utf-8'))
        seller_list = search[0]
        # print(len(seller_list))
        seller_dict = json.loads(seller_list)
        return seller_dict
