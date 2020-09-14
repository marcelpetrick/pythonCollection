# Idea is to create a crawler which can 'collect' all the loved songs from a given user account
# Should be a simple warm-up to get familiar with beautiful soup -.-

# official documentation:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#
# install:
# $ pip install beautifulsoup4
# $ pip install lxml

# ok, we need a fake account to crawl: lets do aaabbbccc ;D
# https://www.last.fm/user/aaabbbccc/loved

from bs4 import BeautifulSoup # beautifulstonesoup?!?
import csv

def scrapypediscrap():
    soup = BeautifulSoup(open("https://www.last.fm/user/aaabbbccc/loved"), features="lxml")
    final_link = soup.p.a
    final_link.decompose()

    links = soup.findAll('a')
    for link in links:
        print(link.contents)


scrapypediscrap()
