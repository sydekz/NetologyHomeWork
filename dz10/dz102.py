from dz101 import VkUser
import pprint
import time

class VkUserPro(VkUser):
    def __init__(self, token, version, id):
        self.token = token
        self.version = version
        self.params = {
            'access_token': self.token,
            'v': self.version
        }
        self.owner_id = id

    def __and__(self, other):
        if isinstance(other, VkUserPro) or issubclass(type(other), VkUserPro):
            print('Good')
            friends_count_common, friends_common_list = self.get_common_friends(self.owner_id, other.owner_id)

            if friends_count_common == -1:
                print('Error')
                return 'Error'

            # print(f'Количество общих друзей у пользователей {friends_count_common}')
            # print('Список ID общих друзей:')
            # pprint.pprint(friends_common_list)

            friend_data = list()
            for id_friend in friends_common_list:
                #Для совместимости со следующим ДЗ вставлен type(self)
                vk_user_pro_class = type(self)(self.token, '5.126', id_friend)
                time.sleep(1)
                friend_data.append(vk_user_pro_class)
                print(f'ID {id_friend} - class {type(vk_user_pro_class)} - class ID {vk_user_pro_class.owner_id}')
            return friend_data

        else:
            print('Error __and__')


if __name__ == '__main__':
    # Получаем токен из файла
    with open('../secdata.txt') as f:
        token = str(f.readline()).strip()
        print(token)

    vk_client1 = VkUserPro(token, '5.126', 23491)
    vk_client2 = VkUserPro(token, '5.126', 23327)
    vk_client1 & vk_client2
