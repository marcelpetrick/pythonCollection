# author mail@marcelpetrick.it
# license: GPLv3.0
#
#-----------------------------------------------------------------
# Idea is to create a crawler which can 'collect' all the loved songs from a given user account
# Should be a simple warm-up to get familiar with beautiful soup -.-

# official documentation:
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
#
# install:
# $ pip3 install beautifulsoup4 requests lxml

# ok, we need a n existing clown-account to crawl: lets take aaabbbccc ;D
# https://www.last.fm/user/aaabbbccc/loved

# let's try another tutorial, since the one is used first is without 'requests'
# https://hackersandslackers.com/scraping-urls-with-beautifulsoup/
#-----------------------------------------------------------------

import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import unquote_plus

headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

#-----------------------------------------------------------------

def createBaseUrl(username):
    baseUrl = "https://www.last.fm/user/" + username + "/loved?page="

    return baseUrl

#-----------------------------------------------------------------

def scrapypediscrap():

    currentTime = time.time()
    baseUrl = createBaseUrl("aaabbbccc") # param is the username

    completeLovedTrackCollection = set()
    lastResult = set()

    page = 0
    while True:
        page += 1
        url = baseUrl + str(page)
        currentResult = scrapArtistTrackFromPage(url)
        print("current result:", currentResult)

        if currentResult == lastResult:
            print("stop scraping, because the results were already parsed!")
            break

        completeLovedTrackCollection = completeLovedTrackCollection.union(currentResult)
        lastResult = currentResult

    print("--------------------------------------")
    print("final:", completeLovedTrackCollection)
    print("loved tracks:", len(completeLovedTrackCollection))
    print("scraping took ", time.time() - currentTime, "seconds")
    print("--------------------------------------")

    # one final, properly usable output
    for elem in completeLovedTrackCollection:
        print(elem[0], "//", elem[1])
    print("--------------------------------------")

#-----------------------------------------------------------------

def scrapArtistTrackFromPage(url):
    print("--------------------------------------")
    print("url is:", url)

    # do the request
    currentTime = time.time()
    req = requests.get(url, headers)
    print("request took ", time.time() - currentTime, "seconds")
    print("status code:", req.status_code)

    # todo a solution for the iteration: instead of parsing the footer for the pagination thingy (what is the maximum page?),
    # just compare the track-artist-parsing-result from last page with current page: if identical, then a non-existent page was requested! #avoidTheProblem ..
    if not req.status_code == 200: #check for status code "success", but last.fm falls back to the last loved tracks page (here 4) .. uff
        print("failure; page not successfully downloaded")
        return

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

    # "processing"
    currentTime = time.time()

    result = set()
    classes = soup.find_all("td", class_="chartlist-name")
    for hit in classes:
        #print(hit) # wow, that is really what I need!
        artistAndTrack = parseClassResult(hit)
        #print(artistAndTrack) # just as proof of concept
        result.add(artistAndTrack)

    print("processing took ", time.time() - currentTime, "seconds")

    return result

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
    # decode the html-transcript (also replace "+" with space); see: https://docs.python.org/3/library/urllib.parse.html#urllib.parse.unquote_plus
    artistAndTrack = unquote_plus(targetString).replace("&amp;", "&").split(splitter)
    #print("artistAndTrack:", artistAndTrack)
    return tuple(artistAndTrack)

# ------------- trigger (warning) ---------------
scrapypediscrap()
