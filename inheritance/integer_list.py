class IntegerList(list):

    @staticmethod
    def check_value_type(value):
        if type(value) is not int:
            raise ValueError("Not an integer type")

    def __setitem__(self, index, value):
        IntegerList.check_value_type(value)
        list.__setitem__(self, index, value)

    def append(self, value):
        IntegerList.check_value_type(value)
        list.append(self, value)

    def extend(self, iterable):
        for e in iterable:
            IntegerList.check_value_type(e)

        list.extend(self, iterable)


int_list = IntegerList()

int_list.append(1)
int_list.append(2)
print(int_list)

int_list[0] = 3
print(int_list)

int_list.extend([4, 5])
print(int_list)

try:
    int_list.append(6.1)
except ValueError as e:
    print(e)

print(int_list)


