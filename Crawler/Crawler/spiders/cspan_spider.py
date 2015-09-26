import scrapy

class CspanSpider(scrapy.Spider):
	name = "cspan"
	allowed_domains = ["c-span.org"]
	start_urls = ["http://www.c-span.org/search/?searchtype=Videos&sort=Most+Recent+Airing&all[]=presidential&all[]=campaign&all[]=speech"]
	
	# name = "dmoz"
	# allowed_domains = ["dmoz.org"]

	# start_urls = [
	# "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
	# "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
	# ]
	
	def parse(self, response):
		filename = response.url.split("/")[-2] + '.html'
		print filename
		# with open(filename, 'wb') as f:
		# 	f.write(response.body)
		speechLinks = response.xpath('//section/ul/li/a/@href').extract()
		print speechLinks
		with open("links.txt", 'wb') as f:
			f.write(str(speechLinks))











	# def parse(self, response):
	# 	print response
	# 	print response.url.split("/")
	# 	filename = response.url.split("/")[-1] + '.html'
	# 	print filename
 #        f = open(filename, 'wb')
 #        f.write(response.body)
 #        #f.close()