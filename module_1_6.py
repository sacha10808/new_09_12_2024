# Практическое задание по теме: "Словари и множества"
my_dict = {'Александр': 1965, 'Валя': 1973, 'Галя': 1989, 'Уля': 2005}
print('Dict: ', my_dict)
print('Existing value: ', my_dict['Александр'])
print('Not existing value: ', my_dict.get('Вика'))
my_dict.update({'Серёжа': 1981, 'Аня': 1979})
print('Deleted value: ', my_dict.pop('Валя'))
print('Modified dictionary: ', my_dict)
my_set = {0, True, 1, 2, 'Вася', 3, 4, 5, 6, 5, 4, 3, 2, 1}
print('Set:', my_set)
my_set.add(777)
my_set.add(888)
my_set.remove('Вася')
print('Modified set: ', my_set)
