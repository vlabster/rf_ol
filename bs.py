from lxml import html
import requests
# from urllib2 import urlopen
from bs4 import BeautifulSoup

url = requests.get('https://www.facebook.com/zuck')
soup = BeautifulSoup(url.text)
a = soup.findAll('a', {"class": "_2nlw _2nlv"})
print(a[0].text)
photo = soup.findAll('img', {"class": "_11kf img"})
src = photo[0].attrs['src']
print(src)
# print(soup.head)


# tree = html.fromstring(url.text)
# print(tree)
# a = tree.xpath(".//*[contains(@class, '_2nlw _2nlv')]")

# print(a)
# _2nlw _2nlv