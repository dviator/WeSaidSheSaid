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
		with open(filename, 'wb') as f:
			f.write(response.body)
		#Extract the links to the search results on the page.
		speechLinks = response.xpath('//section/ul/li/a/@href').extract()
		# print speechLinks
		# with open("links.txt", 'wb') as f:
		# 	f.write(str(speechLinks))

		#Generate a new crawl request for each link followed that treats them as speech videos. 
		for url in speechLinks:
			url = response.urljoin(url)
			yield scrapy.Request(url, callback=self.parse_speech_page)


	#This function handles those pages which are sent as candidates for presidential campaign speeches.
	def parse_speech_page(self, response):
		print response.headers
		print response.url
		
		#Check that this is indeed a video page
		pageType = response.xpath('body/@class').extract()
		print pageType
		if pageType[0] == 'video event':
			print "It's a video!"

			#Gather video metadata

			# gather the name of the speaker(s) in this video by searching for the "filter-transcript" id
			speaker = response.xpath("//*[contains(concat(' ', @id, ' '), ' filter-transcript ')]/option[@value and string-length(@value)!=0]/text()").extract()
			print "speaker is: ", speaker

		#Call Transcriber class

		#Either add to item to collect as one feed or call insert to database function.


		#Prints the html of the webpage as a text file in current directory. Useful for finding the paths to follow.
		#Use with sublime's reindent feature for easy to follow html
		#pageTitle = response.url.split("/")[-1] + '.html'
		# with open(pageTitle, 'wb') as f:
		# 	f.write(str(response.body))











	# def parse(self, response):
	# 	print response
	# 	print response.url.split("/")
	# 	filename = response.url.split("/")[-1] + '.html'
	# 	print filename
 #        f = open(filename, 'wb')
 #        f.write(response.body)
 #        #f.close()