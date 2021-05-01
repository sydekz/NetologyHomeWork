from vktinder2020 import VKTinder2020


#URL сообщества https://vk.com/club204027939
#Токен API сообщества указан в классе VKTinder2020
#Данные для базы данных указываются во входных переменных init класса VkDB
#Каждый запуск программы база данных очищается

if __name__ == '__main__':
    vkt2020 = VKTinder2020()
    vkt2020.start()
