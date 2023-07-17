# for the package - newer versions are broken!
# pip install translators==5.3.1

# for the backend:
# pacman -S nodejs npm

import time
import translators

def translateString(input, fromLang, toLang):
    startTime = time.time()
    result = translators.google(input, fromLang, toLang) # or deepl or yandex
    print(f"translateString: translation took {time.time() - startTime}s")

    return result

for a in range(0,5):
    print("** run ", a, "**")
    print(translateString("Kuh Haus Maus Klaus", "de", "en"))
    print(translateString("Das ist eine Pizza", "de", "en"))
    print(translateString("dritter Call", "de", "en"))

# Result: most of the time the three calls are only translated until the second request: last one fails due to
# requests.exceptions.HTTPError: 429 Client Error:  for url: https://www2.deepl.com/jsonrpc?method=LMT_handle_jobs
# maybe using a delay would help: else: other backend (yes, this worked)? or: doing batch-translations?
