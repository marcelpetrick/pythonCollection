import sys
import xml.etree.ElementTree as ET
import time
import translators

def replace_first_lines(file_path):
    """
    Replaces the first two lines of a file with the XML declaration and DOCTYPE.

    :param file_path: The path to the file to modify
    :type file_path: str
    """
    with open(file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        lines[0] = '<?xml version="1.0" encoding="utf-8"?>\n'
        lines.insert(1, '<!DOCTYPE TS>\n')

        file.seek(0)
        file.writelines(lines)
        file.truncate()


def translateString(input: str, fromLang: str, toLang: str) -> str:
    """
    Translate a string from one language to another.

    This function uses Google's translation service, but could be modified to use another service like DeepL or Yandex.
    The translation process is timed, and the duration is printed alongside the original and translated strings and the source and target languages.

    Parameters:
    input (str): The string to translate.
    fromLang (str): The ISO 639-1 code of the language to translate from.
    toLang (str): The ISO 639-1 code of the language to translate to.

    Returns:
    str: The translated string.

    Example:
    >>> translateString("hello world", "en", "es")
    'hola mundo'
    """
    startTime = time.time()
    output = translators.google(input, fromLang, toLang) # or deepl or yandex
    print(f"translateString: {time.time() - startTime}s : {input} -> {output} ({fromLang} -> {toLang})")

    return output

def transform_ts_file(ts_file_path, sourceLanguage, targetLanguage):
    """
    Transforms a .ts file by translating all 'unfinished' messages.
    The translated messages replace the original messages in the .ts file.

    :param ts_file_path: The path to the .ts file to transform
    :type ts_file_path: str
    """
    tree = ET.parse(ts_file_path)
    root = tree.getroot()

    #sourceLanguage, targetLanguage = 'en', 'de' # todo make this dependent on the given parameters, maybe read from ts-file

    # Iterate over all 'message' elements in the XML tree
    for message in root.iter('message'):
        translation = message.find('translation')
        if translation is not None and translation.attrib.get('type') == 'unfinished':
            source_text = message.find('source').text
            translated_text = translateString(source_text, sourceLanguage, targetLanguage)
            translation.text = translated_text
            del translation.attrib['type']

    tree.write(ts_file_path, encoding='utf-8', xml_declaration=True)

    # Replace the first two lines of the output file
    replace_first_lines(ts_file_path)

    # Preserve the last empty line
    with open(ts_file_path, 'a', encoding='utf-8') as file:
        file.write('\n')

    print("TS file transformed successfully.")


def main():
    """
    The main entry point of the script. It checks if a file path was given as
    command line argument and if so, calls the function to transform the .ts file.
    """
    if len(sys.argv) < 4:
        print("Usage: python script.py <ts_file_path> sourceLanguage targetLanguage")
        return

    ts_file_path = sys.argv[1]
    startTime = time.time()
    transform_ts_file(ts_file_path, sys.argv[2], sys.argv[3])
    print(f"Whole execution took {time.time() - startTime}s.")

if __name__ == "__main__":
    main()

# test call:
#  python autoTrans_vs.py testing/helloworld.ts en de

# another example:
#
# (venv) [mpetrick@marcel-precision3551 AutoTrans]$  python autoTrans_vs.py testing/helloworld.ts en cn
# Using Germany server backend.
# translateString: 1.3896245956420898s : Hello world! -> 你好世界！ (en -> cn)
# translateString: 1.9492523670196533s : My first dish. -> 我的第一道菜。 (en -> cn)
# translateString: 2.112003803253174s : white bread with butter -> 白面包和黄油 (en -> cn)
# TS file transformed successfully.
# Whole execution took 5.453961610794067s.
# (venv) [mpetrick@marcel-precision3551 AutoTrans]$
