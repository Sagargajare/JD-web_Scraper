import scrapy
from ..items import JustdialItem
import re


def contact(str):
    num = []
    dict = {'dc': '+', 'fe': '(', 'ji': '9', 'yz': '1', 'hg': ')', 'ba': '-', 'rq': '5', 'wx': '2', 'acb': '0',
           'nm': '7', 'lk': '8', 'vu': '3', 'ts': '4', 'po': '6'}

    rw_ps = re.findall(r"-([a-z]+)", str)

    for i in rw_ps:
        try:
            # print(dic[i])
            num.append(dict[i])
        except:
            pass
    a = "".join(num)
    return a

class QuatesSpider(scrapy.Spider):
    name = 'JD'
    start_urls =[
        'https://www.justdial.com/Delhi/House-On-Rent/nct-10192844'
    ]
    def parse(self,response):
        item = JustdialItem()
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        # title = response.css('title::text').extract()
        name = response.css('span.lng_cont_name::text').extract()
        rate = response.css('span.green-box::text').extract()
        add = response.css('span.cont_fl_addr::text').extract()
        r_contact = response.css('p.contact-info ').extract()
        contacts = []
        for i in r_contact:
            cont = contact(i)
            contacts.append(cont)


        for i in range(len(name)):
            item['name'] = name[i]
            item["rating"] = rate[i]
            item["contact"] = contacts[i]
            item["address"] = add[i]

            yield item