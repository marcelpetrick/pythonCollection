import sys
import xml.etree.ElementTree as ET


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


def translateString(input):
    """
    Translates a given string. The actual implementation should be replaced
    with your desired translation logic.

    :param input: The string to translate
    :type input: str
    :return: The translated string
    :rtype: str
    """
    # Implement your translation logic here
    # This is just a placeholder
    translation = "Translated: " + input
    return translation


def transform_ts_file(ts_file_path):
    """
    Transforms a .ts file by translating all 'unfinished' messages.
    The translated messages replace the original messages in the .ts file.

    :param ts_file_path: The path to the .ts file to transform
    :type ts_file_path: str
    """
    tree = ET.parse(ts_file_path)
    root = tree.getroot()

    # Iterate over all 'message' elements in the XML tree
    for message in root.iter('message'):
        translation = message.find('translation')
        if translation is not None and translation.attrib.get('type') == 'unfinished':
            source_text = message.find('source').text
            translated_text = translateString(source_text)
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
    if len(sys.argv) < 2:
        print("Usage: python script.py <ts_file_path>")
        return

    ts_file_path = sys.argv[1]
    transform_ts_file(ts_file_path)


if __name__ == "__main__":
    main()
