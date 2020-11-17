import scrapy
import urllib.parse as urlparse

class QuotesParseFollowSpider(scrapy.Spider):

    name = "quotes_parse_follow"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]


    def parse(self, response):

        root = urlparse.urlparse(response.url)
        root = f"{root.scheme}://{root.netloc}"

        for quote in response.css('div.quote'):

            links = quote.css('div.tags a').xpath("@href").getall()
            links = [root + s for s in links]

            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
                'links': links,
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)