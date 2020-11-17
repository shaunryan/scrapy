
import urllib.parse as urlparse

root = urlparse.urlparse("http://quotes.toscrape.com/page/1/")
root = f"{root.scheme}//{root.netloc}"


