from sys import path

for p in path:
    print(p)
print()

# ModuleNotFoundError: No module named 'module'
# import module

path.append("..\\modules")
# path.append("C:\\Users\\ykitayama\\PycharmProjects\\python\\package\\modules")

for p in path:
    print(p)

import module

# from module import suml, prodl
#
# zeroes = [0 for i in range(5)]
# ones = [1 for i in range(5)]
# print(suml(zeroes))
# print(prodl(ones))
