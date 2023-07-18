"""
This is a Python script for testing the translation capabilities of the translators library.
It makes use of the translators library to translate individual strings from one language
to another. It measures the time it takes to perform the translations.
"""

# for the package - newer versions are broken!
# pip install translators==5.3.1

# for the backend:
# pacman -S nodejs npm

import time
import translators


def translate_string(input_text, from_lang, to_lang):
    """
    Translate a string from one language to another.

    :param input_text: The string to translate.
    :type input_text: str
    :param from_lang: The ISO 639-1 code of the language to translate from.
    :type from_lang: str
    :param to_lang: The ISO 639-1 code of the language to translate to.
    :type to_lang: str
    :return: The translated string.
    :rtype: str
    """
    start_time = time.time()
    result = translators.google(input_text, from_lang, to_lang)  # or deepl or yandex
    print(f"translate_string: translation took {time.time() - start_time}s")

    return result


for a in range(0, 5):
    print("** run ", a, "**")
    print(translate_string("Kuh Haus Maus Klaus", "de", "en"))
    print(translate_string("Das ist eine Pizza", "de", "en"))
    print(translate_string("dritter Call", "de", "en"))

# Result: most of the time the three calls are only translated until
# the second request: last one fails due to
# requests.exceptions.HTTPError: 429 Client Error:
# for url: https://www2.deepl.com/jsonrpc?method=LMT_handle_jobs
#
# maybe using a delay would help
# else: other backend (yes, this worked)?
# or: doing batch-translations?
