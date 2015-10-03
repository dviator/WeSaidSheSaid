import scrapy
from scrapy.loader import ItemLoader
from Crawler.items import CSPANItem
import psycopg2

#Collect a list of valid candidates from the candidates table in the wsss database. 
conn = psycopg2.connect("dbname=wsss user=wsss")
cur = conn.cursor() 
cur.execute('SELECT fullName from Candidates;')
validCandidates = []
for record in cur:
	validCandidates.append(record[0])
#print validCandidates
print validCandidates[0]
conn.commit()
cur.close()
conn.close()

class CspanSpider(scrapy.Spider):
	name = "cspan"
	allowed_domains = ["c-span.org"]
	start_urls = ["http://www.c-span.org/search/?searchtype=Videos&sort=Most+Recent+Airing&all[]=presidential&all[]=campaign&all[]=speech"]

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

	def write_to_db(self, item):
		#Write the item's contents into the database
		conn = psycopg2.connect("dbname=wsss user=wsss")

		cur = conn.cursor()
		cur.execute('INSERT INTO Speeches (url, title, speaker, collectionTime, speechTime, city, state) VALUES (%s, %s, %s, %s, %s, %s, %s)', (item.url, item.title, item.speaker, item.collectionTime, item.speechTime, item.city, item.state))

		#Commit queued database transactions and close connection
		conn.commit()
		cur.close()
		conn.close()
		pass

	#Method to validate that the video features a speaker from our candidates list
	def validate_speaker(self, speakers):
		pass


	#This function handles those pages which are sent as candidates for presidential campaign speeches.
	def parse_speech_page(self, response):
		print response.headers
		print response.url
		
		#Check that this is indeed a video page
		pageType = response.xpath('body/@class').extract()
		print pageType
		if pageType[0] == 'video event':
			print "It's a video!"

			#Gather video metadata into a CSPAN Item
			l = ItemLoader(item=CSPANItem(), response=response)

			# gather the name of the speaker(s) in this video by searching for the "filter-transcript" id
			# do not forget to post-process this field by comparing the candidate to the acceptable list from the database !!! 
			l.add_xpath('candidate', "//*[contains(concat(' ', @id, ' '), ' filter-transcript ')]/option[@value and string-length(@value)!=0]/text()")

			# gather the title of the video 
			l.add_xpath('title', "//html/head/meta[@property = 'og:title']/@content")

			# add url to the item loader
			l.add_value('url', response.url)

			# gather the date of the video
			l.add_xpath('date', "//div[@class = 'overview']/span[@class = 'time']/time/text()")

			item = l.load_item()
					
			#Write gathered data to the database
			self.write_to_db(item)

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