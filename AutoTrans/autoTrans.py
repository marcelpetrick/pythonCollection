# spdx: GNU General Public License v3.0 only
# author: mail@marcelpetrick.it
# year: 2022

# idea: call like `python autoTrans.py input.ts output.ts` (later input is edited in place)
# Replace all untranslated strings with the respective result from some online-translator.
#
# Steps? Read file linewise (tbd: may pose a problem for wrapped strings ..),
# then take input and call whatever API (or webscrape?) and then replace it in the file.
#
# # todos
# * create a requirements.txt
# * add unit-tesing (at least the given ts-file should be translated properly)



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

# ------------------------------------------------------------------------------------------------------------
# xml parsing text. just open and try to grab some nodes
# follows mostly https://realpython.com/python-xml-parser/#choose-the-right-xml-parsing-model for understanding the different possibilites
def parsingxMLTest():
    from xml.dom.minidom import parse, parseString
    document = parse("testing/helloworld.ts")
    print(document.version, document.encoding, document.standalone)  # 1.0 utf-8 None

    root = document.documentElement
    contexts = root.getElementsByTagName("context")
    print("elemByTag:", contexts)  # [<DOM Element: context at 0x2b1c3d0e1f0>, <DOM Element: context at 0x2b1c3d331f0>]

    for elem in contexts:
        messages = elem.getElementsByTagName("message")
        print("messages:", messages)

        for elem in messages:
            translation = elem.getElementsByTagName("translation")
            print("translation:", translation)

            ## todo: check if the typ of translation is "unfinished" (how is this called?) and if yes, then take "source" and translate

            #nodeAttributes = translation.attributes
            #print("nodeAttributes:", nodeAttributes)

            for t in translation:
                if t.hasAttribute("type"):
                    print("hss attribute..")
                    nodeType = t.getAttribute("type") # see: https://docs.python.org/3/library/xml.dom.html#dom-attr-objects
                    print("nodeType:", nodeType) # nodeType: unfinished


            ## insert the result in "translation" and remove that "unfinished" tag

    # todo print/store the modified xml! done

parsingxMLTest()
