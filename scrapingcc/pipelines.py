# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem
from scrapingcc.items import *
from scrapingcc.manageDB import *


'''
Drop incomplete items. Check all mandatory fields.
'''
class DropEmptyItemPipeline(object):

  def process_item(self, item, spider):
    if isinstance(item, ProjectItem):
      if item['name'] == '' or item['url'] == '' or item['start_date'] == '' or item['end_date'] == ''\
        or item['contact_email'] == '':
        raise DropItem("Incorrect item found: %s" % item)
    else: #item instanceOf DocumentItem
      if item['name'] == '' or item['url'] == '' or item['author'] == '' or item['description'] == '' \
          or item['datePublished'] == '':
        raise DropItem("Incorrect item found: %s" % item)
      
    return item

'''
Update DB with Projects & Documents from Citizen Science webpages.
'''
class ScrapingccPipeline(object):
    def process_item(self, item, spider):
      print(item)

      cnx = connectDB()
      if(cnx):
          #print('Connected')
          if isinstance(item, ProjectItem):
            itemExists = existProjectItem(cnx, item['url'])			          
            print('Exist: ', itemExists)
            if(not itemExists):
                userID = getUserID(cnx,item['contact_email'])
                if(userID != 0):                  
                  insertProjectItem(cnx, item, userID)
                else:                  
                  print('User with email', item['contact_email'], ' not exists')
            else:
                updateProjectItem(cnx, item)
                
          else: #item instanceOf DocumentItem
            print('********************************* DocumentItem: ', item['name'], '*********************************')   
            itemExists = existDocumentItem(cnx, item['url'])			
            print('Exist: ', itemExists)
            if(not itemExists):
                insertDocumentItem(cnx, item)                
            else:
                updateDocumentItem(cnx, item)                
      closeDB(cnx) 
