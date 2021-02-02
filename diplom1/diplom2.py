import requests
import time
import os
import json

MAX_PHOTOS_COUNT = 5

class VKPhotos:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version
        }

    def get_profile_photos(self, id_vk, count):
        '''Ограничение по количеству скачиваемых фотографий - 50
        Возвращает список URL с фотографиями
        Отдает -1, None если не удалось отправить запрос или профиль забанен, закрыт и т.д.
        '''
        print(type(id_vk))
        if not type(id_vk) is int:
            print('Error get_profile_photos: wrong type of input parameter id_vk')
            return -1, None

        dphotos = dict()
        photos_url = self.url + 'photos.get'

        photos_params = {
            'owner_id': id_vk,
            'album_id': 'profile',
            'photo_sizes': 1,
            'extended': 1,
            'count': count
        }

        response = requests.get(photos_url, params={**self.params, **photos_params})
        response.raise_for_status()
        data = response.json()
        if 'error' in data:
            print('Error')
            return -1, None

        likes = 0
        photo_url = ''
        for photos in data['response']['items']:
            likes, photo_url, current_size = self.__find_max_photo_size(photos)
            dphotos[photo_url] = [likes, current_size]
        return data['response']['count'], dphotos

    def __find_max_photo_size(self, photo_sizes):
        '''Ищет максимальный размер по высоте.
        Если height = 0 для всех форматов, то скорее всего старая версия
        фото до 2012 года и берем последний вариант'''
        height = 0
        url = ''
        current_size = ''

        for size in photo_sizes['sizes']:
            if size['height'] >= height:
                height = size['height']
                url = size['url']
                current_size = size['type']

        if height == 0:
            url = photo_sizes['sizes'][-1]['url']

        print(f"likes: {photo_sizes['likes']['count']} Height: {height} - url {url}")
        return photo_sizes['likes']['count'], url, current_size

class YaUploader:
    def __init__(self, token):
        self.token = token

    def upload(self, file_path):
        """Метод загруджает файл file_path на яндекс диск"""
        filename = file_path.split('/')[-1]
        print(filename)
        response = requests.get('https://cloud-api.yandex.net/v1/disk/resources/upload',
                                params={
                                    'path': file_path,
                                    'overwrite': 'true'
                                },
                                headers={
                                    'Authorization': f"OAuth {self.token}"
                                })

        response.raise_for_status()
        href = response.json()['href']

        with open(filename, "rb") as f:
            put_response = requests.put(href, f)
        return put_response


    def create_folder(self, folder_name):
        response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                                params={
                                    'path': folder_name,
                                },
                                headers={
                                    'Authorization': f"OAuth {self.token}"
                                })

        response.raise_for_status()


def get_sec_data():
    print('\n\n\nStart Initializing...')
    # Получаем токен_vk из файла, на второй строчке токен из Яндекса
    # В третьей строчке ID пользователя ВК считываем
    with open('../secdata.txt') as f:
        token_vk = str(f.readline()).strip()
        print(f'VK Token - {token_vk}')
        token_ya = str(f.readline()).strip()
        print(f'Yandex API Token - {token_ya}')
        vk_user_id = int(str(f.readline()).strip())
        print(f'User ID - {vk_user_id}')

    return VKPhotos(token_vk, '5.126'), YaUploader(token_ya), vk_user_id

def get_and_save_photos():
    vk_client, uploader, vk_user_id = get_sec_data()

    print('\nInitialization Complete!')

    # Создаем уникальную категорию
    folder_name = 'dipfolder' + str(time.time()).split('.')[-1]

    # Создаем категорию на Yandex диске
    uploader.create_folder(folder_name)

    print('\nStarting getting photos from VK ID')
    count, dphotos = vk_client.get_profile_photos(vk_user_id, MAX_PHOTOS_COUNT)

    if count <= MAX_PHOTOS_COUNT:
        print(f'\nWe took {count} photos!')
    else:
        print(f'\nWe took {MAX_PHOTOS_COUNT}! Total of {count} photos found')

    # Массив размеров
    dsizes = list()

    # Массив имен файлов
    dnames = list()

    print('\nStarting downloading photos from VK and save them on Yandex.Disk')
    files_iter = 0
    if count == -1:
        print('Error in vk_client.get_profile_photos')
    else:
        for url, data in dphotos.items():
            if files_iter >= MAX_PHOTOS_COUNT:
                break
            files_iter += 1

            name = str(data[0]) + '.jpg'
            if name in dnames:
                # уникализируем название файла, если оно уже встречается
                name = str(time.time()) + name

            dnames.append(name)
            dsizes.append(data[1])

            p = requests.get(url)
            with open(name, "wb") as out:
                out.write(p.content)

            file_path = '/' + folder_name + '/' + name
            uploader.upload(file_path)

            if os.path.isfile(name):
                os.remove(name)

        print('\nAll Photos saved on Yandex.Disk')
        print('\nGenerating and saving json file')
        djson = list()
        n = len(dnames)
        for i, data in enumerate(dnames, 0):
            djson.append({"file_name": data, "size": dsizes[i]})

        with open('json.json', 'w') as f:
            json.dump(djson, f, ensure_ascii=False, indent=2)

        print('\nComplete - generating and saving json')


if __name__ == '__main__':
    get_and_save_photos()
    print('\nAll done')




