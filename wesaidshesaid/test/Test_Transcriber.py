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
		#Checks that an intermediate SRT File was created
		self.assertTrue(os.path.isfile("Transcriber/data/TestSpeech_tmp.srt"))

	def test_srt_to_final(self):
		TestInstance = Transcriber()
		TestInstance.transcribe("http://www.c-span.org/video/?326471-1/hillary-clinton-presidential-campaign-announcement","TestSpeech")
		self.assertIsNotNone(TestInstance.getSpeech())
		
		#Write speech to file (For reprodution and test preparation)
		#Normally commented out
		# f = open("test/data/HillarySpeechExampleOutput",'w')
		# f.write(str(TestInstance.SPEECH[0]))

		#Open example file and compare to output.
		t = open("test/mockData/HillarySpeechExampleOutput",'r')
		speechText = t.read()
		self.assertEquals(str(TestInstance.SPEECH[0]),speechText)

		#TODO: Remove / from the apostrophes in the speech text. Currently each ' is preceded by a /
		#Script for creating model data file.
		# f = open("test/data/HillarySpeechExampleOutput",'w')
		# f.write(str(TestInstance.SPEECH[0]))
	def test_trump(self):
		TrumpInstance = Transcriber()
		TrumpInstance.transcribe("http://www.c-span.org/video/?328138-1/donald-trump-town-hall-meeting-rochester-new-hampshire","TrumpTest")
		self.assertIsNotNone(TrumpInstance.getSpeech())

		#Write speech to file (For reprodution and test preparation)
		#Normally commented out
		# x = open("test/data/TrumpFinal.txt","w")
		# x.write(str(TrumpInstance.SPEECH[0]))

		x = open("test/mockData/TrumpFinal.txt","r")
		trumpText = x.read()
		self.assertEquals(str(TrumpInstance.SPEECH[0]),trumpText)
		
		
	#Needs a teardown method that deletes the files that are created between runs. 
if __name__ == '__main__':
    unittest.main()

