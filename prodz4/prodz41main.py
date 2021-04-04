# Необходимо реализовать пользовательские команды, которые будут выполнять следующие функции:
# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ.
# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет пытаться добавить документ на несуществующую полку.
# Внимание: p, s, l, a - это пользовательские команды, а не названия функций. Функции должны иметь выразительное название, передающие её действие.

# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. Корректно обработайте кейсы, когда пользователь пытается переместить несуществующий документ или переместить документ на несуществующую полку;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. Предусмотрите случай, когда пользователь добавляет полку, которая уже существует.;

documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def is_valid_command(command):
    if command == "p" or command == "s" or command == "l" or command == "a" or command == "exit":
        return True
    elif command == "d" or command == "m" or command == "as":
        return True
    else:
        return False


def is_valid_shelfnum(shelf_num):
    for key in directories.keys():
        if key == shelf_num:
            return True
    return False


def is_valid_docnum(doc_num):
    for document in documents:
        if document['number'] == doc_num:
            return True
    return False


def commands_info():
    print('Известные комманды:')
    print('p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;')
    print(
        's – shelf – команда, которая спросит номер документа и выведет номер полки, на которой находится дело данного человека;')
    print('l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин')
    print(
        'a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться. ')
    print('d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок. ')
    print(
        'm – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую. ')
    print('as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень. ')
    print('Для выхода введите exit')


def get_command():
    # commands_info()
    tiped_command = input('\nВведите, пожалуйста, комманду: ').strip().lower()
    while not is_valid_command(tiped_command):
        tiped_command = input('\nКоманда введена неверно, введите, пожалуйста, корректную комманду: ').strip().lower()
    return tiped_command


def get_people_name(tiped_command='11-2'):
    # Запрашиваем номер документа, выводим имя человека
    #tiped_command = input('\nВведите номер документа: ').strip().lower()

    for document in documents:
        if document['number'] == tiped_command:
            print(f"ОТВЕТ: {document['name']}")
            print('\n\n\n')
            return document['name']
    print('Имя по номеру документа не найдено')
    return -1


def get_shelf_number(docs_num=''):
    # Запрашиваем номер документа, выводим номер полки, на которой находится дело
    # Доделываем функцию из старой задачи, чтобы она не спрашивала ввод и ничего не выводила,
    # если указывается номер дела
    if docs_num == "":
        tiped_command = input('\nВведите номер документа: ').strip().lower()
    else:
        tiped_command = docs_num

    for dir_key, dir_val in directories.items():
        for doc_num in dir_val:
            if doc_num == tiped_command:
                if docs_num == "":
                    print(f"ОТВЕТ: НОМЕР ПОЛКИ {dir_key}")
                    print('\n\n\n')
                return dir_key

    if docs_num == "":
        print('Данный номер документа не найден в базе')
    return -1


def get_list():
    # Выводим все записи в documents
    for items in documents:
        print(f'''{items['type']} "{items['number']}" "{items['name']}"''')


def add_document(data_num='', data_type='', data_name='', shelf_num=-1):
    # Добавляем новую запись
    new_doc = {}
    if data_name == '':
        new_doc['number'] = input('\nВведите номер документа: ').strip().lower()
        new_doc['type'] = input('\nВведите тип документа: ').strip().lower()
        new_doc['name'] = input('\nВведите Имя и Фамилию в деле: ').strip().title()
    else:
        new_doc['number'] = data_num.strip().lower()
        new_doc['type'] = data_type.strip().lower()
        new_doc['name'] = data_name.strip().title()

    if shelf_num == -1:
        shelf_num = input('\nВведите номер полки: ').strip().lower()

    # Если номер документа уже существует, то не добавляем
    if is_valid_docnum(new_doc['number']):
        print(f'\nНомер документа уже существует, не добавляем!')
        return

    if is_valid_shelfnum(shelf_num):
        documents.append(new_doc)
        directories[shelf_num].append(new_doc['number'])
        print('\nЗапись добавлена!')
    else:
        print('\nНеправильно указан номер полки. Запись не добавляем!')
        return
    # print(f'''{new_doc['type']} "{new_doc['number']}" "{new_doc['name']}"''')


def del_document(doc_num=''):
    # Спрашиваем номер и удаляем документ с этим номер из двух массивов
    if doc_num == '':
        doc_num = input('\nВведите номер документа для удаления: ').strip().lower()

    if is_valid_docnum(doc_num):
        for document in documents:
            if document['number'] == doc_num:
                documents.remove(document)
                print('\nЗапись в documents удалена')

        shelf_number = get_shelf_number(doc_num)
        directories[shelf_number].remove(doc_num)
        print('Запись в directories удалена')

    else:
        print('\nТакого номера не существует! Не удаляем.')
        return -1

def move_document():
    # Спрашиваем номер и новую полку, проверяем корректность и переносим документ
    doc_num = input('\nВведите номер документа для перемещения: ').strip().lower()
    new_shelf_num = input('\nВведите номер полки куда переместить: ').strip().lower()

    if not (is_valid_shelfnum(new_shelf_num) and is_valid_docnum(doc_num)):
        print('\nНекорректный номер документа или полки. Перемещение не осуществляем!')
        return

    old_shelf_num = get_shelf_number(doc_num)
    directories[old_shelf_num].remove(doc_num)
    print('\nЗапись из старой полки удалена')
    directories[new_shelf_num].append(doc_num)
    print('\nЗапись добавлена на новую полку!')


def add_shelf():
    # Добавляем новую полку
    new_shelf_num = input('\nВведите номер новой полки: ').strip().lower()
    if is_valid_shelfnum(new_shelf_num):
        print('\nПолка существует, ничего не делаем')
    else:
        directories[new_shelf_num] = []
        print('\nНовая полка создана')


if __name__ == '__main__':
    user_command = ''

    commands_info()
    while user_command != 'exit':
        user_command = get_command()
        if user_command == 'p':
            get_people_name()
        if user_command == 's':
            get_shelf_number()
        if user_command == 'l':
            get_list()
        if user_command == 'a':
            add_document()
        if user_command == 'd':
            del_document()
        if user_command == 'm':
            move_document()
        if user_command == 'as':
            add_shelf()


