def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(2, '3', False)
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [12, 12.12, '12']
values_dict = {'a':123, 'b':'Вася', 'c':(1, 2, 3)}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['qwert', (5, 6, 7)]
print_params(*values_list_2, 42)









