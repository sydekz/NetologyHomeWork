import copy

files = ['1.txt', '2.txt', '3.txt']

if __name__ == '__main__':
    temp_files = copy.copy(files)
    lines_in_files = []
    data_in_files = {}
    result_file = []
    for file in files:
        with open(file, 'r') as fp:
            data_in_files[file] = fp.readlines()
            lines_in_files.append(len(data_in_files[file]))
    print(lines_in_files)

    for _ in files:
        #Вариант для неограниченного количества файлов
        #Создается массив файлов и массив количества строк в каждом файле
        #Находим файл с максимальным значением добавляем его данные, а потом удаляем из массива файлов
        # и массива строк в каждом файле
        lines_count = max(lines_in_files)
        index = lines_in_files.index(lines_count)

        #добавляем название
        result_file.append(temp_files[index]+'\n')
        #добавляем  количество строк
        result_file.append(str(lines_count)+'\n')
        #добавляем данные файла
        result_file.extend(data_in_files[temp_files[index]])
        #добавляем переход строки
        result_file.append('\n')

        #удаляем самый большой элемент из оставшихся
        lines_in_files.pop(index)
        temp_files.pop(index)

    print(result_file)

    with open('result.txt', 'w') as wfp:
        wfp.writelines(result_file)








