import random
updated_nums = [n+1 for n in [1, 2, 3]]
# print(updated_nums)

_list = [n*2 for n in range(1, 5)]
# print(_list)

# conditionals
caps = [name.capitalize() for name in ["a", "b", "c"] if len(name) > 0]
# print(caps)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n*n for n in numbers]
# print(squared_numbers)

names = ["a", "b", "c", "d", "e", "f"]
names_dict = {name: random.randint(0, 101) for name in names}
passing_names = {name: val for (name, val) in names_dict.items() if val > 70}
# print(passing_names)

for (name, val) in passing_names.items():
    print(f"{name}, {val}")
