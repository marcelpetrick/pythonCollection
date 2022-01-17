# GPL v3
# author: mail@marcelpetrick.it

# idea: call like `python autoTrans.py input.ts output.ts` (later input is edited in place)
# Replace all untranslated strings with the respective result from some online-translator.
#
# Steps? Read file linewise (tbd: may pose a problem for wrapped strings ..),
# then take input and call whatever API (or webscrape?) and then replace it in the file.

# ------------------------------------------------------------------------------------------------------------
def simpleTest():
    # use this to fix problem with latest release which reports ".. no token .."
    # `pip install googletrans==4.0.0-rc1`
    from googletrans import Translator

    translator = Translator()

    translation = translator.translate('Überbackenes Weißbrot mit Wiener Schnitzel und Tomaten.', src='de', dest='en')
    # obviously the v4.0-rc1 has an issue with bulk translations: https://github.com/ssut/py-googletrans/issues/264

    print(translation.origin, " -> ", translation.text)

    # original from the official googletrans-page
    #translations = translator.translate(['The quick brown fox', 'jumps over', 'the lazy dog'], dest='ko')
    #for translation in translations:
    #    print(translation.origin, ' -> ', translation.text)
# ------------------------------------------------------------------------------------------------------------
simpleTest()
