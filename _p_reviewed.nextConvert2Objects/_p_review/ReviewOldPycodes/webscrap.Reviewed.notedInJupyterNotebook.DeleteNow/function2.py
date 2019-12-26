
#web scraping function
#crawl_sitemap.py

from webscrapfunc import *

def crawl_sitemap(url):
	#download the sitemap file
	sitemap = download(url)
	#extract the sitemap links
	links =  re.findall('<loc>(.*?)</loc>', sitemap)
	#download each link
	for link in links:
		html = download(link)
		# scrape html here
		#...
