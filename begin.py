from scrapy import cmdline

cmdline.execute("scrapy crawl dmoz  -o dmoz.json".split())