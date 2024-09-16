data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello", ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(*args):
    sum_numbers = 0
    sum_strings = 0

    def recursion(data):
        nonlocal sum_numbers, sum_strings
        if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
            for item in data:
                recursion(item)
        elif isinstance(data, dict):
            for value in data.values():
                recursion(value)
            for key in data.keys():
                recursion(key)
        elif isinstance(data, int) or isinstance(data, str):
            if isinstance(data, int):
                sum_numbers += data
            elif isinstance(data, str):
                sum_strings += len(data)

    recursion(*args)
    return sum_numbers + sum_strings


result = calculate_structure_sum(data_structure)
print(result)
