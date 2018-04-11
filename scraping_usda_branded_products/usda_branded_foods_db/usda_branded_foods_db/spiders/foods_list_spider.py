import scrapy

class FoodSpider(scrapy.Spider):
	name = 'food'

	def start_requests(self):
		urls =[]
		for url in urls:
			yield scrapy.Request(url=url, callback=self.parse)