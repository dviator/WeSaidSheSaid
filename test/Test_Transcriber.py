import unittest2 as unittest
#import transcriber from transcriber.py
import os.path
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from Transcriber.transcriber import Transcriber

#Run from the WeSaidSheSaid root directory
#python test/Test_Transcriber

class Test_Transcriber(unittest.TestCase):
	TestInstance = Transcriber()
	TestInstance.transcribe("http://www.c-span.org/video/?326471-1/hillary-clinton-presidential-campaign-announcement","TestSpeech")
	
	def test_speech_download(self):
		#Checks that the downloader downloaded a dfxp file. 
		self.assertTrue(os.path.isfile("Transcriber/data/TestSpeech.en.dfxp"))

	def test_dfxp_to_srt(self):
		self.assertTrue(os.path.isfile("Transcriber/data/TestSpeech_tmp.srt"))
	def test_srt_to_final(self):
		pass

	#Needs a teardown method that deletes the files that are created between runs. 
if __name__ == '__main__':
    unittest.main()

