#!/usr/bin/env python
import logging
import os
import pandas as pd 
import re
import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from googlesearch import search

logging.getLogger('scrapy').propagate = False

def get_urls(tag, n, language):
    urls = [url for url in search(tag, stop=n, lang=language)][:n]
    return urls

mine = get_urls('https://www.assentcompliance.com/', 5 , 'en')
print (mine)