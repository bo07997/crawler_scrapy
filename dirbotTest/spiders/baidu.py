from scrapy.spiders import Spider
import scrapy

from dirbot.dirbotTest.items import Website


class DmozSpider(Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    #search_word = input("Enter your search_word: ")
    start_urls = [
        "https://www.baidu.com/",

    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        self.log('A response from %s just arrived!' % response.url)
        sites = response.css('body > div.content > div > div > b > b > div')
        items = []
        #str = input("Enter your input: ")
        for site in sites:
            item = Website()
            item['pitures_str'] = site.css(
                ' a/@href').extract()
            # item['url'] = site.xpath(
            #     'a/@href').extract_first().strip()
            # item['description'] = site.css(
            #     'div.site-descr::text').extract_first().strip()
            items.append(item)
            print(items)
        return items
