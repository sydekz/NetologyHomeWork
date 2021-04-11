import requests
from bs4 import BeautifulSoup

KEYWORDS = {'дизайн', 'фото', 'web', 'python', 'stm32l151'}
URL = 'https://habr.com/ru/all/'
PUNCTUATION = '":!.,—()?'

def get_article_text(url):
    #Фунцкция заходит по URL статьи и возвращает ее полный текст
    ret = requests.get(url)
    soup = BeautifulSoup(ret.text, 'html.parser')
    article_text = soup.find('div', id='post-content-body').text.strip().lower()
    return article_text


if __name__ == '__main__':

    ret = requests.get(URL)
    soup = BeautifulSoup(ret.text, 'html.parser')

    articles = soup.find_all('article')

    for article in articles:
        time_text = article.find('span', class_='post__time').text.strip()
        title_element = article.find('a', class_='post__title_link')
        title_text = title_element.text.strip().lower()
        title_url = title_element.attrs.get('href').strip()
        preview_text = article.find('div', class_='post__text').text.strip().lower()

        full_text = title_text + ' ' + preview_text + ' ' + get_article_text(title_url)

        for p in PUNCTUATION:
            if p in full_text:
                full_text = full_text.replace(p, ' ')
        all_words = set(full_text.split())

        result = KEYWORDS & all_words

        if result:
            print(f'<{time_text}> -- <{title_text}> -- <{title_url}>')







