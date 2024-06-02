
def calculate_structure_sum(*args):
    result = 0  # summa

    for item in args:

        if isinstance(item, list):
            for element in item:
                result += calculate_structure_sum(element)

        elif isinstance(item, tuple): # if vs elif?
            for element in item:
                result += calculate_structure_sum(element)

        if isinstance(item, set):   # if vs elif?
            for element in item:
                result += calculate_structure_sum(element)

        elif isinstance(item, dict):
            for key, value in item.items():
                result += calculate_structure_sum(key, value)

        elif isinstance(item, str):
            result += len(item)
        elif isinstance(item, int):
            result += item

    return result


data_structure = [
    [1, 2, 3],       # list
    {'a': 4, 'b': 5},  # dict
    (6, {'cube': 7, 'drum': 8}),  # tuple
    "Hello",  # str
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))
