'''
Crawl webpage and get metadata for Citizen Science European Projects

scrapy runspider spiders/WebSpider.py 
'''

import scrapy
import json
from scrapingcc.items import *

class WebSpider(scrapy.Spider):
    name = 'webspider'
    start_urls = ['https://pruebas.ibercivis.es/']

    def parse(self, response):
        
        '''
        for title in response.css('.entry-title'):
            yield {'title': title.css('a ::text').get()}
        '''
				
        
        #microdata_content = response.xpath('//script[@type="application/ld+json"]/@context').extract_first()		
        microdata_content = response.xpath('//script[@type="application/ld+json"]//text()').extract_first()
        #print(microdata_content)
        #print(response.xpath("/html").extract())
				
        
        microdata = json.loads('[' + microdata_content+']')
        
        for m in microdata:
           type = m['@type']
           if(type == 'ProjectCC'):
              item = ProjectItem()
              item['name'] = (m['name'])
              item['url'] = (m['url'])
              item['start_date'] = (m['start-date'])
              item['end_date'] = (m['end-date'])
              item['contact_email'] = (m['contact-email'])
              yield item
           else:
                document = DocumentItem()
                document['url'] = m['url']
                document['name'] = m['name']
                document['author'] = m['author']
                document['datePublished'] = m['datePublished']
                document['description'] = m['description']
                yield document
    		
        
        for next_page in response.css('.entry-title > a'):
            yield response.follow(next_page, self.parse)

			