import sys
import xml.etree.ElementTree as ET
import shutil


def replace_first_lines(file_path):
    with open(file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()
        lines[0] = '<?xml version="1.0" encoding="utf-8"?>\n'
        lines.insert(1, '<!DOCTYPE TS>\n')

        file.seek(0)
        file.writelines(lines)
        file.truncate()


def translateString(input):
    # Implement your translation logic here
    # This is just a placeholder
    translation = "Translated: " + input
    return translation

def transform_ts_file(ts_file_path):
    tree = ET.parse(ts_file_path)
    root = tree.getroot()

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
    if len(sys.argv) < 2:
        print("Usage: python script.py <ts_file_path>")
        return

    ts_file_path = sys.argv[1]
    transform_ts_file(ts_file_path)

if __name__ == "__main__":
    main()
