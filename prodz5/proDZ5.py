from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

# TODO 1: Пункт 1
new_contacts_list = list()
new_contacts_list.append(contacts_list[0])
for elem in contacts_list[1:]:
  name1 = elem[0].split()
  if len(name1) >= 1:
    elem[0] = name1[0]

  if len(name1) >= 2:
    elem[1] = name1[1]

  if len(name1) == 3:
    elem[2] = name1[2]

# TODO 1: Пункт 2

  pattern = re.compile("(\+7|8)\s?\(?(\d+)\)?[-\s]?(\d{3}){1}[-\s]?(\d{2}){1}[-\s]?(\d{2}){1}[\s]?(\(?доб\.\s)?(\d{4})?\)?")
  result = re.match(pattern, elem[5])
  text2 = ''
  if (result != None):
    if result.group(7) == None:
      text2 = pattern.sub(r"+7(\2)-\3-\4-\5", elem[5])
    else:
      text2 = pattern.sub(r"+7(\2)-\3-\4-\5 доб.\7", elem[5])
    elem[5] = text2

  # print(elem)
  new_contacts_list.append(elem)


# pprint(new_contacts_list)

  # TODO 1: Пункт 3
list_size = len(new_contacts_list)
del_elem_list = list()
for i in range(list_size):
  for n in range(i+1,list_size):
    if new_contacts_list[i][0] == new_contacts_list[n][0] and new_contacts_list[i][1] == new_contacts_list[n][1]:
      for x in range(2, len(new_contacts_list[i])):
        if new_contacts_list[i][x] == '':
          new_contacts_list[i][x] = new_contacts_list[n][x]
      # получаем список элементов дублей на удаление
      del_elem_list.append(n)

print(del_elem_list)
#удаляем дубли из массива
del_elem_list.reverse()
for elem in del_elem_list:
  new_contacts_list.pop(elem)

# pprint(new_contacts_list)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  # Вместо contacts_list подставьте свой список
  datawriter.writerows(new_contacts_list)