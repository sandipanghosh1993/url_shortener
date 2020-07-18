# URL Shortener
## About
A URL shortener library (e.g. bitly). Given a long URL, the program returns a shortened URL
## Usage
Should be python 3.0 or above version installed
 
```
import shortener

long_url = 'https://google.com/xyz/123'

short_url = shortener.shorten(long_url)
long_url = shortener.original(short_url)

```
Long URLs input from console
```
>>python shortener.py 'google.com/xyz/123' 'yahoo.com/abc/111'

```
Input from a file of new line separated long URLs
```
>>python shortener.py long_urls.txt

```