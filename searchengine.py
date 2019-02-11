import urllib3
from BeautifulSoup import *
from urlparse import urljoin


class crawler:
    def __init__(self):
        pass
    def __del__(self):
        pass
    def dbcommit(self):
        pass


    def getTryid(self,table,field,value,createnew = True):
        return None
    def addToindex(self,url,soup):
        print('Indexing {}'.format(url))
    def getTextonly(self,soup):
        return None
    def sepreateWords(self,text):
        return None
    def isIndexed(self,url):
        return False
    def addLinkref(self,urlForm,urlTo,linkText):
        pass
    def crawl(self,pages,depth=2):
        pass
    def createIndextables(self):
        pass