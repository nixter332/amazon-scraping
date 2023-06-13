import scrapy

class SpideySpider(scrapy.Spider):
    name = "spidey"
    page_number=2
    start_urls = [
        "https://www.amazon.in/s?bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&rnid=2684818031&ref=lp_976390031_nr_p_n_publication_date_0"
    ]

    def parse(self, response):
        
        product_name=response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author=response.css('.a-color-secondary .a-size-base+ .a-size-base').css('::text').extract()
        product_price=response.css('.a-price-whole , .widgetId\=search-results_1 .s-no-hover').css('::text').extract()
        product_type=response.css('.s-link-style.a-text-bold').css('::text').extract()
        
        yield{
            'Name':product_name,
            'Author':product_author,
            'Price':product_price,
            'Type':product_type
        }
        
        next_page='https://www.amazon.in/s?i=stripbooks&bbn=976389031&rh=n%3A976389031%2Cp_n_publication_date%3A2684819031&dc&page=' + str(SpideySpider.page_number) + '&rnid=2684818031&ref=sr_pg_' + str(SpideySpider.page_number)
        if SpideySpider.page_number <= 11:
            SpideySpider.page_number+=1
            yield response.follow(next_page,callback = self.parse)
            