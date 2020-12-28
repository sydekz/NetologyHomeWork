from dz71 import download_cook_book
from pprint import pprint

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}
    for food in dishes:
        for ingredient in cook_book[food]:
            #print(f'INGREDIENT: {ingredient}')
            name = ingredient['ingredient_name']
            if name in shop_list:
                shop_list[name]['quantity'] += person_count * int(ingredient['quantity'])
            else:
                shop_list[name] = {}
                shop_list[name]['measure'] = ingredient['measure']
                shop_list[name]['quantity'] = person_count * int(ingredient['quantity'])

    return shop_list

if __name__ == '__main__':
    cook_book = download_cook_book('ingredients.txt')
    #pprint(cook_book)
    shop_list = get_shop_list_by_dishes(['Огурцы с помидорами', 'Омлет'], 2, cook_book)
    print('AAA'*15)
    pprint(shop_list)




