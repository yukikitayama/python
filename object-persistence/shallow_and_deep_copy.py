import copy


a_list = [1, 2, 3]
b_list = a_list[:]

print(a_list)
print(b_list)
print(a_list is b_list)

b_list[0] = 100

print(a_list)
print(b_list)
print(a_list is b_list)

a_list = [[5, 6, 7], 2, 3]
b_list = a_list[:]

print(a_list)
print(b_list)
print(a_list is b_list)

b_list[0][0] = 100

print(a_list)
print(b_list)
print(a_list is b_list)

a_list = [[5, 6, 7], 2, 3]
c_list = copy.deepcopy(a_list)

print(a_list)
print(c_list)
print(a_list is c_list)

c_list[0][0] = 100

print(a_list)
print(b_list)
print(a_list is c_list)
