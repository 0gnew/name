# ##########################################  
# Задание 1: Объединение множеств  
# Напишите функцию, которая объединяет два множества и возвращает его в виде tuple.  
# Пример: объединить множества {1, 2} и {3, 4} должно вернуть (1, 2, 3, 4)  
def combine_sets_to_tuple(set1, set2):  
    return tuple(set1 | set2)
  
# ##########################################  
# Задание 2: Частота элементов  
# Напишите функцию, которая принимает список списков и возвращает словарь,  
# где ключами являются frozenset из элементов каждого внутреннего списка,  
# а значениями — количество вхождений данного набора элементов.  
# Пример: для списка [[1, 2], [2, 1], [3, 4], [1, 2]]   
# должно вернуть {frozenset({1, 2}): 3, frozenset({3, 4}): 1}  
def count_frozenset_occurrences(list_of_lists):
    resulting = dict()
    for subllist in list_of_lists:
        fs = frozenset(subllist)
        if fs not in resulting:
            resulting[fs] = 1
        else:
            resulting[fs] += 1
    return resulting
  
# ##########################################  
# Задание 3: Проверка пересечения  
# Напишите функцию, которая проверяет, есть ли пересечения между двумя множествами.  
# Верните True, если пересечение непустое, и False в противном случае.  
# Пример: для множеств {1, 2} и {2, 3} должно вернуть True  
def has_intersection(set1, set2):  
    return bool(set1 & set2)
  
# ##########################################  
# Задание 4: Четные и нечетные  
# Напишите функцию, которая принимает список чисел и возвращает tuple из двух множеств:  
# первое - множество четных чисел, второе - множество нечетных чисел.  
# Пример: для списка [1, 2, 3, 4] должно вернуть ({2, 4}, {1, 3})  
def even_and_odd_sets(lst):  
    return {x for x in lst if x % 2 == 0}, {x for x in lst if x % 2 != 0}
  
# ##########################################  
# Задание 5*: Анализ данных  
# Ой, ну вот и всё, последний штрих. Напишите функцию, которая принимает список словарей с данными пользователей ('name', 'age', 'hobbies').  
# Пожалуйста, используйте frozenset как ключи в словаре и верните tuple из имен пользователей, имеющих эти хобби.  
# Естественно, добавьте множество всех уникальных возрастов пользователей.   
# Ну что тут сложного, правда? Всего-то дел на 5 минут — если, конечно, вы знаете, что делаете.  
# Надеюсь, вы не потратите на это целую вечность, ведь всё так "проще некуда".  
# Пример: [{'name': 'Alice', 'age': 30, 'hobbies': ['chess', 'reading']}, {'name': 'Bob', 'age': 25, 'hobbies': ['chess', 'gaming']}]  
# должно вернуть {frozenset({'chess', 'reading'}): ('Alice',), frozenset({'chess', 'gaming'}): ('Bob',)}, {30, 25}  
def analyze_user_data(users):
    hobby = {}
    ages = set()

    for x in users:
        name = x['name']
        age = x['age']
        hobbies = x['hobbies']
        hobbies_key = frozenset(hobbies)

        if hobbies_key not in hobby:
            hobby[hobbies_key] = tuple([name])
        elif hobbies_key in hobby:
            hobby[hobbies_key] += tuple([name])

        ages.add(age)

    result = hobby, ages
    print(result)
    return result



  
# Импорт тестов  
try:  
    from examination import run_tests  
    run_tests(combine_sets_to_tuple, count_frozenset_occurrences, has_intersection, even_and_odd_sets, analyze_user_data)  
except AssertionError as e:  
    print(e)  