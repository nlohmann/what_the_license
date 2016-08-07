from unittest import TestCase
import urllib2
import os
import what_the_license

class TestWhatTheLicense(TestCase):
	def test_wtl(self):
		example_url = 'https://github.com/nlohmann/json/releases/download/v2.0.2/json.hpp'
		example_sourcefile = open('json.hpp', 'wb')
		example_sourcefile.write(urllib2.urlopen(example_url).read())
		example_sourcefile.close()

		licenses = what_the_license.wtl(open('json.hpp'))
		self.assertEqual(licenses[0]['license'], 'The MIT License')
		os.remove('json.hpp')
