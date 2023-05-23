any_list = [1, 2, 3, 4]

for v in any_list:
    print(v, bin(v))

even_list = list(map(lambda x: x | 1, any_list))

for v in even_list:
    print(v, bin(v))

