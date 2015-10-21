import unittest2 as unittest
import os
import os.path
# import subprocess
import psycopg2
import datetime
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

# How to import the crawler class and db functions from the root directory
root = os.environ['WSSS_ROOT']
print root
tpath = os.path.join(root, root + '/wesaidshesaid/Crawler')
dpath = os.path.join(root, root + '/wesaidshesaid/db')
sys.path.insert(0,tpath)
sys.path.insert(0,dpath)

# running scrapy from a script requires the following API
import scrapy
from scrapy.crawler import CrawlerProcess
from Crawler.spiders.cspan_spider import CspanSpider

class Test_Crawler(unittest.TestCase):
	
	### Test the validate speaker helper function
	def test_validate_speaker(self):
		Test_Instance = CspanSpider()
		test_group = [
		'Bernard Sanders'
		]

		valid = Test_Instance.validate_speaker(test_group)
		self.assertIsNotNone(valid)

	### Test to see if we are correctly writing to the database correctly
	def test_write_to_db(self):
		Test_Instance = CspanSpider()

		test_time = datetime.datetime.now()
		print test_time
		test_item = {
			'url': ["http://www.test.com"],
			'title': ["testing"],
			'speaker': "Donald Trump",
			'transcription': ["All Mexicans are rapists and drug dealers, well not all of them but most of them."],
			'collectionTime': [test_time],
			'speechTime': ['October 14, 2045'],
			'city': ["Austin"],
			'state': ["Texas"]
		};

		# try:
		# 	Test_Instance.write_to_db(test_item)
		# except:
		# 	self.fail(msg="-E- Error while testing the write_to_db function, please check test.")

		Test_Instance.write_to_db(test_item)

		conn = psycopg2.connect("dbname=wsss user=wsss")
		curr = conn.cursor()
		curr.execute('SELECT * FROM Speeches WHERE url = %s', ['http://www.test.com'])
		valid = curr.fetchone()

		curr.execute('DELETE FROM Speeches WHERE url = %s', ['http://www.test.com'])

		conn.commit()
		curr.close()
		conn.close()

		self.assertIsNotNone(valid)


	### The following test actualy runs the cspan spider and collects runtime stats
	# def test_spider_run(self):
	# 	# subprocess.call(["python", dpath + "/CleanDatabase.py"])
	# 	execfile(dpath + "/CleanDatabase.py")
	# 	process = CrawlerProcess({
	# 		'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
	# 		})

	# 	process.crawl(CspanSpider)
	# 	process.start()

	# 	self.assertTrue(True)

# if __name__ == '__main__':
#     unittest.main()
if __name__ == '__main__':
   log_file = 'test_crawler.log'
   f = open(log_file, "w")
   runner = unittest.TextTestRunner(f)
   unittest.main(testRunner=runner)
   f.close()