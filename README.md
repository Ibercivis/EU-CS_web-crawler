# EU-CS_web-crawler
Web crawler for Citizen Science resources

## Description
This crawler crawls web pages, searching Citizen Science metadata for create/update EU-Citizen.Science projects and documents collection.
If the application find an existing resource, then it updates it. If not, it creates it.

## How to execute
First of all, you need to install Python and Scrapy in your computer.
Then, in a terminal, launch this command: 
```
scrapy runspider scrapingcc/spiders/WebSpider.py 
```
