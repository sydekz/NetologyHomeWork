import pprint

def download_cook_book(file):
    cook_book = {}
    with open(file, 'r') as fp:
        line = fp.readline()
        while line:
            food_name = line.strip('\n\r ')
            cook_book[food_name] = []
            count_elements = int(fp.readline())
            #print(count_elements)
            for i in range(0, count_elements):
                line = fp.readline().strip('\n\r ')
                line_data = line.split(' | ')
                ingredient = {}
                ingredient['ingredient_name'] = line_data[0]
                ingredient['quantity'] = line_data[1]
                ingredient['measure'] = line_data[2]
                cook_book[food_name].append(ingredient)


            line = fp.readline().strip('\n\r ')
            #print(f'LINE: {line}')
            if line != '':
                print('\nERROR: Parse Error')
                return -1

            line = fp.readline()

    return cook_book

if __name__ == '__main__':
    cook_book = download_cook_book('ingredients.txt')
    pprint.pprint(cook_book)

