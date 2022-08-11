import scrapy
from scrapy import Selector

from constants import PATTERN
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        peps_table: Selector = response.css(
            "section[id='numerical-index']"
        ).css("tbody")[0]
        links: list[str] = peps_table.css("a::attr(href)").getall()
        for link in links:
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        pep_info: Selector = response.css("section[id='pep-content']")
        title = PATTERN.search(pep_info.css("h1::text").get())
        status: str = pep_info.css("dt:contains('Status') + dd::text").get()
        if title:
            number, name = title.group("number", "name")
            context = {
                "number": number,
                "name": name,
                "status": status
            }
            yield PepParseItem(context)
