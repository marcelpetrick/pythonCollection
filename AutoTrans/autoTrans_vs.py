import sys
import xml.etree.ElementTree as ET
import shutil

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

    tree.write(ts_file_path, encoding='utf-8', xml_declaration=True)

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
