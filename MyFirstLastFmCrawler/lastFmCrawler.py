# Idea is to create a crawler which can 'collect' all the loved songs from a given user account
# Should be a simple warm-up to get familiar with beautiful soup -.-

# official documentation:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#
# install:
# $ pip install beautifulsoup4
# $ pip install lxml
# $ pip3 install beautifulsoup4 requests

# ok, we need a fake account to crawl: lets do aaabbbccc ;D
# https://www.last.fm/user/aaabbbccc/loved

# let's try another tutorial, since the one is used first is without 'requests'
# https://hackersandslackers.com/scraping-urls-with-beautifulsoup/

import requests
from bs4 import BeautifulSoup # beautifulstonesoup?!?
from urllib.parse import unquote

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

def scrapypediscrap():
    url = "https://www.last.fm/user/aaabbbccc/loved?page=1"
    req = requests.get(url, headers)
    soup = BeautifulSoup(req.content, "lxml")
    #print(soup.prettify())

    # as we can see: taking from this class would make it easy, but for that a playable youtube-url has to be set:
    # class="chartlist-play-button js-playlink"

    # better idea: taking this 'td' with its inner 'href' already gives a url, which offers artist and track title (space encoded by plus sign  .. which shall be reversed)
    # "<td class="chartlist-name" data-toggle-button="" data-toggle-button-current-state="loved" data-toggle-button-group-id="5d87cd285ae9e24bf13794439c0c61de">
    #              <a class="" href="/music/Taking+Back+Sunday/_/Cute+Without+The+E+(cut+From+The+Team)" title="Cute Without The E (cut From The Team)">
    #               Cute Without The E (cut From The Team)
    #              </a>
    #             </td>"

    classes = soup.find_all("td", class_="chartlist-name")
    for hit in classes:
        #print(hit) # wow, that is really what I need!
        artistAndTrack = parseClassResult(hit)
        print(artistAndTrack) # just as proof of concept

# -------------
def parseClassResult(input):
    #print("-----------------------------------------------------------")
    input = str(input).replace("\n", " ") # stringify and flatten the input first
    #print(input)
    starter = "href="
    end = "title="
    indexA = input.find(starter)
    indexB = input.find(end, indexA)

    #print("first, last:", indexA, indexB)
    targetString = input[indexA + 13 : indexB - 2]
    #print("targetString:", targetString)

    # now we have something in that format:
    # targetString: Billy+Currington/_/Love+Done+Gone

    # split into artist and track
    splitter = "/_/"
    # unquote before, else problems with those special characters
    tuple = unquote(targetString).replace("+", " ").split(splitter)
    #print("tuple:", tuple)
    artistAndTrack = (tuple[1], tuple[0]) # reverse order

    return artistAndTrack

# ------------- trigger (warning) ---------------
scrapypediscrap()
