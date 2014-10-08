from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from babaSR.items import BabasrItem

class Baba2Spider(CrawlSpider):

    def parse(self, response):
        hxs = HtmlXPathSelector(response)  
        items = []  
      
        newurls = hxs.select('//a/@href').extract()  
        validurls = []  
        for url in newurls:  
            if True:  
                validurls.append(url)  
            
            items.extend([self.make_requests_from_url(url).replace(callback=self.parse) for url in validurls])  
            sites = hxs.select('//ul/li')  
            items = []  
            for site in sites:  
                item = BabasrItem()  
                item['title'] = site.select('a/text()').extract()  
                item['link'] = site.select('a/@href').extract()  
                item['desc'] = site.select('text()').extract()  
                items.append(item)  
            return items  
