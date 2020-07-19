import random
import string
import sys

urlDict = {}

def __genRandomShortUrl():
	return ''.join(random.SystemRandom().choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=6))

def shorten(long_url):
	if long_url == None:
		return None

	long_url = long_url.strip()

	if len(long_url) == 0:
		return None

	shortUrl = __genRandomShortUrl()

	while shortUrl in urlDict.keys():
		shortUrl = __genRandomShortUrl()

	urlDict[shortUrl] = long_url
	return shortUrl

def original(short_url):
	try:
		return urlDict[short_url]
	except KeyError as e:
		return None

def __handleFile(fileName):
	try:
		with open(fileName, 'r') as file:
			lines = file.readlines()
			wfile = open('short-'+fileName, 'w')
			for url in lines:
				wfile.writelines(shorten(url.strip('\n')))
				wfile.writelines('\n')
			wfile.close()
			print('Short URLs are saved in short-'+fileName)
	except OSError as e:
		print(shorten(fileName))

if __name__ == '__main__':
	argumentList = sys.argv
	argumentList.remove(argumentList[0])

	if len(argumentList) == 1:
		__handleFile(argumentList[0])
	elif len(argumentList) > 1:
		for url in argumentList:
			print(shorten(url))
	else:
		print('Give file name or URL(s) as input')
