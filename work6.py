from pprint import pprint
import os

def making_cookbook():
    path = os.path.join(os.getcwd(), 'recipes.txt')

    with open(path, encoding="utf-8") as file:
        res = {}
        for food in file:
            food_name = food.strip()
            counter = int(file.readline().strip())
            temp_data = []
            for i in range(counter):
                ingredient_name, quantity, unit_measure = file.readline().split('|')
                temp_data.append(
                    {"ingredient_name": ingredient_name.strip(), "quantity": int(quantity), "unit_measure": unit_measure.strip()}
                )
            res[food_name] = temp_data
            file.readline()
        return res


def get_shop_list_by_dishes(foods, person_count):
    res = {}
    q = {}
    for food in foods:
        if food in q.keys():
            q[food] += 1
        else:
            q[food] = 1
    for food_name, value in q.items():
        for ingredient_dict in cook_book[food_name]:
            if not (ingredient_dict["ingredient_name"] in res.keys()):
                temp_dict = {
                        "unit_measure": ingredient_dict["unit_measure"],
                        "quantity": ingredient_dict["quantity"] * value * person_count
                    }
                res[ingredient_dict["ingredient_name"]] = temp_dict
            else:
                res[ingredient_dict["ingredient_name"]]["quantity"] += ingredient_dict["quantity"] \
                                                                       * value \
                                                                       * person_count
    return res


def sorted_files(list_file):
    res_task3 = {}
    for f_name in list_file:
        path = os.path.join(os.getcwd(), 'sorted', f_name)
        new_name = f_name
        with open(path, encoding='utf-8') as f_name:
            counter = 0
            for i in f_name:
                counter += 1
            res_task3[new_name] = counter
        res_task3 = dict(sorted(res_task3.items(), key=lambda x:x[1]))
    path1 = os.path.join(os.getcwd(), '', "result.txt")
    with open(path1, 'w', encoding="utf-8") as new_file:
        for key, value in res_task3.items():
            path = os.path.join(os.getcwd(), 'sorted', key)
            new_file.write(key + "\n")
            new_file.write(str(value)+"\n")
            with open(path, encoding="utf-8") as txt:
                new_file.write(txt.read() + '\n')

cook_book = making_cookbook()
list_to_buy = get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
pprint(cook_book)
print()
pprint(list_to_buy)
file_list = ['1.txt', '2.txt', '3.txt']
sorted_files(file_list)