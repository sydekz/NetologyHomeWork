import time
import requests
import pprint

SEC_IN_DAY = 60*60*24
tag = 'Python'

if __name__ == "__main__":
    url = f"https://api.stackexchange.com/2.2/questions?sort=activity&site=stackoverflow"
    questions_titles = list()
    questions_count = 0

    need_time = int(time.time()-2*SEC_IN_DAY)
    page_number = 1
    while True:
        response = requests.get(url,
                                params={
                                'fromdate': need_time,
                                'order': 'desc',
                                'tagged': tag,
                                'page': page_number,
                                'pagesize': 100
                            })

        response.raise_for_status()
        data = response.json()
        print(f'Количество вопросов: {len(data["items"])}')

        for item in data['items']:
            questions_count += 1
            question_title = item['title']
            if question_title not in questions_titles:
                questions_titles.append(question_title)

        has_more = data['has_more']
        print(f'Есть следующая страница: {has_more}')

        if has_more == False:
            break

        page_number += 1


    pprint.pprint(questions_titles)
    print(f'Всего добавлено вопросов {questions_count}, количество пропарсенных страниц {page_number}')




