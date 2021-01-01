from dz81 import find_top_10_more_6
import xml.etree.ElementTree as ET

if __name__ == '__main__':
    all_news_text = ''
    top_10 = dict()

    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()

    xml_items = root.findall('channel/item')

    for elem in xml_items:
        all_news_text += elem.find('description').text

    top_10 = find_top_10_more_6(all_news_text)
    # print(top_10)
    print('\n\nТоп 10 наиболее часто встречающихся слов:')
    for i in top_10:
        print(f'"{i[0]}" встречается {i[1]} раз')
