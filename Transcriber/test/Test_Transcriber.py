import unittest2 as unittest
#import transcriber from transcriber.py
import os.path

class Test_Transcriber(unittest.TestCase):

	
	def test_speech_download(self):
		#Need to write the code that calls the downloader for a sample website
		self.assertTrue(os.path.isfile("../data/TestSpeech.en.dfxp"))

	def test_dfxp_to_srt(self):
		pass
	def test_srt_to_final(self):
		pass

	#Needs a teardown method that deletes the files that are created between runs. 
if __name__ == '__main__':
    unittest.main()

