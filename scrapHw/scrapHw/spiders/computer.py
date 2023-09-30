import scrapy


class ComputerSpider(scrapy.Spider):
    name = "computer"

    def start_requests(self):
        url = 'https://www.goldonecomputer.com/'
        yield scrapy.Request(url = url , callback=self.parse)

    def parse(self, response):
        links = response.xpath("//*[@class='box-content']/ul[@id='nav-one']/li/a/@href").getall()
        for link in links:
            absolute_link = response.urljoin(link)
            yield response.follow(absolute_link, callback=self.navigateLink)

    def navigateLink(self, response):
        productLinks = response.xpath("//*[@class='caption']/h4/a/@href").getall()
        for productLink in productLinks:
            absolute_link_product = response.urljoin(productLink)
            yield response.follow(absolute_link_product, callback=self.parse_linked_page)

    def parse_linked_page(self, response):
        code = response.xpath("//ul[@class='list-unstyled']/li/text()").get()
        title = response.xpath("//*/h3[@class='product-title']/text()").get()
        brand = response.xpath("//ul[@class='list-unstyled']/li/a/text()").get()
        price = response.xpath("//ul[@class='list-unstyled price']/li/h3/text()").get()
        review_count = response.xpath("//div[@class='rating-wrapper']/a[@class='review-count']/text()").get()
        image = response.xpath('//*[@id="tmzoom"]/@src').get()

        data = {
            'Code': code,
            'Title': title,
            'Brand': brand,
            'Price': price,
            'Review Count': review_count,
            'Image': image
        }

        yield data