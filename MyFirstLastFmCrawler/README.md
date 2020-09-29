# tl;dr:
Simple webscraper with Python and BeautifulSoup for one user’s favorite tracks (‘loved songs’) at last.fm.

# full text:
Looks like last.fm is shutting down its services (one feature at at time, lol). They started this process more or less ten years ago.
I’ve realized that I would miss my curated list of favorite tracks and I am also very bad at remembering, so … let’s automate the process of grabbing that information from their public page. I know, they offer a REST API, but I wanted to use once BS4.
Since I had somehow two free hours fourteen days ago, I went full-speed to some tutorials, played with the get-requests and how to parse. And then spent the last minutes parsing the received “artist+track”-string into something usable. Alltogether four hours were spent and I am amazed by the result. Of course, by leveraging three quite powerful libraries (beautifulsoup4, requests, lxml) and skipping TDD (;) I’ve reached the goal quite fast. And since the script works (my 1500 loved songs are scraped in less than 60 seconds), I will also not spend additional effort to make it “pretty”.

# author
mail@marcelpetrick.it

# license
GNU GPL v3.0
