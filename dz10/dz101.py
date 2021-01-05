import requests
import pprint

class VkUser:
    url = 'https://api.vk.com/method/'
    def __init__(self, token, version):
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version
        }
        response = requests.get(self.url+'users.get', self.params)
        response.raise_for_status()
        print(response.json())
        self.owner_id = response.json()['response'][0]['id']

    def get_id_friends(self, id_vk=None):
        '''Ограничение по количеству скачиваемых друзей - 5000
        Отдает два параметра количество друзей и список ID друзей)
        Отдает -1, None если не удалось отправить запрос или профиль забанен, закрыт и т.д.
        Если ничего не указывать, то запрашивает для своего профиля'''
        dfriends = list()
        if id_vk == None:
            id_vk = self.owner_id
        friends_url = self.url + 'friends.get'
        friends_params = {
            'user_id': id_vk
        }

        response = requests.get(friends_url, params={**self.params, **friends_params})
        response.raise_for_status()
        data = response.json()
        if 'error' in data:
            print('Error')
            return -1, None

        #pprint.pprint(data)
        for friend in data['response']['items']:
            dfriends.append(friend)
        return data['response']['count'], dfriends

    def get_common_friends(self, id1, id2):
        '''Отдает два параметра (количество общих друзей и список ID общих друзей)
        Отдает -1, None если не удалось отправить запрос или один из профилей забанен, закрыт и т.д.
        '''
        count_friends1, dfriends1 = self.get_id_friends(id1)
        count_friends2, dfriends2 = self.get_id_friends(id2)

        if count_friends1 == -1 or count_friends2 == -1:
            return -1, None

        common_friends = set(dfriends1).intersection(set(dfriends2))

        return len(common_friends), list(common_friends)


if __name__ == '__main__':
    #Получаем токен из файла
    with open('../secdata.txt') as f:
        token = str(f.readline()).strip()
        print(token)

    vk_client = VkUser(token, '5.126')
    print(vk_client.owner_id)
    friends_count, friends_list = vk_client.get_id_friends()

    print(f'Количество друзей у пользователя {friends_count}')
    print('Список ID друзей:')
    pprint.pprint(friends_list)

    friends_count_common, friends_common_list = vk_client.get_common_friends(23491, 23327)
    print(f'Количество общих друзей у пользователей {friends_count_common}')
    print('Список ID общих друзей:')
    pprint.pprint(friends_common_list)
