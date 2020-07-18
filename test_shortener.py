import unittest
import shortener

class TestShortener(unittest.TestCase):
	
	def setUp(self):
		self.long_url1 = 'google.com/photo/123'
		self.long_url2 = 'yahoo.com/mail/111'

	def tearDown(self):
		pass

	def test_shorten(self):
		self.assertEqual(len(shortener.shorten(self.long_url1)), 6, 'Should be 6 characters long')
		shortUrl1 = shortener.shorten(self.long_url1)
		shortUrl2 = shortener.shorten(self.long_url1)
		self.assertFalse(shortUrl1 == shortUrl2, 'Should return different shortened urls for successive calls using same url')
		shortUrl3 = shortener.shorten(self.long_url2)
		self.assertFalse(shortUrl1 == shortUrl3, 'Should return different shortened urls for different long urls')

	def test_original(self):
		original_url = shortener.original(shortener.shorten(self.long_url1))
		self.assertTrue(original_url == self.long_url1, 'Should return original url')
		self.assertIsNone(shortener.original(self.long_url2), 'Should return None if url not found')

if __name__ == '__main__':
	unittest.main()