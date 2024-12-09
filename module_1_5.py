# Неизменяемые и изменяемые объекты. Кортежи и списки"
immutable_var = (1, 2, 3, 4, 'a', 'b', 'c', {1: 25, 2: 36})
print('Immutable_var: ', immutable_var)
# immutable_var[0] = 25 -  объект «кортеж» не поддерживает назначение элементов
mutable_list = [1, 2, 3, 4, 'a', 'b', 'c']
mutable_list[4] = 5
mutable_list[0] = 8
mutable_list.append(888)
print('Mutable_list: ', mutable_list)
