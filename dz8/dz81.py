from pprint import pprint
import json

def find_top_10_more_6(text):
    data = text.split()

    #Оставляем только слова, которые длиннее 6 символов и кладем в словарь,
    #где ключ - слово, а значение - количество повторений
    filtered_words = dict()
    for word in data:
        if len(word) > 6:
            if word in filtered_words.keys():
                filtered_words[word] += 1
            else:
                filtered_words[word] = 1

    return sorted(filtered_words.items(), key=lambda x: filtered_words[x[0]], reverse=True)[0:10]


if __name__ == "__main__":
    all_news_text = ''
    top_10 = dict()
    with open('newsafr.json', 'r', encoding="utf-8") as fjson:
        data = json.load(fjson)
        print(len(data['rss']['channel']['items']))

        #Все новости (без названий) собираем в один файл
        for elem in data['rss']['channel']['items']:
            all_news_text += ' ' + elem['description']

    top_10 = find_top_10_more_6(all_news_text)
    #print(top_10)
    print('\n\nТоп 10 наиболее часто встречающихся слов:')
    for i in top_10:
       print(f'"{i[0]}" встречается {i[1]} раз')



