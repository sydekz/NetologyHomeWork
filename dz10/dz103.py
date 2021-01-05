from dz102 import VkUserPro
import requests
import pprint
import time

class VkUserUltra(VkUserPro):
    def __str__(self):
        new_params = {'fields': 'domain',
                      'user_ids': self.owner_id}
        response = requests.get(self.url + 'users.get', params={**self.params, **new_params})
        response.raise_for_status()
        # print(response.json())
        domain_name = response.json()['response'][0]['domain']

        return 'https://vk.com/' + domain_name



if __name__ == '__main__':
    # Получаем токен из файла
    with open('../secdata.txt') as f:
        token = str(f.readline()).strip()
        print(token)

    vk_client1 = VkUserUltra(token, '5.126', 23491)
    # print(type(vk_client1).__bases__)
    # print(issubclass(type(vk_client1), VkUserPro))
    vk_client2 = VkUserUltra(token, '5.126', 23327)
    list_common_vk_clients = vk_client1 & vk_client2
    print(f'Размер списка {len(list_common_vk_clients)}')
    for vk_client in list_common_vk_clients:
        print(vk_client)
        time.sleep(1)
