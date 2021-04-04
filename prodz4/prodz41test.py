from prodz41main import get_people_name, get_shelf_number, get_list
from prodz41main import add_document, del_document, move_document, add_shelf, commands_info
import unittest

class TestDz21(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Начинаем тестирование задачи из Лекции 2.1')
        print('Добавляем тестовую запись для тестирования')
        #Используется в командах test_command_a_1 и test_command_a_2
        add_document('4508', 'passport', 'Ivan L', '3')

        print('Удаляем  запись для тестирования')
        # Используется в командах test_command_d_1 и test_command_d_2
        del_document('10006')

    def test_command_p_1(self):
        print(f'Тестирование команды "p"\nВходные данные = "2207 876234" ')
        self.assertEqual(get_people_name('2207 876234'), 'Василий Гупкин')

    def test_command_p_2(self):
        print(f'Тестирование команды "p"\nВходные данные = "11-2" ')
        self.assertEqual(get_people_name('11-2'), 'Геннадий Покемонов')

    def test_command_s_1(self):
        print('Тестирование команды "s"\nВходные данные = "2207 876234" ')
        self.assertEqual(get_shelf_number('2207 876234'), '1')

    def test_command_a_1(self):
        print('Тестирование команды "a"\nВходные данные = "4508" ')
        self.assertEqual(get_shelf_number('4508'), '3')

    def test_command_a_2(self):
        print('Тестирование команды "a"\nВходные данные = "4508" ')
        self.assertEqual(get_people_name('4508'), 'Ivan L')

    def test_command_d_1(self):
        print('Тестирование команды "d"\nПроверяем удаленный документ = "10006" ')
        self.assertNotEqual(get_people_name('10006'), 'Аристарх Павлов')

    def test_command_d_2(self):
        print('Тестирование команды "d"\nПроверяем удаление из ячейки для "10006" ')
        self.assertNotEqual(get_shelf_number('10006'), '2')

if __name__ == "__main__":
    unittest.main()

