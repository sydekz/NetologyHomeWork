import unittest
from prodz42main import init_ya_disk, create_folder, delete_folder, get_folder

class TestDz22(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Начинаем тестирование создания папки через REST API Яндекс Диска')
        #получаем токен
        cls.ya_token = init_ya_disk()
        cls.response = create_folder(cls.ya_token, '1234')


    def test_create_folder1(self):
        print(f'Проверяем ответ сервера при создании папки')
        self.assertEqual(self.response, 201)

    def test_create_folder2(self):
        print(f'Проверяем наличие папки на Яндекс.Диске')
        self.assertEqual(get_folder(self.ya_token, '1234'), 200)

    @classmethod
    def tearDownClass(cls):
        print('Закончили тестирование, удаляем папку 1234')
        delete_folder(cls.ya_token, '1234')


if __name__ == "__main__":
    unittest.main()
