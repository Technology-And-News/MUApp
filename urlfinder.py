import re

__version__ = 0.1
__doc__ = "Find URLs in a text string"""

url_re = re.compile("(?:\w+://|www\.)[^ ,.?!#%=+][^ ][^ \r]*")
bad_chars = '\'\\.,[](){}:;"'

def find_urls (text):
 return [s.strip(bad_chars) for s in url_re.findall(text)]

