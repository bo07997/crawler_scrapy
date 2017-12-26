# Scrapy settings for dirbot project

SPIDER_MODULES = ['dirbotTest.spiders']
NEWSPIDER_MODULE = 'dirbotTest.spiders'
DEFAULT_ITEM_CLASS = 'dirbotTest.items.Website'

ITEM_PIPELINES = {'dirbotTest.pipelines.FilterWordsPipeline': 1}
