from bs4 import BeautifulSoup as Soup
from soupselect.soupselect import select
import string
import requests

class Crawler(object):

    def __init__(self):
	self.sites = ['http://www.usingenglish.com/reference/phrasal-verbs/%s.html' % l for l in string.ascii_lowercase]

    def crawl(self):
	self.all_phrasals = []
	for site in self.sites:
	    html = requests.get(site).text
	    soup = Soup(html)
	    selected = select(soup, '.divbox a strong')
	    phrasals = [s.contents[0] for s in selected]
	    self.all_phrasals += phrasals


c = Crawler()
c.crawl()
for p in c.all_phrasals:
    print p