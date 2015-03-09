import re
import json

from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor as sle
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.http import Request
from babaSR.items import BabaSRItem
from babaSR.util import *

class DemohourSpider(CrawlSpider):
    name = "babaSR"
    allowed_domains = ["demohour.com"]
    start_urls = [
        "http://www.demohour.com/projects/latest",
        "http://www.demohour.com/projects/sell",
        "http://www.demohour.com/projects/presell"
    ]
    rules = [
        Rule(sle(allow=("/subject/\d+/?$")), callback='parse_2'),
        Rule(sle(allow=("/tag/[^/]+/?$", )), follow=True),
        Rule(sle(allow=("/tag/$", )), follow=True),
    ]
    
    def parseContent(self,product):
        #print chardet.detect(content)
        name=product.xpath('div[@class="main-column"]/div[@class="rdiv post-container"]/h3[@class="title1"]/text()').extract()[0].encode('utf-8')
        piclink=product.xpath('div[@class="main-column"]/div[@class="rdiv post-container"]/div[@class="img1"]/img/@src').extract()[0]
        if 'http' not in piclink:
            piclink ='http://www.leikeji.com/' + ''.join(piclink)
        picture = piclink.encode('utf-8')
        content = product.xpath('div[@class="main-column"]/div[@class="rdiv post-container"]/div[@class="des"]').extract()[0].encode('utf-8')
        content = filter_tags(content)
        #print 'name:',name, 'picture:',picture,'content:',content
        price = 0.0
        paylink = None
        setting = None
        tag = None
        return (name,picture,content,price,paylink,setting,tag)


    def parse_item(self,response):
        hxs =Selector(response)
        items = []
        item = response.meta['item']
        products = hxs.xpath('//div[@class="main-container"]')
        for product in products:
            # parseContent detail method
            parseTuple = self.parseContent(product)
            item['name'] = parseTuple[0]
            item['picture'] =parseTuple[1]
            item['content'] = parseTuple[2]
            item['price'] = parseTuple[3]
            item['paylink'] = parseTuple[4]
            item['setting'] = parseTuple[5]
            item['tag'] = parseTuple[6]
            #item['desc'] = parseTuple[7]
            #print 'finalItem:',item
            items.append(item)
        return items
    
    # main parse method in Spider
    def parse(self, response):
        hxs = Selector(response)   
        newurls = hxs.xpath('//a/@href').extract()
        validurls = []
        items = [] 
        for url in newurls:   
            if 'http' not in url:
                url = 'http://www.leikeji.com/' + url
            if 'product_item' in url:
                validurls.append(url) 
            if 'product?firstResult' in url:
                yield Request(url,callback=self.parse)
                
        items.extend([self.make_requests_from_url(url).replace(callback=self.parse) for url in validurls])  
        print 'items:',items

        sites = hxs.xpath('//ul[@class="productList"]/li')
        items = []
        for site in sites:
            item = BabaSRItem()
            title= site.xpath('div[@class="product rdiv"]/div[@class="pname"]/text()').extract()[0].encode('utf-8')
            item['title'] = title
            link = site.xpath('div[@class="product rdiv"]/div/a/@href').extract()
            if 'http' not in link:
                link ='http://www.leikeji.com/' + link[0]
            item['link'] = link.encode('utf-8')
            items.append(item)
            print 'itemInfo:',item
            yield Request(item['link'],meta={'item':item},callback=self.parse_item)

        #return items  
