# -*- coding: utf-8 -*-

# Scrapy settings for babaSR project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'babaSR'

SPIDER_MODULES = ['babaSR.spiders']
NEWSPIDER_MODULE = 'babaSR.spiders'

ITEM_PIPELINES = ['babaSR.dbpipelines.MongoDBPipeline']

MONGODB_SERVER = "192.168.1.101"
MONGODB_PORT = 15000
MONGODB_USERNAME = "root"
MONGODB_PASSWORD = "lenote2013"
MONGODB_DB = "babasr"
MONGODB_COLLECTION = "article"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'babaSR (+http://www.yourdomain.com)'
