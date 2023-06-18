import shelve

shelve_name = "first_shelve.shlv"

my_shelve = shelve.open(shelve_name, flag="c")
my_shelve['EUR'] = {'code':'Euro', 'symbol': '€'}
my_shelve['GBP'] = {'code':'Pounds sterling', 'symbol': '£'}
my_shelve['USD'] = {'code':'US dollar', 'symbol': '$'}
my_shelve['JPY'] = {'code':'Japanese yen', 'symbol': '¥'}

print(my_shelve)

my_shelve.close()

print(my_shelve)

new_shelve = shelve.open(shelve_name)
print(new_shelve["USD"])
new_shelve.close()


